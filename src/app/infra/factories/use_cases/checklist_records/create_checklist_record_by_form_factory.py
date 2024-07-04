from core.use_cases.checklist_records import CreateChecklistRecordByForm

from infra.repositories import checklist_records_repository, plants_repository


class CreateChecklistRecordByFormFactory:
    @staticmethod
    def produce():
        return CreateChecklistRecordByForm(
            checklist_records_repository=checklist_records_repository,
            plants_repository=plants_repository,
        )
