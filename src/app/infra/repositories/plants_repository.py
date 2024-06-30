from core.entities.plant import Plant
from core.interfaces.repositories import PlantsRepositoryInterface

from infra.database import mysql


class PlantsRepository(PlantsRepositoryInterface):
    def create_plant(self, plants_record: Plant):
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
        select_query = "SELECT * FROM plants ORDER BY created_at DESC"
        rows = mysql.query(sql=select_query, is_single=False)

        plants = []

        for row in rows:
            plants.append(self.__get_plant_entity(row))

        return plants

    def get_plant_by_id(self, id: str) -> Plant | None:
        row = mysql.query(
            sql="SELECT * FROM plants WHERE id = %s",
            is_single=True,
            params=[id],
        )

        if row:
            return self.__get_plant_entity(row)

        return None

    def get_plant_by_name(self, name: str):
        row = mysql.query(
            sql="SELECT * FROM plants WHERE name = %s",
            params=[name],
            is_single=True,
        )

        if row:
            return self.__get_plant_entity(row)

        return None

    def get_last_plant(self) -> Plant | None:
        row = mysql.query(
            sql="SELECT * FROM plants ORDER BY created_at DESC LIMIT 1",
            is_single=True,
        )

        if row:
            return self.__get_plant_entity(row)

        return None

    def filter_plants_by_name(self, plant_name: str) -> list[Plant]:
        rows = mysql.query(
            sql=f"""
            SELECT * FROM plants
            WHERE name LIKE '%{plant_name.lower()}%'  
            ORDER BY created_at DESC
            """,
            is_single=False,
        )

        if len(rows) == 0:
            return []

        return [self.__get_plant_entity(row) for row in rows]

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

    def delete_plant_by_id(self, id: str):
        mysql.mutate(
            "DELETE FROM plants WHERE id = %s",
            params=[
                id,
            ],
        )

    def __get_plant_entity(self, row):
        return Plant(id=row["id"], name=row["name"], hex_color=row["hex_color"])
