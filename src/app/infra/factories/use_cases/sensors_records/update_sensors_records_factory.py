from core.use_cases.sensors_records import UpdateSensorsRecord

from infra.repositories import plants_repository, sensors_records_repository


class UpdateSensorsRecordFactory:
    @staticmethod
    def produce():
        return UpdateSensorsRecord(
            plants_repository=plants_repository,
            sensors_records_repository=sensors_records_repository,
        )
