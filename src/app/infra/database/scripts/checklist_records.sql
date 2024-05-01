-- Active: 1712147539997@@127.0.0.1@3306@smart-farming
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

SELECT CR.*, P.id AS plant_id, P.name AS plant_name, P.id AS plant_id, P.hex_color AS plant_color
FROM checklist_records AS CR
JOIN plants AS P.id = CR.plant_id
WHERE CR.id = '';

SELECT CR.*, P.id AS plant_id, P.name AS plant_name, P.hex_color AS plant_color
FROM checklist_records AS CR 
JOIN plants AS P ON P.id = CR.plant_id
ORDER BY created_at DESC;

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

DELETE FROM checklist_records;