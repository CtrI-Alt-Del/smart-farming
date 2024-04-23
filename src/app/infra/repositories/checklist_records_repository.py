from core.entities.checklist_record import CheckListRecord
from typing import List
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
            leaf_apperance,
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
            checklist_record.leaf_apperance,
            checklist_record.leaf_color,
            checklist_record.plantation_type,
            checklist_record.fertilizer_expiration_date.get_value(),
            checklist_record.created_at.get_value(),
            checklist_record.report,
            checklist_record.plant.id,
        ]

        print("EITA")
        mysql.mutate(sql, params)

    def update_checklist_record_by_id(self, checklist_record: CheckListRecord) -> None:
        mysql.query(
            """
            UPDATE checklist_records
                soil_ph = %s, 
                soil_humidity = %s,
                water_consumption = %s,
                air_humidity = %s,
                temperature = %s,
                illuminance = %s,
                lai = %s,
                leaf_apperance = %s,
                leaf_color = %s,
                plantation_type = %s,
                fertiliziation_date = %s,
                harvested_at = %s,
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
                checklist_record.leaf_apperance,
                checklist_record.leaf_color,
                checklist_record.plantation_type,
                checklist_record.fertiliziation_date,
                checklist_record.harvested_at,
                checklist_record.report,
                checklist_record.plant.id,
                checklist_record.id,
            ],
        )

    def delete_checklist_record_by_id(self, checklist_record_id):
        mysql.query(
            "DELETE FROM checklist_records WHERE id = %s",
            params=[
                checklist_record_id,
            ],
        )

    def get_checklist_records(self) -> List[CheckListRecord]:
        select_query = "SELECT * FROM checklist_records"
        rows = mysql.query(sql=select_query, is_single=False)
        checklist_records = []

        for row in rows:
            checklist_records.append(
                CheckListRecord(
                    id=row["id"],
                    soil_ph=row["soil_ph"],
                    soil_humidity=row["soil_humidity"],
                    water_consumption=row["water_consumption"],
                    air_humidity=row["air_humidity"],
                    temperature=row["temperature"],
                    illuminance=row["illuminance"],
                    lai=row["lai"],
                    leaf_apperance=row["leaf_apperance"],
                    leaf_color=row["leaf_color"],
                    plantation_type=row["plantation_type"],
                    fertiliziation_date=row["fertiliziation_date"],
                    harvested_at=row["harvested_at"],
                    report=row["report"],
                )
            )
        return checklist_records
