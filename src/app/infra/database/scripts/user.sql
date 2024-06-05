-- Active: 1717536900456@@127.0.0.1@3306
DROP TABLE IF EXISTS user;

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
