from core.entities.plant import Plant


class OrderedPlants:
    value: list[Plant] = []

    def __init__(self, plants: list[Plant], active_plant_id: str):
        self.value = self.__order(plants, active_plant_id)

    def __order(self, plants: list[Plant], active_plant_id: str):
        plants_count = len(plants)
        if plants_count == 0 or plants_count == 1:
            return plants

        filtered_plants_by_id = filter(
            lambda plant: plant.id == active_plant_id, plants
        )

        active_plant = list(filtered_plants_by_id)[0]

        ordered_plants = [active_plant]
        ordered_plants.extend(
            [plant for plant in plants if plant.id != active_plant_id]
        ),

        return ordered_plants

    def get_value(self):
        return self.value
