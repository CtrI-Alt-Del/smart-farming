from math import ceil

from core.entities import Plant, SensorsRecord
from core.constants import PAGINATION

from infra.repositories import plants_repository
from infra.repositories import sensors_records_repository


class GetSensorsRecordsTablePageData:
    def execute(
        self, page_number: int = 1, should_get_plants: bool = False
    ) -> tuple[list[SensorsRecord], int, list[Plant]]:

        plants = []
        if should_get_plants:
            plants = plants_repository.get_plants()

        sensors_records = sensors_records_repository.get_filtered_sensors_records(
            page_number=int(page_number)
        )

        sensors_records_count = sensors_records_repository.get_sensors_records_count()

        pages_count = ceil(sensors_records_count / PAGINATION["records_per_page"])

        return sensors_records, pages_count, plants
