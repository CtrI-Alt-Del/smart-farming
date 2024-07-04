from .create_checklist_records_by_csv_file_factory import (
    CreateChecklistRecordsByCsvFileFactory,
)
from .create_checklist_record_by_form_factory import CreateChecklistRecordByFormFactory
from .delete_checklist_records_factory import DeleteChecklistRecordsFactory
from .get_checklist_records_csv_file_factory import GetChecklistRecordsCsvFileFactory
from .get_checklist_records_dashboard_page_data_factory import (
    GetChecklistRecordsDashboardPageDataFactory,
)
from .get_checklist_records_table_page_data_factory import (
    GetChecklistRecordsTablePageDataFactory,
)
from .update_checklist_records_factory import UpdateChecklistRecordFactory


create_checklist_records_by_csv_file = CreateChecklistRecordsByCsvFileFactory.produce()
create_checklist_record_by_form = CreateChecklistRecordByFormFactory.produce()
delete_checklist_records = DeleteChecklistRecordsFactory.produce()
get_checklist_records_csv_file = GetChecklistRecordsCsvFileFactory.produce()
get_checklist_records_dashboard_page_data = (
    GetChecklistRecordsDashboardPageDataFactory.produce()
)
get_checklist_records_table_page_data = (
    GetChecklistRecordsTablePageDataFactory.produce()
)
update_checklist_record = UpdateChecklistRecordFactory.produce()
