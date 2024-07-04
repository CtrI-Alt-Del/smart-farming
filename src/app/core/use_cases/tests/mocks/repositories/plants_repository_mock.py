from core.entities.plant import Plant
from core.interfaces.repositories import PlantsRepositoryInterface


class PlantsRepositoryMock(PlantsRepositoryInterface):
    _plants: list[Plant] = []

    def create_plant(self, plant: Plant):
        self._plants.append(plant)

    def get_plants(self) -> list[Plant]:
        return self._plants

    def get_plant_by_id(self, id: str) -> Plant | None:
        plants = list(filter(lambda plant: plant.id == id, self._plants))

        if len(plants):
            return plants[0]

        return None

    def get_plant_by_name(self, name: str):
        plants = list(filter(lambda plant: plant.name == name, self._plants))

        if len(plants):
            return plants[0]

        return None

    def get_last_plant(self) -> Plant | None:
        if len(self._plants):
            return self._plants[-1]

        return None

    def filter_plants_by_name(self, plant_name: str) -> list[Plant]:
        plants = list(filter(lambda plant: plant_name in plant.name, self._plants))

        return plants

    def update_plant_by_id(self, plant: Plant) -> None:
        self._plants = [
            plant if plant.id == current_plant.id else current_plant
            for current_plant in self._plants
        ]

    def delete_plant_by_id(self, id: str):
        self._plants = [plant for plant in self._plants if plant.id != id]

    def clear_plants(self):
        self._plants = []
