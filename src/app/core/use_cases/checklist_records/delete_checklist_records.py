from core.commons.error import Error

from infra.repositories import checklist_records_repository


class DeleteChecklistRecords:
    def execute(self, checklist_records_ids: list[str]) -> None:
        try:
            for id in checklist_records_ids:
                if id and isinstance(id, str):
                    checklist_records_repository.delete_checklist_record_by_id(id)

        except Error as error:
            raise error
