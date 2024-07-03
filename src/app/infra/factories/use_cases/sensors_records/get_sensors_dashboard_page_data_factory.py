from core.use_cases.sensors_records import GetSensorDashboardPageData

from infra.repositories import (
    plants_repository,
    users_repository,
    sensors_records_repository,
)


class GetSensorDashboardPageDataFactory:
    @staticmethod
    def produce():
        return GetSensorDashboardPageData(
            plants_repository=plants_repository,
            users_repository=users_repository,
            sensors_records_repository=sensors_records_repository,
        )
