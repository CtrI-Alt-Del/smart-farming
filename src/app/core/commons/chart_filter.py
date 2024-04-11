from datetime import date,timedelta
from infra.utils.error import Error

class ChartFilter:

    def __init__(self, records) -> None:
        self.records = records


    def filter_records_by_range_of_date(self , range_days):
        current_date = date.today()
        wanted_data = []
        try:
            for day in range(range_days,0,-1):
                wanted_date = current_date - timedelta(days=day)
                for record in self.records:
                    if record.created_at.date() == wanted_date:
                        wanted_data.append(record)
        except Error as error:
            raise error
        return wanted_data