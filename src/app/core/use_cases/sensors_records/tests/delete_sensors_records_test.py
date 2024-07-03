from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import SensorRecordsRepositoryMock
from core.errors.sensors_records import SensorsRecordNotFoundError
from core.errors.validation import SensorsRecordNotValidError
from core.entities.tests.fakers import SensorsRecordsFaker

from ..delete_sensors_records import DeleteSensorsRecord


def describe_delete_sensors_records_use_case():
    @fixture
    def sensors_records_repository():
        return SensorRecordsRepositoryMock()

    @fixture
    def use_case(
        sensors_records_repository: SensorRecordsRepositoryMock,
    ):
        sensors_records_repository.clear_records()
        return DeleteSensorsRecord(
            sensors_records_repository=sensors_records_repository,
        )

    def it_should_throw_error_if_at_least_one_sensors_record_id_is_not_valid(
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: DeleteSensorsRecord,
    ):
        fake_records = SensorsRecordsFaker.fake_many(3)
        sensors_records_repository.create_many_sensors_records(fake_records)

        ids = [fake_record.id for fake_record in fake_records]

        ids.append(42)

        with raises(SensorsRecordNotValidError):
            use_case.execute(ids)

    def it_should_throw_error_if_at_least_one_sensors_record_is_not_found(
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: DeleteSensorsRecord,
    ):
        fake_records = SensorsRecordsFaker.fake_many(3)
        sensors_records_repository.create_many_sensors_records(fake_records[:2])

        with raises(SensorsRecordNotFoundError):
            use_case.execute([fake_record.id for fake_record in fake_records])

    def it_should_delete_many_records(
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: DeleteSensorsRecord,
    ):
        count = 3
        fake_records = SensorsRecordsFaker.fake_many(count)

        sensors_records_repository.create_many_sensors_records(fake_records)

        use_case.execute([fake_record.id for fake_record in fake_records])

        records = sensors_records_repository.get_last_sensors_records(count=count)

        assert len(records) == 0
