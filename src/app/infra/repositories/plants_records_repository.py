from core.entities.plants_record import PlantsRecord
from typing import List
from infra.database import mysql


class PlantsRecordsRepository:
    def create_plants_record(self, plants_record: PlantsRecord):
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

    def plants_records(self) -> List[PlantsRecord]:
        select_query = "SELECT * FROM plants"
        rows = mysql.query(sql=select_query, is_single=False)
        plants_records = []

        for row in rows:
            plants_records.append(
                PlantsRecord(
                    id=row["id"],
                    name=row["name"],
                    hex_color=row["hex_color"]
                )   
            )
        return plants_records
