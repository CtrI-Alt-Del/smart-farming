-- Active: 1712602370861@@localhost@3306@smart-farming

DROP TABLE IF EXISTS sensors_records;

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
