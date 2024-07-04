from pytest import fixture

from core.use_cases.tests.mocks.repositories import SensorRecordsRepositoryMock
from core.entities.tests.fakers import SensorsRecordsFaker
from core.entities import SensorsRecord

from ..get_last_sensors_record_page_data import GetLastSensorsRecordPageData


def describe_get_last_sensors_record_page_data_use_case():
    @fixture
    def sensors_records_repository():
        return SensorRecordsRepositoryMock()

    @fixture
    def use_case(
        sensors_records_repository: SensorRecordsRepositoryMock,
    ):
        sensors_records_repository.clear_records()
        return GetLastSensorsRecordPageData(
            sensors_records_repository=sensors_records_repository,
        )

    def it_should_get_empty_sensors_record_if_there_is_no_record_in_repository(
        use_case: GetLastSensorsRecordPageData,
    ):
        data = use_case.execute()

        assert data["last_sensors_record"] == SensorsRecord(
            soil_humidity=0,
            ambient_humidity=0,
            temperature=0,
            water_volume=0,
        )

    def it_should_get_empty_variations_if_there_is_no_record_in_repository_or_only_one_record(
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: GetLastSensorsRecordPageData,
    ):
        data = use_case.execute()

        assert data["variations"] == {
            "soil_humidity": 0,
            "ambient_humidity": 0,
            "water_volume": 0,
            "temperature": 0,
        }

        fake_record = SensorsRecordsFaker.fake()
        sensors_records_repository.create_sensors_record(fake_record)

        data = use_case.execute()

        assert data["variations"] == {
            "soil_humidity": 0,
            "ambient_humidity": 0,
            "water_volume": 0,
            "temperature": 0,
        }

    def it_should_get_variations_between_the_two_last_records(
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: GetLastSensorsRecordPageData,
    ):
        last_fake_record = SensorsRecordsFaker.fake(
            soil_humidity=25,
            ambient_humidity=50,
            temperature=100,
            water_volume=0,
        )
        penultimate_fake_record = SensorsRecordsFaker.fake(
            soil_humidity=50,
            ambient_humidity=25,
            temperature=100,
            water_volume=25,
        )

        sensors_records_repository.create_many_sensors_records(
            [last_fake_record, penultimate_fake_record]
        )

        data = use_case.execute()

        data["variations"] = {
            "soil_humidity": -50.0,
            "ambient_humidity": 100.0,
            "water_volume": 0.0,
            "temperature": 0.0,
        }
