from faker import Faker

from core.entities import User

from .base_faker import BaseFaker


class UsersFaker(BaseFaker):
    @classmethod
    def fake(cls, **base_fake_data):
        faker = Faker()

        if base_fake_data is not None:
            cls._base_fake_data = base_fake_data

        return User(
            id=cls._fake_attribute("id", faker.uuid4()),
            email=cls._fake_attribute("email", faker.email()),
            password=cls._fake_attribute("password", faker.password()),
            active_plant_id=cls._fake_attribute("active_plant_id", faker.uuid4()),
        )
