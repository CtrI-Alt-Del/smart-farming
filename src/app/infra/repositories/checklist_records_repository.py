from core.entities.checklist_record import CheckListRecord, Plant
from core.commons import Datetime, Date
from core.constants import PAGINATION

from infra.database import mysql


class ChecklistRecordsRepository:
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
            checklist_record.report if checklist_record.report else "Não",
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
                (
                    checklist_record.leaf_color
                    if checklist_record.leaf_color
                    else "NÃO REGISTRADO"
                ),
                checklist_record.plantation_type,
                checklist_record.fertilizer_expiration_date.get_value(),
                checklist_record.created_at.get_value(),
                checklist_record.report if checklist_record.report else "Não",
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

    def get_filtered_checklist_records(self, page_number: int) -> list[CheckListRecord]:
        pagination_limit = PAGINATION["records_per_page"]
        offset = (page_number - 1) * pagination_limit

        rows = mysql.query(
            sql=f"""
            SELECT CR.*, P.id AS plant_id, P.name AS plant_name, P.hex_color AS plant_color
            FROM checklist_records AS CR 
            JOIN plants AS P ON P.id = CR.plant_id
            ORDER BY created_at DESC
            LIMIT {pagination_limit} OFFSET {offset};
            """,
            is_single=False,
        )

        checklist_records = []

        for row in rows:
            checklist_records.append(self.__get_checklist_record_entity(row))

        return checklist_records

    def get_leaf_appearances_and_leaf_colors_records(self):
        rows = mysql.query(
            sql="""
            SELECT leaf_appearance, leaf_color, created_at, plant_id
            FROM checklist_records
            ORDER BY created_at ASC
            """,
            is_single=False,
        )

        if len(rows) == 0:
            return []

        for row in rows:
            row["date"] = row["created_at"].date()
            del row["created_at"]

        return rows

    def get_lai_records(self):
        rows = mysql.query(
            sql="""
            SELECT 
                DATE(created_at) AS date,
                ROUND(AVG(lai), 1) AS lai,
                plant_id
            FROM checklist_records
            GROUP BY DATE(created_at), plant_id
            ORDER BY date ASC;
            """,
            is_single=False,
        )

        if len(rows) == 0:
            return []

        return rows

    def get_checklist_records_count(self) -> int:
        result = mysql.query(
            sql="SELECT COUNT(id) AS count FROM checklist_records",
            is_single=True,
        )

        return result["count"]

    def get_ordered_by_date_leaf_appearance_and_leaf_color_records(self):
        rows = mysql.query(
            sql="SELECT leaf_appearance, leaf_color, created_at FROM checklist_records",
            is_single=False,
        )

        if len(rows) == 0:
            return []

        for row in rows:
            row["date"] = row["created_at"].date()
            del row["created_at"]

        return rows

    def get_checklist_record_by_id(self, id: str) -> CheckListRecord | None:
        row = mysql.query(
            sql="""
            SELECT CR.*, P.id AS plant_id, P.name AS plant_name, P.hex_color AS plant_color
            FROM checklist_records AS CR 
            JOIN plants AS P ON P.id = CR.plant_id
            WHERE CR.id = %s
            """,
            is_single=True,
            params=[id],
        )

        if not row:
            return None

        return self.__get_checklist_record_entity(row)

    def __get_checklist_record_entity(self, row: dict):
        return CheckListRecord(
            id=row["id"],
            soil_ph=int(row["soil_ph"]),
            soil_humidity=int(row["soil_humidity"]),
            air_humidity=int(row["air_humidity"]),
            lai=float(row["lai"]),
            water_consumption=float(row["water_consumption"]),
            temperature=float(row["temperature"]),
            illuminance=float(row["illuminance"]),
            leaf_appearance=row["leaf_appearance"],
            leaf_color=row["leaf_color"],
            plantation_type=row["plantation_type"],
            fertilizer_expiration_date=Date(row["fertilizer_expiration_date"]),
            created_at=Datetime(row["created_at"]),
            report=row["report"],
            plant=Plant(
                id=row["plant_id"], name=row["plant_name"], hex_color=row["plant_color"]
            ),
        )
