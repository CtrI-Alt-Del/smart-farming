from core.entities.sensors_record import SensorsRecord

from core.commons.error import Error
from infra.repositories import sensors_records_repository


class GetLastSensorsRecord:
    def execute(self) -> SensorsRecord:
        try:
            last_sensors_record = sensors_records_repository.get_last_sensors_record()

            if not last_sensors_record:
                return self.__get_empty_sensors_record()

            return last_sensors_record

        except Error:
            return self.__get_empty_sensors_record()

    def __get_empty_sensors_record(self) -> SensorsRecord:
        return SensorsRecord(
            soil_humidity=0,
            ambient_humidity=0,
            temperature=0,
            water_volume=0,
        )
