from core.commons import Error
from infra.repositories import plants_repository


class GetPlantById:
    def execute(self, id: str) -> None:
        try:
            if not isinstance(id, str):
                raise Error("Planta não econtrada")

            plant = plants_repository.get_plant_by_id(id)
            return plant

        except Error as error:
            raise error
