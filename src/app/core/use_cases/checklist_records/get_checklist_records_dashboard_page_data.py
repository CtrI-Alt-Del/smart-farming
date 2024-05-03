from core.constants import LEAF_APPEARANCES, LEAF_COLORS
from core.commons import Error

from infra.repositories import checklist_records_repository, plants_repository


class GetChecklistRecordsDashboardPageData:
    def execute(self):
        try:
            plants = plants_repository.get_plants()

            records = (
                checklist_records_repository.get_ordered_by_date_leaf_appearances_and_leaf_colors_records()
            )

            days_count_by_leaf_appearance = {
                leaf_appearance: 0 for leaf_appearance in LEAF_APPEARANCES
            }
            days_count_by_leaf_appearance_and_plant = {
                plant.id: days_count_by_leaf_appearance for plant in plants
            }

            days_count_by_leaf_color = {leaf_color: 0 for leaf_color in LEAF_COLORS}
            days_count_by_leaf_color_and_plant = {
                plant.id: days_count_by_leaf_color for plant in plants
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
                        if record["leaf_color"] == leaf_color:
                            days_count_by_leaf_color_and_plant[plant.id][
                                leaf_color
                            ] += 1

            return {
                "days_count_by_leaf_appearance_and_plant": days_count_by_leaf_appearance_and_plant,
                "days_count_by_leaf_color_and_plant": days_count_by_leaf_color_and_plant,
                "plants": plants,
            }
        except Error as error:
            raise error