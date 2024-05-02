from datetime import datetime, date

from core.entities.sensors_record import SensorsRecord, Plant
from core.commons import Error, Datetime

from infra.repositories import sensors_records_repository


class CreateSensorsRecordByForm:
    def execute(self, request: dict) -> None:
        if not isinstance(request["date"], date):
            raise Error(ui_message="Data de registro não informado")

        try:
            created_at = Datetime(
                datetime(
                    hour=request["time"].hour,
                    minute=request["time"].minute,
                    year=request["date"].year,
                    month=request["date"].month,
                    day=request["date"].day,
                )
            )

            plant = Plant(id=request["plant_id"])

            sensors_records = SensorsRecord(
                soil_humidity=request["soil_humidity"],
                ambient_humidity=request["ambient_humidity"],
                temperature=request["temperature"],
                water_volume=request["water_volume"],
                created_at=created_at,
                plant=plant,
            )

            sensors_records_repository.create_sensors_record(sensors_records)

        except Error as error:
            raise error
