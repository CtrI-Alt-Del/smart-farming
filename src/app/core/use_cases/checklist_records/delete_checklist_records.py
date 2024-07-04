from core.interfaces.repositories import ChecklistRecordsRepositoryInterface
from core.entities import CheckListRecord
from core.errors.validation import ChecklistRecordNotValidError
from core.errors.checklist_records import ChecklistRecordNotFoundError


class DeleteChecklistRecords:
    def __init__(
        self,
        checklist_records_repository: ChecklistRecordsRepositoryInterface,
    ):
        self._checklist_records_repository = checklist_records_repository

    def execute(self, checklist_records_ids: list[str]):
        for id in checklist_records_ids:
            if not isinstance(id, str):
                raise ChecklistRecordNotValidError()

            record = self._checklist_records_repository.get_checklist_record_by_id(id)

            if not isinstance(record, CheckListRecord):
                raise ChecklistRecordNotFoundError()

        self._checklist_records_repository.delete_many_checklist_records_by_id(
            checklist_records_ids
        )
