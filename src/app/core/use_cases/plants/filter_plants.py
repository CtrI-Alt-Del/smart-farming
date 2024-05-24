from infra.repositories import plants_repository


class FilterPlants:
    def execute(self, plant_name: str | None):
        plant_name = plant_name.strip()
        if isinstance(plant_name, str) and len(plant_name) != 0:
            return plants_repository.filter_plants_by_name(plant_name)

        return plants_repository.get_plants()
