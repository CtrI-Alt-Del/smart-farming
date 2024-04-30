<<<<<<< HEAD
-- Active: 1714396197562@@127.0.0.1@3306@smart-farming
=======
-- Active: 1714479268496@@127.0.0.1@3306@smart-farming
>>>>>>> refs/remotes/origin/main
DROP TABLE IF EXISTS plants;

CREATE TABLE IF NOT EXISTS plants (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  hex_color VARCHAR(7) NOT NULL UNIQUE
);

INSERT INTO plants (id, name, hex_color) VALUES ('4544afe3-0661-11ef-9512-0242ac140002' ,'alface','#D4F7EB');



SELECT * FROM plants;