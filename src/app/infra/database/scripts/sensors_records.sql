-- Active: 1712258180714@@127.0.0.1@3306@smart-farming
-- Active: 1712258180714@@127.0.0.1@3306@smart-farming

DROP TABLE IF EXISTS sensors_records;

CREATE TABLE IF NOT EXISTS sensors_records (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  soil_humidity INT NOT NULL,
  ambient_humidity INT NOT NULL,
  temperature DECIMAL(10, 2) NOT NULL,
  water_volume DECIMAL(10, 2) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  plant_id CHAR(36) DEFAULT '4544afe3-0661-11ef-9512-0242ac140002',
  FOREIGN KEY (plant_id) REFERENCES plants(id)
);

DESC sensors_records;

SELECT * FROM sensors_records ORDER BY created_at ASC
LIMIT 30000;

SELECT 
  DATE(created_at) AS date, 
  ROUND(AVG(soil_humidity), 1) AS soil_humidity,
  ROUND(AVG(ambient_humidity), 1) AS ambient_humidity,
  ROUND(AVG(temperature), 1) AS temperature,
  ROUND(AVG(water_volume), 1) AS water_volume
FROM sensors_records
GROUP BY DATE(created_at)
ORDER BY DATE(created_at) ASC
LIMIT 20000;

SELECT * FROM sensors_records LIMIT 20000;
SELECT COUNT(*) AS count FROM sensors_records;

 SELECT SR.*, P.id AS plant_id, P.name AS plant_name, P.hex_color as plant_color
            FROM sensors_records AS SR
            JOIN plants AS P ON P.id = SR.plant_id
            ORDER BY created_at DESC
            LIMIT 2000;
DELETE FROM sensors_records;
