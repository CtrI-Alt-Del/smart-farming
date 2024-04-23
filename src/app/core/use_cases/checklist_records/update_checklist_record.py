from core.entities.checklist_record import CheckListRecord
from core.entities.plant import Plant
from core.commons.error import Error

from infra.repositories import checklist_records_repository


class UpdateChecklistRecord:
    def execute(self, request: dict) -> None:
        try:
            checklist_record_id = request["checklist_record_id"]

            if not checklist_record_id or not isinstance(checklist_record_id, str):
                raise Error(
                    ui_message="Registro check-list não encontrado",
                    internal_message="Checklist record id not found",
                    status_code=401,
                )

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
                leaf_apperance=request["leaf_apperance"],
                plant=Plant(id=request["plant_id"]),
            )

            checklist_records_repository.create_checklist_record(checklist_record)

        except Error as error:
            raise error
