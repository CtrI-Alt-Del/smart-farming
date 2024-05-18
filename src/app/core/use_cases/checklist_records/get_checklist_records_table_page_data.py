from datetime import date

from core.entities import Plant, CheckListRecord
from core.commons import Pagination, Date, Error

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

            filters = self.__handle_filters(
                plant_id=plant_id, start_date=start_date, end_date=end_date
            )

            checklist_records_count = (
                checklist_records_repository.get_checklist_records_count()
            )

            pagination = Pagination(page_number, checklist_records_count)

            current_page_number, last_page_number = (
                pagination.get_current_and_last_page_numbers()
            )

            checklist_records = (
                checklist_records_repository.get_filtered_checklist_records(
                    page_number=current_page_number,
                    plant_id=filters["plant_id"],
                    start_date=filters["start_date"],
                    end_date=filters["end_date"],
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

    def __handle_filters(
        self,
        start_date: str,
        end_date: str,
        plant_id: str,
    ):
        if plant_id == "all":
            plant_id = None

        if start_date != "" and isinstance(start_date, str):
            start_date = Date(start_date).get_value()

        if end_date != "" and isinstance(end_date, str):
            end_date = Date(end_date).get_value()

        has_filters = plant_id is not None or (
            isinstance(start_date, date) and isinstance(end_date, date)
        )

        return {
            "plant_id": plant_id,
            "start_date": start_date,
            "end_date": end_date,
        }
