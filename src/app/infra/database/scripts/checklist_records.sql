
Active-- Active: 1712144580322@@127.0.0.1@3306@smart-farming
DROP TABLE checklist_records;

CREATE TABLE checklist_records (
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
  fertiliziation_date DATE NOT NULL DEFAULT (CURDATE()),
  harvested_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  report TEXT
);

