-- Active: 1716251474854@@smart-farming-database.cvmsweq84ztf.us-east-2.rds.amazonaws.com@3306@information_schema

DROP TABLE IF EXISTS plants;

ALTER TABLE plants ADD COLUMN created_at DATETIME DEFAULT (NOW()) NOT NULL;

INSERT INTO plants (id, name, hex_color) 
VALUES ('1ded0f79-01a5-11ef-9b63-0242ac1b0002' ,'Alface','#D9F7EB');

SELECT * FROM plants;

DELETE FROM plants;
