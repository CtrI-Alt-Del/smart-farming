-- Active: 1714828967728@@127.0.0.1@3306
DROP TABLE IF EXISTS user;

CREATE TABLE IF NOT EXISTS user (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) 
VALUES ('douglas.rodri@gmail.com', 'banana');
SELECT * FROM user;
