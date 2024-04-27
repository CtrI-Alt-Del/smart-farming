from typing import List, Dict

from core.entities.sensors_record import SensorsRecord

from infra.database import mysql

from core.constants import PAGINATION_LIMIT


class SensorRecordsRepository:
    def create_sensors_record(self, sensors_record: SensorsRecord) -> None:
        sql = """
        INSERT INTO sensors_records (soil_humidity, ambient_humidity, temperature, water_volume, created_at) 
        VALUES (%s, %s, %s, %s, %s)
        """
        mysql.mutate(
            sql=sql,
            params=[
                sensors_record.soil_humidity,
                sensors_record.ambient_humidity,
                sensors_record.temperature,
                sensors_record.water_volume,
                sensors_record.created_at.get_value(),
            ],
        )

    def get_sensor_records_grouped_by_date(self) -> List[SensorsRecord]:
        sql = """
        SELECT 
            DATE(created_at) AS date, 
            ROUND(AVG(soil_humidity), 1) AS soil_humidity,
            ROUND(AVG(ambient_humidity), 1) AS ambient_humidity,
            ROUND(AVG(temperature), 1) AS temperature,
            ROUND(AVG(water_volume), 1) AS water_volume
        FROM sensors_records
        GROUP BY DATE(created_at)
        ORDER BY DATE(created_at) ASC
        LIMIT 500;
        """
        rows = mysql.query(sql=sql, is_single=False)

        return rows

    def get_last_sensors_record(self) -> SensorsRecord:
        sql_data = """
            SELECT 
                soil_humidity, ambient_humidity, temperature, water_volume, created_at
            FROM sensors_records
            ORDER BY created_at DESC
            LIMIT 1;
        """

        row = mysql.query(sql=sql_data, is_single=True)

        if row:
            return self.__get_sensors_record_entity(row)

    def __get_sensors_record_entity(self, row: Dict) -> SensorsRecord:
        if row:
            return SensorsRecord(
                ambient_humidity=row["ambient_humidity"],
                soil_humidity=row["soil_humidity"],
                temperature=row["temperature"],
                water_volume=row["water_volume"],
                created_at=row["created_at"],
            )
        else:
            return None

    def get_filtered_sensors_records(self, page_number) -> list[SensorsRecord]:
        rows = mysql.query(
            sql=f"""
            SELECT *  FROM sensors_records
            ORDER BY created_at LIMIT {PAGINATION_LIMIT} OFFSET {page_number}            
            """,
            is_single=False,
        )
        sensors_records = []
        for row in rows:
            sensors_records.append(self.__get_sensors_record_entity(row))

        return sensors_records
