from datetime import datetime

from core.entities import SensorsRecord, Plant
from core.commons import Error, Datetime
from core.constants import ADMIN_USER_EMAIL

from infra.repositories import sensors_records_repository, users_repository


class CreateSensorsRecordByApi:
    def execute(self, request: dict) -> None:
        try:
            if not request:
                raise Error("Nenhum dado recebido", 400)

            created_at = Datetime(datetime.now())

            active_plant_id = users_repository.get_user_active_plant_id(
                ADMIN_USER_EMAIL
            )

            if not active_plant_id:
                raise Error("Nenhuma planta cadastrada no sistema", 500)

            sensors_record = SensorsRecord(
                soil_humidity=request["soil_humidity"],
                ambient_humidity=request["ambient_humidity"],
                temperature=request["temperature"],
                water_volume=request["water_volume"],
                created_at=created_at,
                plant=Plant(id=active_plant_id),
            )

            sensors_records_repository.create_sensors_record(sensors_record)

        except Error as error:
            raise error
