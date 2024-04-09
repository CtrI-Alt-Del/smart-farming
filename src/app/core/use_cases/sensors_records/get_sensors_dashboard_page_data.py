from datetime import date, timedelta
from infra.repositories import sensors_records_repository


class GetSensorDashboardPageData:
    def execute(self):
        sensor_records = sensors_records_repository.get_sensor_records()
        options = {
            "150 days": self.filter_sensor_records_by_range_of_date(
                150, sensor_records
            ),
            "300 days": self.filter_sensor_records_by_range_of_date(
                300, sensor_records
            ),
            "450 days": self.filter_sensor_records_by_range_of_date(
                450, sensor_records
            ),
        }
        print(options)
        return options

    def filter_sensor_records_by_range_of_date(self, range_days, sensor_records):
        current_date = date.today()
        wanted_data = []
        for day in range(range_days, 0, -1):
            wanted_date = current_date - timedelta(days=day)
            for sensors_record in sensor_records:
                created_at_date = sensors_record.created_at.date()

                if created_at_date == wanted_date:
                    wanted_data.append(sensors_record)

        return wanted_data
