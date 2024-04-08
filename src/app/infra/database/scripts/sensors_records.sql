-- Active: 1712144580322@@127.0.0.1@3306

DROP TABLE IF EXISTS sensors_records;

CREATE TABLE sensors_records (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  soil_humidity INT NOT NULL,
  ambient_humidity INT NOT NULL,
  temperature DECIMAL(10, 2) NOT NULL,
  water_volume DECIMAL(10, 2) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM sensors_records;