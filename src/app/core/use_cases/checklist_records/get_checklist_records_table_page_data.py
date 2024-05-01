from math import ceil

from core.entities import Plant, CheckListRecord
from core.constants import PAGINATION

from infra.repositories import plants_repository, checklist_records_repository


class GetChecklistRecordsTablePageData:
    def execute(
        self, page_number: int = 1, should_get_plants: bool = False
    ) -> tuple[list[CheckListRecord], int, list[Plant]]:
        plants = []
        if should_get_plants:
            plants = plants_repository.get_plants()

        checklist_count = checklist_records_repository.get_checklist_records_count()

        last_page_number = ceil(checklist_count / PAGINATION["records_per_page"])

        if page_number > last_page_number:
            current_page_number = last_page_number
        else:
            current_page_number = page_number

        checklist_records = checklist_records_repository.get_filtered_checklist_records(
            page_number=current_page_number
        )

        return {
            "checklist_records": checklist_records,
            "plants": plants,
            "last_page_number": last_page_number,
            "current_page_number": current_page_number,
        }
