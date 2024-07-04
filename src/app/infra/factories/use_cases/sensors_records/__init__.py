from .create_sensors_record_by_api_factory import CreateSensorsRecordByApiFactory
from .create_sensors_records_by_csv_file_factory import (
    CreateSensorsRecordsByCsvFileFactory,
)
from .create_sensors_records_by_form_factory import CreateSensorsRecordByFormFactory
from .delete_sensors_records_factory import DeleteSensorsRecordFactory
from .get_sensors_records_csv_file_factory import GetSensorsRecordsCsvFileFactory
from .get_sensors_records_dashboard_page_data_factory import (
    GetSensorsRecordsDashboardPageDataFactory,
)
from .get_last_sensors_record_page_data_factory import (
    GetLastSensorsRecordPageDataFactory,
)
from .get_sensors_records_table_page_data_factory import (
    GetSensorsRecordsTablePageDataFactory,
)
from .update_sensors_records_factory import UpdateSensorsRecordFactory


create_sensors_record_by_api = CreateSensorsRecordByApiFactory.produce()
create_sensors_records_by_csv_file = CreateSensorsRecordsByCsvFileFactory.produce()
create_sensors_records_by_form = CreateSensorsRecordByFormFactory.produce()
delete_sensors_records = DeleteSensorsRecordFactory.produce()
get_sensors_records_csv_file = GetSensorsRecordsCsvFileFactory.produce()
get_last_sensors_record_page_data = GetLastSensorsRecordPageDataFactory.produce()
get_sensors_records_dashboard_page_data = (
    GetSensorsRecordsDashboardPageDataFactory.produce()
)
get_sensors_records_table_page_data = GetSensorsRecordsTablePageDataFactory.produce()
update_sensors_record = UpdateSensorsRecordFactory.produce()
