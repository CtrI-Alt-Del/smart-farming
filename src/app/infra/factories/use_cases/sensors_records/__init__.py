from .create_sensors_record_by_api_factory import CreateSensorsRecordByApiFactory
from .create_sensors_records_by_csv_file_factory import (
    CreateSensorsRecordsByCsvFileFactory,
)
from .delete_sensors_records_factory import DeleteSensorsRecordFactory
from .get_sensors_records_csv_file_factory import GetSensorsRecordsCsvFileFactory
from .get_sensors_dashboard_page_data_factory import GetSensorDashboardPageDataFactory
from .update_sensors_records_factory import UpdateSensorsRecordFactory


create_sensors_record_by_api = CreateSensorsRecordByApiFactory.produce()
create_sensors_records_by_csv_file = CreateSensorsRecordsByCsvFileFactory.produce()
delete_sensors_records_factory = DeleteSensorsRecordFactory.produce()
get_sensors_records_csv_file_factory = GetSensorsRecordsCsvFileFactory.produce()
get_last_sensors_record_page_data_factory = CreateSensorsRecordByApiFactory.produce()
get_sensors_dashboard_page_data = GetSensorDashboardPageDataFactory.produce()
update_sensors_records_factory = UpdateSensorsRecordFactory.produce()
