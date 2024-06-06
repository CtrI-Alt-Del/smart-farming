-- Active: 1715783627262@@localhost@3307
DROP TABLE IF EXISTS user;

USE `smart-farming`;


CREATE TABLE IF NOT EXISTS user (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  email VARCHAR(255) NOT NULL,
  password TEXT NOT NULL
);

INSERT INTO user (email, password) VALUES 
(
  'ctrlaltdelsup@gmail.com', 
  '$2b$12$wbgdsX1apeZ8NZ75kgLJsuRCZnjm34CXXMgk6mx4WoAzExtF6w22G' -- bananaSM77$
);

SELECT * FROM user;


DELETE FROM user;
