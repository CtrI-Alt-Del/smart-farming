MYSQL = {
    "tables": {
        "plants": """
        CREATE TABLE plants (
            id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
            name VARCHAR(255) NOT NULL UNIQUE,
            hex_color VARCHAR(7) NOT NULL,
            created_at DATETIME DEFAULT (NOW()) NOT NULL
        );
        """,
        "sensors_records": """
          CREATE TABLE IF NOT EXISTS sensors_records (
          id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
          soil_humidity INTEGER NOT NULL,
          ambient_humidity INTEGER NOT NULL,
          temperature DECIMAL(10, 2) NOT NULL,
          water_volume DECIMAL(10, 2) NOT NULL,
          created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
          plant_id CHAR(36) DEFAULT '4544afe3-0661-11ef-9512-0242ac140002',
          FOREIGN KEY (plant_id) REFERENCES plants(id) ON DELETE CASCADE
        );
        """,
        "checklist_records": """
        CREATE TABLE IF NOT EXISTS checklist_records (
          id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
          soil_ph INTEGER NOT NULL,
          soil_humidity INTEGER NOT NULL,
          air_humidity INTEGER NOT NULL,
          water_consumption DECIMAL(10, 2) NOT NULL,
          temperature DECIMAL(10, 1) NOT NULL,
          illuminance DECIMAL(10, 2) NOT NULL,
          lai DECIMAL(10, 2),
          leaf_appearance ENUM('SAUDAVEL', 'MURCHA', 'NÃO REGISTRADO') DEFAULT 'NÃO REGISTRADO',
          leaf_color ENUM(
          'VERDE CLARO PREDOMINANTE',
          'VERDE ESCURO PREDOMINANTE',
          'VERDE CLARO COM ALGUMAS MANCHAS CLARAS',
          'VERDE CLARO COM VARIAS MANCHAS CLARAS',
          'VERDE CLARO COM ALGUMAS MANCHAS ESCURAS',
          'VERDE CLARO COM VARIAS MANCHAS ESCURAS',
          'VERDE ESCURO COM ALGUMAS MANCHAS CLARAS',
          'VERDE ESCURO COM VARIAS MANCHAS CLARAS',
          'VERDE ESCURO COM ALGUMAS MANCHAS ESCURAS',
          'VERDE ESCURO COM VARIAS MANCHAS ESCURAS',
          'OPACO PREDOMINANTE',
          'AVERMELHADO PREDOMINANTE', 
          'NÃO REGISTRADO'
          ) DEFAULT 'NÃO REGISTRADO',
          plantation_type ENUM('PLANTIO INTERNO (FATEC)', 'PLANTIO EXTERNO (CASA)') DEFAULT 'PLANTIO INTERNO (FATEC)',
          fertilizer_expiration_date DATE NOT NULL,
          created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
          report TEXT,
          plant_id CHAR(36) DEFAULT '4544afe3-0661-11ef-9512-0242ac140002',
          FOREIGN KEY (plant_id) REFERENCES plants(id) ON DELETE CASCADE
        );
      """,
        "user": """
      CREATE TABLE user (
        id CHAR(36) DEFAULT (UUID()) PRIMARY KEY NOT NULL,
        email VARCHAR(255) NOT NULL,
        password TEXT NOT NULL,
        active_plant_id CHAR(36) DEFAULT '4544afe3-0661-11ef-9512-0242ac140002',
        FOREIGN KEY (active_plant_id) REFERENCES plants(id) ON DELETE SET NULL
      );
        """,
    },
    "inserts": [
        """
        INSERT INTO plants (id, name, hex_color) 
        VALUES ('4544afe3-0661-11ef-9512-0242ac140002' ,'Alface','#3A7D44');
        """,
        """
        INSERT INTO user (email, password) VALUES 
        (
          'supsmartfarm@gmail.com', 
          '$2b$12$GwF4gb7U99hSSEDs6OJr3OenabAd4MEYzGpK4ptavZ14fGwKBVEYy'
        );
        """,
    ],
}
