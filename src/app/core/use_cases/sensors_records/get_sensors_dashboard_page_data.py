from infra.repositories import sensors_records_repository
from core.commons.chart_filter import ChartFilter

class GetSensorDashboardPageData:
    def execute(self):
        sensor_records = sensors_records_repository.get_sensor_records()
        chartFilter = ChartFilter(sensor_records)
        options = {
            "150 days": chartFilter.filter_records_by_range_of_date(150),
            "300 days": chartFilter.filter_records_by_range_of_date(300),
            "450 days": chartFilter.filter_records_by_range_of_date(450),
        }
        return options