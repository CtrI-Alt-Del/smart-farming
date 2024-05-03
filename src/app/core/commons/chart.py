from typing import List, Dict
from datetime import timedelta

from core.commons.error import Error


class Chart:
    def __init__(self, records: List[Dict]) -> None:
        for record in records:
            if "date" not in record:
                raise Error("Date attribute not found in record")

        self.records = records

    def filter_records_by_range_of_days(self, days_range):
        last_record = self.records[-1]
        last_date = last_record["date"]
        data = []

        for day in range(days_range, -1, -1):
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
