-- Active: 1712147539997@@127.0.0.1@3306@smart-farming


CREATE TABLE sensors (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  soil_humidity DECIMAL NOT NULL,
  ambient_humidity DECIMAL NOT NULL,
  temperature DECIMAL NOT NULL,
  water_volume DECIMAL NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);