-- Active: 1712918435172@@127.0.0.1@3306@smart_farming
DROP TABLE IF EXISTS plants;

CREATE TABLE IF NOT EXISTS plants (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  hex_color VARCHAR(7) NOT NULL UNIQUE
);

INSERT INTO plants (name, hex_color) VALUES ('alface','#D3F7EB');

SELECT * FROM plants;