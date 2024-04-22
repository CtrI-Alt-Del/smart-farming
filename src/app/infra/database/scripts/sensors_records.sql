-- Active: 1713806216316@@127.0.0.1@3306@smart-farming

DROP TABLE IF EXISTS sensors_records;

CREATE TABLE IF NOT EXISTS sensors_records (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  soil_humidity INT NOT NULL,
  ambient_humidity INT NOT NULL,
  temperature DECIMAL(10, 2) NOT NULL,
  water_volume DECIMAL(10, 2) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  plant_id CHAR(36) DEFAULT '8fc5808a-00de-11ef-8cc2-0242ac150002',
  FOREIGN KEY (plant_id) REFERENCES plants(id)
);
INSERT INTO sensors_records (soil_humidity, ambient_humidity, temperature, water_volume, created_at) 
VALUES (1, 1, 5, 5, '2005-09-30 00:00:00');

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



SELECT 
  soil_humidity, ambient_humidity, temperature, water_volume, created_at
FROM sensors_records
ORDER BY created_at DESC
LIMIT 1;

DELETE FROM sensors_records;
