from datetime import date,timedelta

class ChartFilter:

    def __init__(self, records) -> None:
        self.records = records


    def filter_records_by_range_of_date(self , range_days):
        current_date = date.today()
        wanted_data = []
        for day in range(range_days,0,-1):
            wanted_date = current_date - timedelta(days=day)
            for record in self.records:
                if record.created_at == wanted_date:
                    wanted_data.append(record)
        return wanted_data