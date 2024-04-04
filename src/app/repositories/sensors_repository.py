from database import mysql

class SensorRepository:

    def insert_sensor_data(self, soil_humidity, ambient_humidity, temperature, water_volume, created_at):
        insert_query = "INSERT INTO sensors (soil_humidity, ambient_humidity, temperature, water_volume, created_at)  VALUES (%s, %s, %s, %s, %s)"
        data = soil_humidity, ambient_humidity, temperature, water_volume, created_at
        mysql.mutate(sql=insert_query, parms=data)

    def get_sensor_data(self):
        select_query = "SELECT * FROM sensors"
        result = mysql.query(sql=select_query)
        return result
    
    