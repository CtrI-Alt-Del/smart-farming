-- Active: 1717536900456@@127.0.0.1@3306@smart-farming
DROP TABLE IF EXISTS user;

USE `smart-farming`;

CREATE TABLE IF NOT EXISTS user (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  email VARCHAR(255) NOT NULL,
  password TEXT NOT NULL,
  active_plant_id CHAR(36) DEFAULT '4544afe3-0661-11ef-9512-0242ac140002'
  FOREIGN KEY (active_plant_id) REFERENCES plants(id) ON DELETE SET NULL
);

INSERT INTO user (email, password) VALUES 
(
  'supsmartfarm@gmail.com', 
  '$2b$12$lI9th4bnxp1XVsyqqSkRCOiScc0u99Gf6HUBXDtLqAtGevT4r06hC'
);

SELECT * FROM user;

DELETE FROM user;
