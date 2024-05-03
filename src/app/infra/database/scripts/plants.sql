-- Active: 1713899386704@@127.0.0.1@3306@smart-farming

DROP TABLE IF EXISTS plants;


ALTER TABLE plants ADD COLUMN created_at DATETIME DEFAULT (NOW()) NOT NULL;

INSERT INTO plants (id, name, hex_color) 
VALUES ('1ded0f79-01a5-11ef-9b63-0242ac1b0002' ,'alface','#D9F7EB');

SELECT * FROM plants;