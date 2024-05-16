from datetime import date

from core.entities import Plant, CheckListRecord
from core.commons import Pagination

from infra.repositories import plants_repository, checklist_records_repository


class GetChecklistRecordsTablePageData:
    def execute(
        self,
        start_date: date,
        end_date: date,
        plant_id: str,
        page_number: int = 1,
        should_get_plants: bool = False,
    ) -> tuple[list[CheckListRecord], int, list[Plant]]:
        plants = []
        if should_get_plants:
            plants = plants_repository.get_plants()

        if plant_id == "all":
            plant_id = None

        checklist_records_count = (
            checklist_records_repository.get_checklist_records_count()
        )

        pagination = Pagination(page_number, checklist_records_count)

        current_page_number, last_page_number = (
            pagination.get_current_and_last_page_numbers()
        )

        checklist_records = checklist_records_repository.get_filtered_checklist_records(
            page_number=current_page_number,
            plant_id=plant_id,
            start_date=start_date,
            end_date=end_date,
        )

        return {
            "checklist_records": checklist_records,
            "plants": plants,
            "last_page_number": last_page_number,
            "current_page_number": current_page_number,
        }
