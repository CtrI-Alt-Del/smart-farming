from core.entities.sensors_record import SensorsRecord

from infra.database import mysql


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
                sensors_record.created_at,
            ],
        )

    def get_sensor_records(self) -> None:
        select_query = "SELECT * FROM sensors_records"
        result = mysql.query(sql=select_query)
        return result
