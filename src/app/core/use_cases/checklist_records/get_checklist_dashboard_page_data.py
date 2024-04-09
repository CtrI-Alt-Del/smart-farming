from infra.repositories import checklist_records_repository
from core.commons.chart_filter import ChartFilter

class GetSensorDashboardPageData():
    def execute(self):
        checklist_records = checklist_records_repository.get_checklist_records()
        chartFilter = ChartFilter(checklist_records)
        options = {
             "7 DAYS":chartFilter.filter_records_by_range_of_date(7),
             "30 DAYS":chartFilter.filter_records_by_range_of_date(30),
             "90 DAYS":chartFilter.filter_records_by_range_of_date(90)
        }
        return options
        

            