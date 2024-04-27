from typing import Tuple

from core.entities import Plant, SensorsRecord

from infra.repositories import plants_repository

from infra.repositories import sensors_records_repository

class GetSensorsRecordsTablePageData:
    def execute(self,page_number: int) -> Tuple[list[Plant] , list[SensorsRecord]]:
        plants = plants_repository.get_plants()
        
        sensors_records = sensors_records_repository.get_filtered_sensors_records(
            page_number=page_number
        )
        return plants,sensors_records