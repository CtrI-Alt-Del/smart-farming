from math import ceil

from core.constants import PAGINATION

from infra.repositories import plants_repository
from infra.repositories import sensors_records_repository


class GetSensorsRecordsTablePageData:
    def execute(self, page_number: int = 1, should_get_plants: bool = False) -> dict:

        plants = []
        if should_get_plants:
            plants = plants_repository.get_plants()

        sensors_records = sensors_records_repository.get_filtered_sensors_records(
            page_number=page_number
        )

        sensors_records_count = sensors_records_repository.get_sensors_records_count()

        last_page_number = ceil(sensors_records_count / PAGINATION["records_per_page"])

        return {
            "sensors_records": sensors_records,
            "last_page_number": last_page_number,
            "plants": plants,
        }
