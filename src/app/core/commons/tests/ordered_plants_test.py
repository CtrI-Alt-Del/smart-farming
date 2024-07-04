from core.commons.ordered_plants import OrderedPlants
from core.entities.tests.fakers import PlantsFaker


def describe_ordered_plants_common():

    def it_should_not_order_if_has_only_one_plant_or_none():
        fake_plant = PlantsFaker.fake()

        ordered_plants = OrderedPlants([fake_plant], active_plant_id=fake_plant.id)
        assert ordered_plants.get_value() == [fake_plant]

        ordered_plants = OrderedPlants([], active_plant_id=None)
        assert ordered_plants.get_value() == []

    def it_should_order_putting_the_active_plant_at_the_beginning_of_the_list():
        fake_plants = PlantsFaker.fake_many(5)
        active_fake_plant = PlantsFaker.fake()

        fake_plants.append(active_fake_plant)

        ordered_plants = OrderedPlants(
            plants=fake_plants, active_plant_id=active_fake_plant.id
        )

        assert len(ordered_plants.get_value()) == 6
        assert ordered_plants.get_value()[0] == active_fake_plant
