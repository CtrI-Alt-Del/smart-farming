from core.use_cases.checklist_records import GetChecklistRecordsTablePageData

from infra.repositories import (
    plants_repository,
    checklist_records_repository,
)


class GetChecklistRecordsTablePageDataFactory:
    @staticmethod
    def produce():
        return GetChecklistRecordsTablePageData(
            plants_repository=plants_repository,
            checklist_records_repository=checklist_records_repository,
        )
