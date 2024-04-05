from database import mysql
from entities.checklist_record import CheckListRecord


class CheckListRecordsRepository:
    def create_checklist_record(self, checklist_record: CheckListRecord):
        sql = """
        INSERT INTO checklist_records
        (soil_ph, soil_humidity, water_consumption, air_humidity, temperature, illuminance, lai, leaf_apperance, leaf_color, plantation_type, fertiliziation_date, harvested_at, report)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
            checklist_record.fertiliziation_date,
            checklist_record.harvested_at,
            checklist_record.report,
        ]

        mysql.mutate(sql, params)

    def get_checklist_records(self):
        query = "SELECT * FROM checklist_record"
        result = mysql.query(sql=query)

        checklist_record = CheckListRecord(
            id=result["id"],
            soil_ph=["soil_ph"],
            soil_humidity=["soil_humidity"],
            water_consumption=["water_consumption"],
            air_humidity=["air_humidity"],
            temperature=["temperature"],
            illuminance=["illuminance"],
            lai=["lai"],
            leaf_apperance=["leaf_apperance"],
            leaf_color=["leaf_color"],
            plantation_type=["plantation_type"],
            fertiliziation_date=["fertiliziation_date"],
            harvested_at=["harvested_at"],
            report=["report"],
        )
        return checklist_record
