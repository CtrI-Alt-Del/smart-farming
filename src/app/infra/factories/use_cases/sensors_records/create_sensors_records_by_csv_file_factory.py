from core.use_cases.sensors_records import CreateSensorsRecordsByCsvFile

from infra.repositories import (
    plants_repository,
    sensors_records_repository,
)


class CreateSensorsRecordsByCsvFileFactory:
    @staticmethod
    def produce():
        return CreateSensorsRecordsByCsvFile(
            plants_repository=plants_repository,
            sensors_records_repository=sensors_records_repository,
        )
