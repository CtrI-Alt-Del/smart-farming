CREATE TABLE users(
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
  email VARCHAR(320) NOT NULL,
  password VARCHAR(40)
);

#INSERT INTO users (email, password) VALUES ('username', MD5('123'));