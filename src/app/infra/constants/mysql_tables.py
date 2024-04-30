MYSQL_TABLES = {
    "sensors_records": """
    CREATE TABLE sensors_records (
      id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
      soil_humidity INT NOT NULL,
      ambient_humidity INT NOT NULL,
      temperature DECIMAL(10, 2) NOT NULL,
      water_volume DECIMAL(10, 2) NOT NULL,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
  );
  """,
    "checklist_records": """
    CREATE TABLE checklist_records (
      id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
      soil_ph DECIMAL(10, 2) NOT NULL,
      soil_humidity DECIMAL(10, 2) NOT NULL,
      water_consumption DECIMAL(10, 2) NOT NULL,
      air_humidity DECIMAL(10, 2) NOT NULL,
      temperature DECIMAL(10, 2) NOT NULL,
      illuminance DECIMAL(10, 2) NOT NULL,
      lai DECIMAL(10, 2),
      leaf_appearance ENUM('SAUDAVEL', 'MURCHA'),
      leaf_color ENUM('VERDE CLARO DOMINANTE',
      'VERDE ESCURO DOMINATE',
      'VERDE CLARO COM ALGUMAS MANCHAS CLARAS',
      'VERDE CLARO COM VARIAS MANCHAS CLARAS',
      'VERDE CLARO COM ALGUMAS MANCHAS ESCURAS',
      'VERDE CLARO COM VARIAS MANCHAS ESCURAS',
      'VERDE ESCURO COM ALGUMAS MANCHAS CLARAS',
      'VERDE ESCURO COM VARIAS MANCHAS CLARAS',
      'VERDE ESCURO COM ALGUMAS MANCHAS ESCURAS',
      'VERDE ESCURO COM VARIAS MANCHAS ESCURAS',
      'OPACO PREDOMINANTE',
      'AVERMELHADO PREDOMINANTE'),
      plantation_type ENUM('PLANTIO INTERNO(FATEC)', 'PLANTIO EXTERNO(CASA)'),
      fertilizer_expiration_date DATE NOT NULL DEFAULT (CURDATE()),
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      report TEXT,
      plant_id CHAR(36) DEFAULT '4544afe3-0661-11ef-9512-0242ac140002',
      FOREIGN KEY (plant_id) REFERENCES plants(id)
  );
  """,
  "plants": """
   CREATE TABLE plants (
    id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    hex_color VARCHAR(7) NOT NULL
  );
  
  """,
    "user": """
    CREATE TABLE user (
      id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
      email VARCHAR(320) NOT NULL,
      password VARCHAR(40) NOT NULL
  );
  """,
}
