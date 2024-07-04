from core.use_cases.sensors_records import DeleteSensorsRecord

from infra.repositories import (
    sensors_records_repository,
)


class DeleteSensorsRecordFactory:
    @staticmethod
    def produce():
        return DeleteSensorsRecord(
            sensors_records_repository=sensors_records_repository,
        )
