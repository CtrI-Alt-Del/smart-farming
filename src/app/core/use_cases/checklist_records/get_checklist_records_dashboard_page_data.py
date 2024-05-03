from core.constants import LEAF_APPEARANCES, LEAF_COLORS
from core.commons import Error, Chart

from datetime import timedelta

from infra.repositories import checklist_records_repository, plants_repository


class GetChecklistRecordsDashboardPageData:
    def execute(self):
        try:
            plants = plants_repository.get_plants()

            #fiz isso pq dava JSON not possible sem
            plants_dict = [
                {
                    "id": plant.id,
                    "name": plant.name,
                    "hex_color":plant.hex_color
                }
                for plant in plants
            ]

            records = checklist_records_repository.get_ordered_by_date_leaf_appearances_and_leaf_colors_records()

            days_count_by_leaf_appearance = {
                leaf_appearance: 0 for leaf_appearance in LEAF_APPEARANCES
            }
            days_count_by_leaf_appearance_and_plant = {
                plant["id"]: days_count_by_leaf_appearance for plant in plants_dict
            }

            days_count_by_leaf_color = {leaf_color: 0 for leaf_color in LEAF_COLORS}
            days_count_by_leaf_color_and_plant = {
                plant["id"]: days_count_by_leaf_color for plant in plants_dict
            }

            for plant in plants_dict:
                for leaf_appearance in LEAF_APPEARANCES:
                    for record in records:
                        if (
                            record["leaf_appearance"] == leaf_appearance
                            and record["plant_id"] == plant["id"]
                        ):
                            days_count_by_leaf_appearance_and_plant[plant["id"]][
                                leaf_appearance
                            ] += 1

                for leaf_color in LEAF_COLORS:
                    for record in records:
                        if record["leaf_color"] == leaf_color:
                            days_count_by_leaf_color_and_plant[plant["id"]][
                                leaf_color
                            ] += 1

            return {
                "days_count_by_leaf_appearance_and_plant": days_count_by_leaf_appearance_and_plant,
                "days_count_by_leaf_color_and_plant": days_count_by_leaf_color_and_plant,
                "plants": plants_dict,
            }
        except Error as error:
            raise error

    def get_plant_growth_chart_data(self):
        records = checklist_records_repository.get_plant_growth_grouped_by_date()
        
        if len(records) == 0:
            raise Error("Sem nenhum registro cadastrado no sistema")

        
        
        chart = Chart(records)
        
        charts_filtered_data = {}
        
        for days in [7, 30, 90]:
            charts_filtered_data[f"{days} days"] = (
                {
                    "records": chart.filter_records_by_range_of_days(days),
                    "average": self.get_checklist_records_grouped_by_date(
                        days, records
                    ),
                },
            )[0]
        
        print(charts_filtered_data,flush=True)
        return charts_filtered_data
        
    def get_checklist_records_grouped_by_date(
        self, days_range, checklist_records_grouped_by_date
    ):
        last_date = checklist_records_grouped_by_date[-1]["date"]
        total = {
            "plant_growth":0
        }
        checklist_records_count = 0

        for day in range(days_range, -1, -1):
            current_date = last_date - timedelta(days=day)

            for checklist_record in checklist_records_grouped_by_date:
                if checklist_record["date"] == current_date:
                    for attribute, value in checklist_record.items():
                        if attribute == "date":
                            continue

                        total[attribute] += value

                    checklist_records_count += 1

        average = {
            "plant_growth": 0,
            
        }

        for attribute, value in total.items():
            average[attribute] += round(value / checklist_records_count, 2)

        return average
