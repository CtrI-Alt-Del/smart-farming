from core.commons import Error

from infra.repositories import plants_repository


class DeleteChecklistRecords:
    def execute(self, plants_ids: list[str]) -> None:
        try:
            for id in plants_ids:
                if id and isinstance(id, str):
                    has_plants = bool(
                        plants_repository.get_plant_by_id(id)
                    )

                    if not has_plants:
                        raise Error(
                            ui_message="Registro plant não encontrado",
                            internal_message="Plant not found",
                        )

                    plants_repository.delete_plant_by_id(id)

        except Error as error:
            raise error
