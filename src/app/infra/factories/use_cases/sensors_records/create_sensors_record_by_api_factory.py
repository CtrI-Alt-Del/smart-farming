from core.use_cases.sensors_records import CreateSensorsRecordByApi

from infra.repositories import (
    plants_repository,
    users_repository,
    sensors_records_repository,
)


class CreateSensorsRecordByApiFactory:
    @staticmethod
    def produce():
        return CreateSensorsRecordByApi(
            plants_repository=plants_repository,
            users_repository=users_repository,
            sensors_records_repository=sensors_records_repository,
        )
