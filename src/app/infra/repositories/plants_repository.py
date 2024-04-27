from core.entities.plant import Plant
from infra.database import mysql


class PlantsRepository:
    def create_plants_record(self, plants_record: Plant):
        sql = """
        INSERT INTO plants
        (name, hex_color)
        VALUES (%s, %s)
        """
        params = [
            plants_record.name,
            plants_record.hex_color,
        ]

        mysql.mutate(sql, params)

    def get_plants(self) -> list[Plant]:
        select_query = "SELECT * FROM plants"
        rows = mysql.query(sql=select_query, is_single=False)

        plants = []

        for row in rows:
            plants.append(self.__get_plant_entity(row))

        return plants

    def __get_plant_entity(self, row):
        return Plant(id=row["id"], name=row["name"], hex_color=row["hex_color"])
