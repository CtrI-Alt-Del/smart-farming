from core.constants import LEAF_APPEARANCES, LEAF_COLORS, ADMIN_USER_EMAIL
from core.commons import LineChart, OrderedPlants
from core.errors.plants import PlantNotFoundError
from core.errors.checklist_records import ChecklistRecordNotFoundError
from core.interfaces.repositories import (
    PlantsRepositoryInterface,
    UsersRepositoryInterface,
    ChecklistRecordsRepositoryInterface,
)


class GetChecklistRecordsDashboardPageData:
    def __init__(
        self,
        plants_repository: PlantsRepositoryInterface,
        users_repository: UsersRepositoryInterface,
        checklist_records_repository: ChecklistRecordsRepositoryInterface,
    ):
        self._plants_repository = plants_repository
        self._users_repository = users_repository
        self._checklist_records_repository = checklist_records_repository

    def execute(self):
        plants = self._plants_repository.get_plants()

        if len(plants) == 0:
            raise PlantNotFoundError()

        active_plant_id = self._users_repository.get_user_active_plant_id(
            ADMIN_USER_EMAIL
        )

        ordered_plants = OrderedPlants(plants, active_plant_id)

        leaf_records = (
            self._checklist_records_repository.get_leaf_appearances_and_leaf_colors_records()
        )

        if len(leaf_records) == 0:
            raise ChecklistRecordNotFoundError()

        plants = ordered_plants.get_value()

        leaf_charts_data = self.__get_leaf_charts_data(leaf_records, plants)

        lai_records = (
            self._checklist_records_repository.get_lai_records_for_line_charts()
        )

        if len(lai_records) == 0:
            raise ChecklistRecordNotFoundError()

        plant_growth_chart = LineChart(lai_records)

        plant_growth_chart_data = plant_growth_chart.get_data(plants)

        return {
            **leaf_charts_data,
            "plant_growth_chart_data": plant_growth_chart_data,
            "plants": plants,
            "active_plant_id": active_plant_id,
        }

    def __get_leaf_charts_data(self, records, plants):
        days_count_by_leaf_appearance_and_plant = {
            plant.id: {leaf_appearance: 0 for leaf_appearance in LEAF_APPEARANCES}
            for plant in plants
        }

        days_count_by_leaf_color_and_plant = {
            plant.id: {leaf_color: 0 for leaf_color in LEAF_COLORS} for plant in plants
        }

        for plant in plants:
            for leaf_appearance in LEAF_APPEARANCES:
                for record in records:
                    if (
                        record["leaf_appearance"] == leaf_appearance
                        and record["plant_id"] == plant.id
                    ):
                        days_count_by_leaf_appearance_and_plant[plant.id][
                            leaf_appearance
                        ] += 1

            for leaf_color in LEAF_COLORS:
                for record in records:
                    if (
                        record["leaf_color"] == leaf_color
                        and record["plant_id"] == plant.id
                    ):
                        days_count_by_leaf_color_and_plant[plant.id][leaf_color] += 1

        return {
            "days_count_by_leaf_appearance_and_plant": days_count_by_leaf_appearance_and_plant,
            "days_count_by_leaf_color_and_plant": days_count_by_leaf_color_and_plant,
        }
