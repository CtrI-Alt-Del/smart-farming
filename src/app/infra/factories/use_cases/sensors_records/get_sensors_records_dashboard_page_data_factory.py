from core.use_cases.sensors_records import GetSensorsRecordsDashboardPageData

from infra.repositories import (
    plants_repository,
    users_repository,
    sensors_records_repository,
)


class GetSensorsRecordsDashboardPageDataFactory:
    @staticmethod
    def produce():
        return GetSensorsRecordsDashboardPageData(
            plants_repository=plants_repository,
            users_repository=users_repository,
            sensors_records_repository=sensors_records_repository,
        )
