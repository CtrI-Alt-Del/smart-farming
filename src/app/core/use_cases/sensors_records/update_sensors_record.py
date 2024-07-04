from datetime import datetime, date

from core.entities import SensorsRecord
from core.commons import Datetime, Weekday
from core.errors.validation import SensorsRecordNotValidError, DatetimeNotValidError
from core.errors.sensors_records import SensorsRecordNotFoundError
from core.errors.plants import PlantNotFoundError
from core.interfaces.repositories import (
    SensorRecordsRepositoryInterface,
    PlantsRepositoryInterface,
)


class UpdateSensorsRecord:
    def __init__(
        self,
        sensors_records_repository: SensorRecordsRepositoryInterface,
        plants_repository: PlantsRepositoryInterface,
    ):
        self._sensors_records_repository = sensors_records_repository
        self._plants_repository = plants_repository

    def execute(self, request: dict) -> None:
        sensors_records_id = request["sensors_record_id"]

        if not sensors_records_id or not isinstance(sensors_records_id, str):
            raise SensorsRecordNotValidError()

        has_sensors_record = bool(
            self._sensors_records_repository.get_sensors_record_by_id(
                sensors_records_id
            )
        )

        if not has_sensors_record:
            raise SensorsRecordNotFoundError()

        if not isinstance(request["date"], date):
            raise DatetimeNotValidError()

        created_at = Datetime(
            datetime(
                hour=request["time"].hour,
                minute=request["time"].minute,
                year=request["date"].year,
                month=request["date"].month,
                day=request["date"].day,
            )
        )

        weekday = Weekday(created_at.get_value(is_datetime=True))

        plant = self._plants_repository.get_plant_by_id(request["plant_id"])

        if not plant:
            raise PlantNotFoundError()

        sensors_record = SensorsRecord(
            id=sensors_records_id,
            soil_humidity=request["soil_humidity"],
            ambient_humidity=request["ambient_humidity"],
            temperature=request["temperature"],
            water_volume=request["water_volume"],
            plant=plant,
            weekday=weekday,
            created_at=created_at,
        )

        self._sensors_records_repository.update_sensors_record_by_id(sensors_record)

        return sensors_record
