from infra.repositories import sensors_records_repository

from infra.database import mysql

class GetLastSensorsRecord:
    def execute(self):
            sql_data = """
            SELECT 
                soil_humidity, ambient_humidity, temperature, water_volume, created_at
            FROM sensors_records
            ORDER BY created_at DESC
            LIMIT 1;
        """
            try:
                row = mysql.query(sql=sql_data, is_single=True)

                if row:  
                    return sensors_records_repository._get_sensors_record(row)
                
                else:
                    return {
                        'soil_humidity': 0,
                        'ambient_humidity': 0,
                        'temperature': 0,
                        'water_volume': 0,
                        'created_at': None 
                    }

            except Exception as e:
                print(f"Error retrieving last sensor record: {e}")
                return []