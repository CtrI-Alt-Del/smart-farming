from datetime import datetime, date

from core.entities import CheckListRecord
from core.commons import Date, Datetime
from core.errors.validation import ChecklistRecordNotValidError, DateNotValidError
from core.errors.checklist_records import ChecklistRecordNotFoundError
from core.errors.plants import PlantNotFoundError
from core.interfaces.repositories import (
    SensorRecordsRepositoryInterface,
    PlantsRepositoryInterface,
)


class UpdateChecklistRecord:
    def __init__(
        self,
        checklist_records_repository: SensorRecordsRepositoryInterface,
        plants_repository: PlantsRepositoryInterface,
    ):
        self._checklist_records_repository = checklist_records_repository
        self._plants_repository = plants_repository

    def execute(self, request: dict) -> None:
        checklist_record_id = request["checklist_record_id"]

        if not checklist_record_id or not isinstance(checklist_record_id, str):
            raise ChecklistRecordNotValidError()

        has_checklist_record = bool(
            self._checklist_records_repository.get_checklist_record_by_id(
                checklist_record_id
            )
        )

        if not has_checklist_record:
            raise ChecklistRecordNotFoundError()

        if not isinstance(request["date"], date):
            raise DateNotValidError()

        created_at = Datetime(
            datetime(
                hour=request["hour"],
                year=request["date"].year,
                month=request["date"].month,
                day=request["date"].day,
            )
        )

        fertilizer_expiration_date = Date(request["fertilizer_expiration_date"])

        plant = self._plants_repository.get_plant_by_id(request["plant_id"])

        if not plant:
            raise PlantNotFoundError()

        checklist_record = CheckListRecord(
            id=checklist_record_id,
            plantation_type=request["plantation_type"],
            illuminance=request["illuminance"],
            lai=request["lai"],
            soil_humidity=request["soil_humidity"],
            temperature=request["temperature"],
            water_consumption=request["water_consumption"],
            soil_ph=request["soil_ph"],
            report=request["report"],
            air_humidity=request["air_humidity"],
            leaf_color=request["leaf_color"],
            leaf_appearance=request["leaf_appearance"],
            fertilizer_expiration_date=fertilizer_expiration_date,
            created_at=created_at,
            plant=plant,
        )

        self._checklist_records_repository.update_checklist_record_by_id(
            checklist_record
        )

        return checklist_record
