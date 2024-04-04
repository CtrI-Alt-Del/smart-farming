from database.mysql import mysql
from entities.checklist import CheckList


class CheckListRepository:
    def create_checklist(
        self,
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
        fertiliziation_date=None,
        harvested_at=None,
        report=None,
    ):
        sql_checklist = """INSERT INTO checklist 
        (soil_ph, soil_humidity, water_consumption, air_humidity, temperature, illuminance, lai, leaf_apperance, leaf_color, plantation_type, fertiliziation_date, harvested_at, report)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        params_checklist = (
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
            fertiliziation_date,
            harvested_at,
            report,
        )
        mysql.mutate(sql=sql_checklist, params=params_checklist)

    def get_checklist_by_id(self, id):
        query = "SELECT * FROM checklist"
        result = mysql.query(sql=query)

        checklist = CheckList(
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
        return checklist
        
        
