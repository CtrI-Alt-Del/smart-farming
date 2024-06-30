from core.commons import Error
from core.interfaces.repositories import (
    PlantsRepositoryInterface,
)


class GetPlantById:
    def __init__(
        self,
        repository: PlantsRepositoryInterface,
    ):
        self.repository = repository

    def execute(self, id: str):
        try:
            if not isinstance(id, str):
                raise Error(
                    ui_message="Planta inválida",
                    internal_message="Plant id is not string",
                    status_code=400,
                )

            return self.repository.get_plant_by_id(id)

        except Error as error:
            raise error
