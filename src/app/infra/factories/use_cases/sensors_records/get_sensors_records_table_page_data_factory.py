from core.use_cases.sensors_records import GetSensorsRecordsTablePageData

from infra.repositories import (
    plants_repository,
    sensors_records_repository,
)


class GetSensorsRecordsTablePageDataFactory:
    @staticmethod
    def produce():
        return GetSensorsRecordsTablePageData(
            plants_repository=plants_repository,
            sensors_records_repository=sensors_records_repository,
        )
