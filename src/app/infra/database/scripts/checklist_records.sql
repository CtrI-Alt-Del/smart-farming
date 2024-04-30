-- Active: 1712258180714@@127.0.0.1@3306@smart-farming
DROP TABLE IF EXISTS checklist_records;

CREATE TABLE IF NOT EXISTS checklist_records (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  soil_ph DECIMAL(10, 2) NOT NULL,
  soil_humidity DECIMAL(10, 2) NOT NULL,
  water_consumption DECIMAL(10, 2) NOT NULL,
  air_humidity DECIMAL(10, 2) NOT NULL,
  temperature DECIMAL(10, 2) NOT NULL,
  illuminance DECIMAL(10, 2) NOT NULL,
  lai DECIMAL(10, 2),
  leaf_appearance ENUM('SAUDAVEL', 'MURCHA'),
  leaf_color ENUM('VERDE CLARO DOMINANTE',
   'VERDE ESCURO DOMINATE',
   'VERDE CLARO COM ALGUMAS MANCHAS CLARAS',
   'VERDE CLARO COM VARIAS MANCHAS CLARAS',
  'VERDE CLARO COM ALGUMAS MANCHAS ESCURAS',
   'VERDE CLARO COM VARIAS MANCHAS ESCURAS',
   'VERDE ESCURO COM ALGUMAS MANCHAS CLARAS',
   'VERDE ESCURO COM VARIAS MANCHAS CLARAS',
   'VERDE ESCURO COM ALGUMAS MANCHAS ESCURAS',
   'VERDE ESCURO COM VARIAS MANCHAS ESCURAS',
   'OPACO PREDOMINANTE',
   'AVERMELHADO PREDOMINANTE'),
  plantation_type ENUM('PLANTIO INTERNO(FATEC)', 'PLANTIO EXTERNO(CASA)'),
  fertilizer_expiration_date DATE NOT NULL DEFAULT (CURDATE()),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  report TEXT,
  plant_id CHAR(36) DEFAULT '4544afe3-0661-11ef-9512-0242ac140002',
  FOREIGN KEY (plant_id) REFERENCES plants(id)
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
  'VERDE CLARO DOMINANTE', -- leaf_color
  'PLANTIO INTERNO(FATEC)', -- plantation_type
  CURDATE(), -- fertilizer_expiration_date
  'Relatório de checagem', -- report
  '4544afe3-0661-11ef-9512-0242ac140002' -- plant_id
);

SELECT *, P.id AS plant_id, P.name AS plant_name
FROM checklist_records AS CR 
JOIN plants AS P ON P.id = CR.plant_id
ORDER BY created_at;

SELECT COUNT(id) FROM checklist_records;

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
  '2024-03-03', -- fertilizer_expiration_date
  'Relatório de checagem', -- report
  '4544afe3-0661-11ef-9512-0242ac140002' -- plant_id
);

DELETE FROM checklist_records;