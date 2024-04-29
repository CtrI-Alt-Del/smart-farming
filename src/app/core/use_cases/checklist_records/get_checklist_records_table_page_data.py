from core.entities import Plant, CheckListRecord

from infra.repositories import plants_repository
from infra.repositories import checklist_records_repository


class GetChecklistRecordsTablePageData:
    def execute(
        self, page_number: int = 1, should_get_plants: bool = False
    ) -> tuple[list[CheckListRecord], list[Plant]]:
        plants = []
        if should_get_plants:
            plants = plants_repository.get_plants()

        checklist_records = checklist_records_repository.get_filtered_checklist_records(
            page_number=page_number
        )

        return checklist_records, plants
