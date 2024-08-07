from datetime import timedelta
from dataclasses import asdict

from core.entities.plant import Plant
from core.entities.line_chart_record import LineChartRecord
from core.constants import DAYS_RANGES


class LineChart:
    def __init__(self, records: list[LineChartRecord]):
        self.records = [asdict(record) for record in records]

    def get_data(self, plants: list[Plant]):
        chart_data = {
            plant.id: {
                f"{days_range} days": {"values": [], "dates": [], "average": 0}
                for days_range in DAYS_RANGES
            }
            for plant in plants
        }

        for days_range in DAYS_RANGES:
            for plant in plants:
                days_range_records = self.__filter_records_by_range_of_days(
                    days_range, plant.id
                )

                if not len(days_range_records):
                    continue

                values = []
                dates = []

                for record in days_range_records:
                    if record["plant_id"] == plant.id:
                        dates.append(record["date"])
                        values.append(record["value"])

                total = sum([record for record in values])
                values_count = len(values)
                average = total / len(values) if values_count > 0 else 0

                days_range_key = f"{days_range} days"

                chart_data[plant.id][days_range_key]["values"] = values
                chart_data[plant.id][days_range_key]["average"] = average
                chart_data[plant.id][days_range_key]["dates"] = dates

        return chart_data

    def __filter_records_by_range_of_days(self, days_range: int, plant_id: str):
        last_date = self.__get_last_record_date_by_plant(plant_id)

        if last_date is None:
            return []

        data = []

        for day in range(days_range - 1, -1, -1):
            current_date = last_date - timedelta(days=day)

            for record in self.records:
                if record["date"] == current_date:
                    data.append(
                        {
                            **record,
                            "date": record["date"].strftime("%d/%m/%Y"),
                        }
                    )

        return data

    def __get_last_record_date_by_plant(self, plant_id: str):
        for index in range(1, len(self.records) + 1):
            record = self.records[-index]

            if record["plant_id"] == plant_id:
                return record["date"]
