from typing import Tuple

from core.entities import Plant, CheckListRecord

from infra.repositories import plants_repository
from infra.repositories import checklist_records_repository


class GetChecklistRecordsTablePageData:
    def execute(self, page_number: int) -> Tuple[list[Plant], list[CheckListRecord]]:
        plants = plants_repository.get_plants()

        checklist_records = checklist_records_repository.get_filtered_checklist_records(
            page_number=page_number
        )

        return plants, checklist_records
