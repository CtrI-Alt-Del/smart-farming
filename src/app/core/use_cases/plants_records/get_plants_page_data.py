from infra.repositories import plants_repository


class GetPlantsPageData:
    def execute(self):
        plants = plants_repository.get_plants()

        return plants
