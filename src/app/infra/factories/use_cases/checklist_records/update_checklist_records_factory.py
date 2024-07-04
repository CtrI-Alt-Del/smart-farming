from core.use_cases.checklist_records import UpdateChecklistRecord

from infra.repositories import plants_repository, checklist_records_repository


class UpdateChecklistRecordFactory:
    @staticmethod
    def produce():
        return UpdateChecklistRecord(
            plants_repository=plants_repository,
            checklist_records_repository=checklist_records_repository,
        )
