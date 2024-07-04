from core.use_cases.checklist_records import CreateChecklistRecordsByCsvFile

from infra.repositories import (
    plants_repository,
    sensors_records_repository,
)


class CreateChecklistRecordsByCsvFileFactory:
    @staticmethod
    def produce():
        return CreateChecklistRecordsByCsvFile(
            plants_repository=plants_repository,
            sensors_records_repository=sensors_records_repository,
        )
