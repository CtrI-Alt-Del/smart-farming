-- Active: 1713899386704@@127.0.0.1@3306@smart-farming
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
  leaf_apperance ENUM('SAUDAVEL', 'MURCHA'),
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
  plant_id CHAR(36) DEFAULT '8fc5808a-00de-11ef-8cc2-0242ac150002',
  FOREIGN KEY (plant_id) REFERENCES plants(id)
);

SELECT * FROM checklist_records ORDER BY created_at

INSERT INTO checklist_records (
  soil_ph,
  soil_humidity,
  water_consumption,
  air_humidity,
  temperature,
  illuminance,
  lai,
  leaf_apperance,
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
  'SAUDAVEL', -- leaf_apperance
  'VERDE CLARO DOMINANTE', -- leaf_color
  'PLANTIO INTERNO(FATEC)', -- plantation_type
  '2024-03-03', -- fertilizer_expiration_date
  'Relatório de checagem', -- report
  '1ded0f79-01a5-11ef-9b63-0242ac1b0002' -- plant_id
);