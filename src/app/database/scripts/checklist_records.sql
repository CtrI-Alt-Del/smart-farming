-- Active: 1712098149489@@127.0.0.1@3306@smart-farming
DROP TABLE checklist_records;

CREATE TABLE checklist_records (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  soil_ph DECIMAL NOT NULL,
  soil_humidity DECIMAL NOT NULL,
  water_consumption DECIMAL NOT NULL,
  air_humidity DECIMAL NOT NULL,
  temperature DECIMAL NOT NULL,
  illuminance DECIMAL NOT NULL,
  lai DECIMAL NOT NULL,
  leaf_apperance ENUM('a', 'b'),
  leaf_color ENUM('a', 'b'),
  plantation_type ENUM('a', 'b'),
  fertiliziation_date DATE NOT NULL DEFAULT (CURDATE()),
  harvested_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  report TEXT NOT NULL
);

