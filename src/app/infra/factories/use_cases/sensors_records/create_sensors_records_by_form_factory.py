from core.use_cases.sensors_records import CreateSensorsRecordByForm

from infra.repositories import (
    plants_repository,
    sensors_records_repository,
)


class CreateSensorsRecordByFormFactory:
    @staticmethod
    def produce():
        return CreateSensorsRecordByForm(
            plants_repository=plants_repository,
            sensors_records_repository=sensors_records_repository,
        )
