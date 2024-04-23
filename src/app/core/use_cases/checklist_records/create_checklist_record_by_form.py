from datetime import datetime, date

from core.entities.checklist_record import CheckListRecord
from core.entities.plant import Plant
from core.commons.datetime import Datetime
from core.commons.date import Date
from core.commons.error import Error

from infra.repositories import checklist_records_repository


class CreateChecklistRecordByForm:
    def execute(self, request: dict) -> None:
        if not isinstance(request["date"], date):
            raise Error(ui_message="Data de registro não informado")

        try:
            created_at = Datetime(
                datetime(
                    hour=int(request["hour"]),
                    year=request["date"].year,
                    month=request["date"].month,
                    day=request["date"].day,
                )
            )

            fertilizer_expiration_date = Date(request["fertilizer_expiration_date"])

            plant = Plant(id=request["plant_id"])

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
                leaf_apperance=request["leaf_apperance"],
                fertilizer_expiration_date=fertilizer_expiration_date,
                created_at=created_at,
                plant=plant,
            )

            print(checklist_record.fertilizer_expiration_date.get_value())
            checklist_records_repository.create_checklist_record(checklist_record)

        except Error as error:
            raise error
