from datetime import datetime

from core.entities.sensors_record import SensorsRecord
from core.commons import Error, Datetime

from infra.repositories import sensors_records_repository, plants_repository


class CreateSensorsRecordByApi:
    def execute(self, request: dict) -> None:
        try:
            if not request:
                raise Error("Nenhum dado recebido", 400)

            created_at = Datetime(datetime.now())

            plant = plants_repository.get_last_plant()

            if not plant:
                raise Error("Nenhuma planta cadastrada no sistema", 500)

            sensors_record = SensorsRecord(
                soil_humidity=request["soil_humidity"],
                ambient_humidity=request["ambient_humidity"],
                temperature=request["temperature"],
                water_volume=request["water_volume"],
                created_at=created_at,
                plant=plant,
            )

            sensors_records_repository.create_sensors_record(sensors_record)

        except Error as error:
            raise error
