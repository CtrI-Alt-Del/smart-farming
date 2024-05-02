from core.entities.plant import Plant
from infra.database import mysql


class PlantsRepository:
    def create_plant_record(self, plants_record: Plant):
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

    def get_plant_by_id(self, id: str) -> Plant | None:
        row = mysql.query(
            sql="SELECT * FROM plants WHERE id = %s",
            is_single=True,
            params=[id],
        )

        if row:
            return self.__get_plant_entity(row)

        return None

    def update_plant_by_id(self, plant: Plant) -> None:
        mysql.mutate(
            """
            UPDATE plants 
            SET
                name = %s, 
                hex_color = %s
            WHERE id = %s
            """,
            params=[
                plant.name,
                plant.hex_color,
                plant.id,
            ],
        )
