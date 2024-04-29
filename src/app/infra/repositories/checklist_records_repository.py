from core.entities.checklist_record import CheckListRecord, Plant
from core.commons import Datetime, Date
from core.constants import PAGINATION_LIMIT

from infra.database import mysql


class CheckListRecordsRepository:
    def create_checklist_record(self, checklist_record: CheckListRecord) -> None:
        sql = """
        INSERT INTO checklist_records
        (
            soil_ph,
            soil_humidity,
            water_consumption,
            air_humidity,
            temperature,
            illuminance,
            lai,
            leaf_appearance,
            leaf_color,
            plantation_type,
            fertilizer_expiration_date,
            created_at,
            report,
            plant_id
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = [
            checklist_record.soil_ph,
            checklist_record.soil_humidity,
            checklist_record.water_consumption,
            checklist_record.air_humidity,
            checklist_record.temperature,
            checklist_record.illuminance,
            checklist_record.lai,
            checklist_record.leaf_appearance,
            checklist_record.leaf_color,
            checklist_record.plantation_type,
            checklist_record.fertilizer_expiration_date.get_value(),
            checklist_record.created_at.get_value(),
            checklist_record.report,
            checklist_record.plant.id,
        ]

        mysql.mutate(sql, params)

    def update_checklist_record_by_id(self, checklist_record: CheckListRecord) -> None:
        mysql.mutate(
            """
            UPDATE checklist_records 
            SET
                soil_ph = %s, 
                soil_humidity = %s,
                water_consumption = %s,
                air_humidity = %s,
                temperature = %s,
                illuminance = %s,
                lai = %s,
                leaf_appearance = %s,
                leaf_color = %s,
                plantation_type = %s,
                fertilizer_expiration_date = %s,
                created_at = %s,
                report = %s,
                plant_id = %s
            WHERE id = %s
            """,
            params=[
                checklist_record.soil_ph,
                checklist_record.soil_humidity,
                checklist_record.water_consumption,
                checklist_record.air_humidity,
                checklist_record.temperature,
                checklist_record.illuminance,
                checklist_record.lai,
                checklist_record.leaf_appearance,
                checklist_record.leaf_color,
                checklist_record.plantation_type,
                checklist_record.fertilizer_expiration_date.get_value(),
                checklist_record.created_at.get_value(),
                checklist_record.report,
                checklist_record.plant.id,
                checklist_record.id,
            ],
        )

    def delete_checklist_record_by_id(self, checklist_record_id: str):
        mysql.mutate(
            "DELETE FROM checklist_records WHERE id = %s",
            params=[
                checklist_record_id,
            ],
        )

    def get_checklist_record_by_id(self, id: str) -> CheckListRecord | None:
        print(id)
        row = mysql.query(
            sql="SELECT * FROM checklist_records WHERE id = %s",
            is_single=True,
            params=[id],
        )

        if row:
            return self.__get_checklist_record_entity(row)

        return None

    def get_filtered_checklist_records(self, page_number) -> list[CheckListRecord]:
        rows = mysql.query(
            sql=f"""
            SELECT *, P.id AS plant_id, P.name AS plant_name
            FROM checklist_records AS CR 
            JOIN plants AS P ON P.id = CR.plant_id
            ORDER BY created_at DESC
            LIMIT {PAGINATION_LIMIT} OFFSET {page_number};
            """,
            is_single=False,
        )

        checklist_records = []

        for row in rows:
            checklist_records.append(self.__get_checklist_record_entity(row))

        return checklist_records

    def __get_checklist_record_entity(self, row: dict):
        return CheckListRecord(
            id=row["id"],
            soil_ph=row["soil_ph"],
            soil_humidity=row["soil_humidity"],
            water_consumption=row["water_consumption"],
            air_humidity=row["air_humidity"],
            temperature=row["temperature"],
            illuminance=row["illuminance"],
            lai=row["lai"],
            leaf_appearance=row["leaf_appearance"],
            leaf_color=row["leaf_color"],
            plantation_type=row["plantation_type"],
            fertilizer_expiration_date=Date(row["fertilizer_expiration_date"]),
            created_at=Datetime(row["created_at"]),
            report=row["report"],
            plant=Plant(id=row["id"], name=row["name"]),
        )
