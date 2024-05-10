from core.entities.sensors_record import SensorsRecord

from core.commons import Error
from infra.repositories import sensors_records_repository


class GetLastSensorsRecordPageData:

    def execute(self):
        variations = {
            "soil_humidity": 0,
            "ambient_humidity": 0,
            "water_volume": 0,
            "temperature": 0,
        }

        try:
            last_sensors_records = sensors_records_repository.get_last_sensors_records(
                count=2
            )

            if not len(last_sensors_records) >= 2:
                return {
                    "last_sensors_record": (
                        last_sensors_records[0]
                        if len(last_sensors_records) == 1
                        else self.__get_empty_sensors_record()
                    ),
                    "variations": variations,
                }

            variations = {
                "soil_humidity": self.__get_variation(
                    last_sensors_records, "soil_humidity"
                ),
                "ambient_humidity": self.__get_variation(
                    last_sensors_records, "ambient_humidity"
                ),
                "water_volume": self.__get_variation(
                    last_sensors_records, "water_volume"
                ),
                "temperature": self.__get_variation(
                    last_sensors_records, "temperature"
                ),
            }

            return {
                "last_sensors_record": last_sensors_records[0],
                "variations": variations,
            }

        except Error:
            return {
                "last_sensors_record": self.__get_empty_sensors_record(),
                "variations": variations,
            }

    def __get_variation(
        self, last_sensors_records: list[SensorsRecord], attribute: str
    ):
        penultimate_record = last_sensors_records[1]
        last_sensors_record = last_sensors_records[0]

        last_record_atribute_value = getattr(last_sensors_record, attribute)
        penultimate_record_value = getattr(penultimate_record, attribute)

        if last_record_atribute_value == 0:
            return 0

        difference = last_record_atribute_value - penultimate_record_value

        return round(difference / penultimate_record_value * 100, 2)

    def __get_empty_sensors_record(self) -> SensorsRecord:
        return SensorsRecord(
            soil_humidity=0,
            ambient_humidity=0,
            temperature=0,
            water_volume=0,
        )
