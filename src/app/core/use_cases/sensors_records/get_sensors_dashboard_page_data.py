from datetime import timedelta

from core.commons.chart import Chart

from infra.repositories import sensors_records_repository


class GetSensorDashboardPageData:
    def execute(self):
        sensor_records_grouped_by_date = (
            sensors_records_repository.get_sensor_records_grouped_by_date()
        )

        chart = Chart(sensor_records_grouped_by_date)

        charts_filtered_data = {}

        for days in [7, 30, 90]:
            charts_filtered_data[f"{days} days"] = (
                {
                    "records": chart.filter_records_by_range_of_days(days),
                    "average": self.get_sensors_records_average_by_range_of_days(
                        days, sensor_records_grouped_by_date
                    ),
                },
            )[0]

        return charts_filtered_data

    def get_sensors_records_average_by_range_of_days(
        self, range_days, sensor_records_grouped_by_date
    ):
        last_date = sensor_records_grouped_by_date[-1]["date"]
        total = {
            "soil_humidity": 0,
            "ambient_humidity": 0,
            "temperature": 0,
            "water_volume": 0,
        }
        sensors_records_count = 0

        for day in range(range_days, -1, -1):
            current_date = last_date - timedelta(days=day)

            for sensors_record in sensor_records_grouped_by_date:
                if sensors_record["date"] == current_date:
                    for attribute, value in sensors_record.items():
                        if attribute == "date":
                            continue

                        total[attribute] += value

                    sensors_records_count += 1

        average = {
            "soil_humidity": 0,
            "ambient_humidity": 0,
            "temperature": 0,
            "water_volume": 0,
        }

        for attribute, value in total.items():
            average[attribute] += round(value / sensors_records_count, 2)

        return average
