from core.entities import Plant, CheckListRecord
from core.commons import Pagination, RecordsFilters, Error

from infra.repositories import plants_repository, checklist_records_repository


class GetChecklistRecordsTablePageData:
    def execute(
        self,
        start_date: str,
        end_date: str,
        plant_id: str,
        page_number: int = 1,
        should_get_plants: bool = False,
    ) -> tuple[list[CheckListRecord], int, list[Plant]]:
        try:
            plants = []
            if should_get_plants:
                plants = plants_repository.get_plants()

            filters = RecordsFilters(
                plant_id=plant_id, start_date=start_date, end_date=end_date
            )

            checklist_records_count = (
                checklist_records_repository.get_checklist_records_count(
                    plant_id=filters.plant_id,
                    start_date=filters.start_date,
                    end_date=filters.end_date,
                )
            )

            pagination = Pagination(page_number, checklist_records_count)

            current_page_number, last_page_number = (
                pagination.get_current_and_last_page_numbers()
            )

            checklist_records = (
                checklist_records_repository.get_filtered_checklist_records(
                    page_number=current_page_number,
                    plant_id=filters.plant_id,
                    start_date=filters.start_date,
                    end_date=filters.end_date,
                )
            )

            return {
                "checklist_records": checklist_records,
                "plants": plants,
                "last_page_number": last_page_number,
                "current_page_number": current_page_number,
            }

        except Error as error:
            raise error
