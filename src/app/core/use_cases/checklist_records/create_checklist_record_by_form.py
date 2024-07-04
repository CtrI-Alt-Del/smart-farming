from datetime import datetime, date

from core.entities.checklist_record import CheckListRecord, Plant
from core.commons import Date, Datetime
from core.errors.validation import DateNotValidError
from core.errors.plants import PlantNotFoundError
from core.interfaces.repositories import (
    ChecklistRecordsRepositoryInterface,
    PlantsRepositoryInterface,
)


class CreateChecklistRecordByForm:
    def __init__(
        self,
        checklist_records_repository: ChecklistRecordsRepositoryInterface,
        plants_repository: PlantsRepositoryInterface,
    ):
        self._checklist_records_repository = checklist_records_repository
        self._plants_repository = plants_repository

    def execute(self, request: dict) -> None:
        if not isinstance(request["date"], date):
            raise DateNotValidError(ui_message="Data de inserção não válido")

        if not isinstance(request["fertilizer_expiration_date"], date):
            raise DateNotValidError(ui_message="Data de validade de adubo não válido")

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

        if not isinstance(plant, Plant):
            raise PlantNotFoundError()

        checklist_record = CheckListRecord(
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

        self._checklist_records_repository.create_checklist_record(checklist_record)
