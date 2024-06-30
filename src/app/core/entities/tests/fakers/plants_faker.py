from faker import Faker

from core.entities import Plant

from .base_faker import BaseFaker


class PlantsFaker(BaseFaker):
    @classmethod
    def fake(cls, **base_fake_data):
        faker = Faker()

        if base_fake_data is not None:
            cls._base_fake_data = base_fake_data

        return Plant(
            id=cls._fake_attribute("id", faker.uuid4()),
            name=cls._fake_attribute("name", faker.name_nonbinary()),
            hex_color=cls._fake_attribute("hex_color", faker.hex_color()),
        )
