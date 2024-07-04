from datetime import datetime

from core.entities import SensorsRecord, Plant
from core.commons import Datetime
from core.interfaces.repositories import (
    PlantsRepositoryInterface,
    UsersRepositoryInterface,
    SensorRecordsRepositoryInterface,
)
from core.errors.validation import SensorsRecordNotValidError
from core.errors.plants import PlantNotFoundError
from core.constants import ADMIN_USER_EMAIL


class CreateSensorsRecordByApi:
    def __init__(
        self,
        plants_repository: PlantsRepositoryInterface,
        users_repository: UsersRepositoryInterface,
        sensors_records_repository: SensorRecordsRepositoryInterface,
    ):
        self._plants_repository = plants_repository
        self._users_repository = users_repository
        self._sensors_records_repository = sensors_records_repository

    def execute(self, request: dict) -> None:
        if not request:
            raise SensorsRecordNotValidError()

        created_at = Datetime(datetime.now())

        active_plant_id = self._users_repository.get_user_active_plant_id(
            ADMIN_USER_EMAIL
        )

        if not active_plant_id:
            raise PlantNotFoundError()

        sensors_record = SensorsRecord(
            soil_humidity=request["soil_humidity"],
            ambient_humidity=request["ambient_humidity"],
            temperature=request["temperature"],
            water_volume=request["water_volume"],
            created_at=created_at,
            plant=Plant(id=active_plant_id),
        )

        self._sensors_records_repository.create_sensors_record(sensors_record)
