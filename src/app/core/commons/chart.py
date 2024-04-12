from typing import List, Dict
from datetime import timedelta


class Chart:
    def __init__(self, records: List[Dict]) -> None:
        self.records = records

    def filter_records_by_range_of_days(self, days_range):
        last_date = self.records[-1]["date"]
        data = []

        for day in range(days_range, -1, -1):
            current_date = last_date - timedelta(days=day)

            for sensors_record in self.records:
                if sensors_record["date"] == current_date:
                    data.append(
                        {
                            **sensors_record,
                            "date": sensors_record["date"].strftime("%d/%m/%Y"),
                        }
                    )

        return data
