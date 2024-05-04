from datetime import timedelta

from core.commons.error import Error
from core.constants import DAYS_RANGES


class LineChart:
    def __init__(self, records: list[dict], attribute):
        self.records = []

        for record in records:
            for required_attribute in ["date", "plant_id", attribute]:
                if required_attribute not in record:
                    raise Error("Required attribute not found in record")

            self.records.append(
                {
                    "date": record["date"],
                    "plant_id": record["plant_id"],
                    "value": record[attribute],
                }
            )

    def filter_records_by_range_of_days(self, days_range):
        last_record = self.records[-1]
        last_date = last_record["date"]
        data = []

        for day in range(days_range - 1, -1, -1):
            current_date = last_date - timedelta(days=day)

            if days_range == 7:
                print(current_date, flush=True)

            for record in self.records:
                if record["date"] == current_date:
                    data.append(
                        {
                            **record,
                            "date": record["date"].strftime("%d/%m/%Y"),
                        }
                    )

        return data

    def get_data(self, plants):
        chart_data = {
            plant.id: {
                f"{days_range} days": {"values": [], "dates": [], "average": 0}
                for days_range in DAYS_RANGES
            }
            for plant in plants
        }

        for days_range in DAYS_RANGES:
            for plant in plants:
                days_range_records = self.filter_records_by_range_of_days(days_range)

            values = []
            dates = []

            for record in days_range_records:
                if record["plant_id"] == plant.id:
                    days_range_key = f"{days_range} days"

                    dates.append(record["date"])
                    values.append(record["value"])

            total = sum([record for record in values])
            average = total / len(values)

            chart_data[plant.id][days_range_key]["values"] = values
            chart_data[plant.id][days_range_key]["average"] = average
            chart_data[plant.id][days_range_key]["dates"] = dates

        return chart_data
