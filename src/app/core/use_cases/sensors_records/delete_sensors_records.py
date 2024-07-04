from core.interfaces.repositories import SensorRecordsRepositoryInterface
from core.errors.validation import SensorsRecordNotValidError
from core.errors.sensors_records import SensorsRecordNotFoundError
from core.entities import SensorsRecord


class DeleteSensorsRecord:
    def __init__(
        self,
        sensors_records_repository: SensorRecordsRepositoryInterface,
    ):
        self._sensors_records_repository = sensors_records_repository

    def execute(self, sensors_records_ids: list[str]) -> None:
        for id in sensors_records_ids:
            if not isinstance(id, str):
                raise SensorsRecordNotValidError()

            record = self._sensors_records_repository.get_sensors_record_by_id(id)

            if not isinstance(record, SensorsRecord):
                raise SensorsRecordNotFoundError()

        self._sensors_records_repository.delete_many_sensors_records_by_id(
            sensors_records_ids
        )
