-- Active: 1712602370861@@localhost@3306@smart-farming

DROP TABLE IF EXISTS sensors_records;

CREATE TABLE sensors_records (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  soil_humidity INT NOT NULL,
  ambient_humidity INT NOT NULL,
  temperature DECIMAL(10, 2) NOT NULL,
  water_volume DECIMAL(10, 2) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM sensors_records ORDER BY created_at ASC;

SELECT 
  DATE(created_at) AS date, 
  ROUND(AVG(soil_humidity), 1) AS soil_humidity,
  ROUND(AVG(ambient_humidity), 1) AS ambient_humidity,
  ROUND(AVG(temperature), 1) AS temperature,
  ROUND(AVG(water_volume), 1) AS water_volume
FROM sensors_records
GROUP BY DATE(created_at)
ORDER BY DATE(created_at) ASC
LIMIT 7;
