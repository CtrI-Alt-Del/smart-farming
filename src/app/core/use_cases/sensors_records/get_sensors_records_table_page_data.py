from core.commons import Pagination, Error, RecordsFilters
from core.interfaces.repositories import (
    PlantsRepositoryInterface,
    SensorRecordsRepositoryInterface,
)
from core.entities import SensorsRecord, Plant


class GetSensorsRecordsTablePageData:
    def __init__(
        self,
        plants_repository: PlantsRepositoryInterface,
        sensors_records_repository: SensorRecordsRepositoryInterface,
    ):
        self._plants_repository = plants_repository
        self._sensors_records_repository = sensors_records_repository

    def execute(
        self,
        start_date: str,
        end_date: str,
        plant_id: str,
        page_number: int = 1,
        should_get_plants: bool = False,
    ) -> tuple[list[SensorsRecord], int, list[Plant]]:
        try:
            plants = []
            if should_get_plants:
                plants = self._plants_repository.get_plants()

            filters = RecordsFilters(
                plant_id=plant_id, start_date=start_date, end_date=end_date
            )

            records_count = self._sensors_records_repository.get_sensors_records_count()

            pagination = Pagination(page_number, records_count)

            current_page_number, last_page_number = (
                pagination.get_current_and_last_page_numbers()
            )

            sensors_records = (
                self._sensors_records_repository.get_filtered_sensors_records(
                    page_number=current_page_number,
                    plant_id=filters.plant_id,
                    start_date=filters.start_date,
                    end_date=filters.end_date,
                )
            )

            return {
                "sensors_records": sensors_records,
                "plants": plants,
                "last_page_number": last_page_number,
                "current_page_number": current_page_number,
            }

        except Error as error:
            return error
