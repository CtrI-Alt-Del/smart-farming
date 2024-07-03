from datetime import datetime, date

from core.entities.sensors_record import SensorsRecord, Plant
from core.interfaces.repositories import (
    SensorRecordsRepositoryInterface,
    PlantsRepositoryInterface,
)
from core.errors.validation import DatetimeNotValidError, DateNotValidError
from core.errors.plants import PlantNotFoundError
from core.commons import Datetime


class CreateSensorsRecordByForm:
    def __init__(
        self,
        sensors_records_repository: SensorRecordsRepositoryInterface,
        plants_repository: PlantsRepositoryInterface,
    ):
        self._sensors_records_repository = sensors_records_repository
        self._plants_repository = plants_repository

    def execute(self, request: dict):
        if "time" not in request or not isinstance(request["time"], datetime):
            raise DatetimeNotValidError()

        if "date" not in request or not isinstance(request["date"], date):
            raise DateNotValidError()

        created_at = Datetime(
            datetime(
                hour=request["time"].hour,
                minute=request["time"].minute,
                year=request["date"].year,
                month=request["date"].month,
                day=request["date"].day,
            )
        )

        plant = self._plants_repository.get_plant_by_id(request["plant_id"])

        if not isinstance(plant, Plant):
            raise PlantNotFoundError()

        sensors_records = SensorsRecord(
            soil_humidity=request["soil_humidity"],
            ambient_humidity=request["ambient_humidity"],
            temperature=request["temperature"],
            water_volume=request["water_volume"],
            created_at=created_at,
            plant=plant,
        )

        self._sensors_records_repository.create_sensors_record(sensors_records)
