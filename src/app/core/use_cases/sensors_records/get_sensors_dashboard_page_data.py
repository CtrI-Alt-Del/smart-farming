from datetime import date,timedelta
from infra.repositories import sensors_records_repository

class GetSensorDashboardPageData():
    def execute(self):
        sensor_records = sensors_records_repository.get_sensor_records()
        options = {
             "7 DAYS":self.filter_sensor_records_by_range_of_date(7,sensor_records),
             "30 DAYS":self.filter_sensor_records_by_range_of_date(30,sensor_records),
             "90 DAYS":self.filter_sensor_records_by_range_of_date(90,sensor_records)
        }
        return options
    def filter_sensor_records_by_range_of_date(self , range_days,sensor_records):
            current_date = date.today()
            wanted_data = []
            for day in range(range_days,0,-1):
                wanted_date = current_date - timedelta(days=day)
                for sensors_record in sensor_records:
                    if sensors_record.created_at == wanted_date:
                        wanted_data.append(sensors_record)
            return wanted_data
        

            
