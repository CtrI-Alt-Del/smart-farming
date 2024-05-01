from datetime import datetime, date

from core.entities import CheckListRecord
from core.commons import Error, Date, Datetime

from infra.repositories import checklist_records_repository, plants_repository


class UpdateChecklistRecord:
    def execute(self, request: dict) -> None:
        try:
            checklist_record_id = request["checklist_record_id"]

            if not checklist_record_id or not isinstance(checklist_record_id, str):
                raise Error(
                    ui_message="Registro check-list não encontrado",
                    internal_message="Checklist record id not found",
                )

            has_checklist_record = bool(
                checklist_records_repository.get_checklist_record_by_id(
                    checklist_record_id
                )
            )

            if not has_checklist_record:
                raise Error(
                    ui_message="Registro check-list não encontrado",
                    internal_message="Checklist record id not found",
                )

            if not isinstance(request["date"], date):
                raise Error(ui_message="Data de registro não informado")

            created_at = Datetime(
                datetime(
                    hour=int(request["hour"]),
                    year=request["date"].year,
                    month=request["date"].month,
                    day=request["date"].day,
                )
            )

            fertilizer_expiration_date = Date(request["fertilizer_expiration_date"])

            plant = plants_repository.get_plant_by_id(request["plant_id"])

            if not plant:
                raise Error(ui_message="Planta não encontrada para esse registro")

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

            checklist_records_repository.update_checklist_record_by_id(checklist_record)

            return checklist_record

        except Error as error:
            raise error
