from core.use_cases.checklist_records import CreateChecklistRecordByForm

from infra.repositories import checklist_records_repository


class CreateChecklistRecordByFormFactory:
    @staticmethod
    def produce():
        return CreateChecklistRecordByForm(checklist_records_repository)
