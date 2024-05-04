from datetime import datetime, date

from core.entities import SensorsRecord
from core.commons import Error, Datetime

from infra.repositories import sensors_records_repository, plants_repository


class UpdateSensorsRecord:
    def execute(self, request: dict) -> None:
        try:
            sensors_records_id = request["sensors_record_id"]

            if not sensors_records_id or not isinstance(sensors_records_id, str):
                raise Error(
                    ui_message="Registro dos sensores não encontrado",
                    internal_message="Sensors record in not found",
                )
            has_sensors_record = bool(
                sensors_records_repository.get_sensors_record_by_id(sensors_records_id)
            )

            if not has_sensors_record:
                raise Error(
                    ui_message="Registro dos sensores não encontrado",
                    internal_message="Sensors record id not found",
                )
            if not isinstance(request["date"], date):
                raise Error(ui_message="Data de registro não informado")

            created_at = Datetime(
                datetime(
                    hour=request["time"].hour,
                    minute=request["time"].minute,
                    year=request["date"].year,
                    month=request["date"].month,
                    day=request["date"].day,
                )
            )

            plant = plants_repository.get_plant_by_id(request["plant_id"])

            if not plant:
                raise Error(ui_message="Planta não encontrada para esse registro")

            sensors_record = SensorsRecord(
                id=sensors_records_id,
                soil_humidity=request["soil_humidity"],
                ambient_humidity=request["ambient_humidity"],
                temperature=request["temperature"],
                water_volume=request["water_volume"],
                plant=plant,
                created_at=created_at,
            )

            sensors_records_repository.update_sensors_record_by_id(sensors_record)

            return sensors_record

        except Error as error:
            raise error
