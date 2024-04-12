from infra.repositories import checklist_records_repository
from core.commons.chart import Chart

class GetChecklistDashboardPageData():
    def execute(self):
        checklist_records = checklist_records_repository.get_checklist_records()
        chartFilter = Chart(checklist_records)
        options = {
             "7 days":chartFilter.filter_records_by_range_of_date(7),
             "30 days":chartFilter.filter_records_by_range_of_date(30),
             "90 days":chartFilter.filter_records_by_range_of_date(90)
        }
        return options
            
