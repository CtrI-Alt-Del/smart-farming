-- Active: 1713899386704@@127.0.0.1@3306@smart-farming
DROP TABLE IF EXISTS checklist_records;

INSERT INTO checklist_records (
  soil_ph,
  soil_humidity,
  water_consumption,
  air_humidity,
  temperature,
  illuminance,
  lai,
  leaf_appearance,
  leaf_color,
  plantation_type,
  fertilizer_expiration_date,
  report,
  plant_id
) VALUES (
  6.5, -- soil_ph
  50.0, -- soil_humidity
  1000.0, -- water_consumption
  70.0, -- air_humidity
  25.0, -- temperature
  50000.0, -- illuminance
  3.5, -- lai
  'SAUDAVEL', -- leaf_appearance
  'VERDE CLARO DOMINANTE', -- leaf_color
  'PLANTIO INTERNO(FATEC)', -- plantation_type
  CURDATE(), -- fertilizer_expiration_date
  'Relatório de checagem', -- report
  '1ded0f79-01a5-11ef-9b63-0242ac1b0002' -- plant_id
);

INSERT INTO checklist_records (
  soil_ph,
  soil_humidity,
  water_consumption,
  air_humidity,
  temperature,
  illuminance,
  lai,
  leaf_appearance,
  leaf_color,
  plantation_type,
  fertilizer_expiration_date,
  report,
  plant_id
) VALUES (
  6.5, -- soil_ph
  50.0, -- soil_humidity
  1000.0, -- water_consumption
  70.0, -- air_humidity
  25.0, -- temperature
  50000.0, -- illuminance
  3.5, -- lai
  'SAUDAVEL', -- leaf_appearance
  'VERDE CLARO PREDOMINANTE', -- leaf_color
  'PLANTIO INTERNO (FATEC)', -- plantation_type
  '2024-03-03', -- fertilizer_expiration_date
  'Relatório de checagem', -- report
  '1ded0f79-01a5-11ef-9b63-0242ac1b0002' -- plant_id
);

SELECT * FROM checklist_records;

SELECT *, P.id AS plant_id, P.name AS plant_name
FROM checklist_records AS CR 
JOIN plants AS P ON P.id = CR.plant_id
ORDER BY created_at;

SELECT leaf_appearance, leaf_color, created_at 
FROM checklist_records
ORDER BY created_at;  


SELECT lai, created_at, plant_id
FROM checklist_records
ORDER BY created_at ASC;

SELECT 
  DATE(created_at) AS date,
  ROUND(AVG(lai), 1) AS avg_lai,
  plant_id
FROM checklist_records
GROUP BY DATE(created_at), plant_id
ORDER BY date ASC;

DELETE FROM checklist_records;
