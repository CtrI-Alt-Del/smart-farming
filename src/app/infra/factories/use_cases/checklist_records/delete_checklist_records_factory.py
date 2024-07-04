from core.use_cases.checklist_records import DeleteChecklistRecords

from infra.repositories import (
    checklist_records_repository,
)


class DeleteChecklistRecordsFactory:
    @staticmethod
    def produce():
        return DeleteChecklistRecords(
            checklist_records_repository=checklist_records_repository,
        )
