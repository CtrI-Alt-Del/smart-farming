from math import ceil

from core.constants import PAGINATION

from infra.repositories import plants_repository, sensors_records_repository


class GetSensorsRecordsTablePageData:
    def execute(self, page_number: int = 1, should_get_plants: bool = False) -> dict:
        plants = []
        if should_get_plants:
            plants = plants_repository.get_plants()

        sensors_count = sensors_records_repository.get_sensors_records_count()

        last_page_number = ceil(sensors_count / PAGINATION["records_per_page"])

        if last_page_number > 0 and page_number > last_page_number:
            current_page_number = last_page_number
        else:
            current_page_number = page_number

        sensors_records = sensors_records_repository.get_filtered_sensors_records(
            page_number=current_page_number
        )

        return {
            "sensors_records": sensors_records,
            "plants": plants,
            "last_page_number": last_page_number,
            "current_page_number": current_page_number,
        }
