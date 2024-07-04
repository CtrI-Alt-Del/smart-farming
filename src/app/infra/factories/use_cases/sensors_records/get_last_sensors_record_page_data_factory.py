from core.use_cases.sensors_records import GetLastSensorsRecordPageData

from infra.repositories import sensors_records_repository


class GetLastSensorsRecordPageDataFactory:
    @staticmethod
    def produce():
        return GetLastSensorsRecordPageData(
            sensors_records_repository=sensors_records_repository,
        )
