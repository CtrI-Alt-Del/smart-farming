from faker import Faker

from core.entities import SensorsRecord
from core.commons import Datetime, Weekday

from .base_faker import BaseFaker
from .plants_faker import PlantsFaker


class SensorsRecordsFaker(BaseFaker):
    @classmethod
    def fake(cls, **base_fake_data):
        faker = Faker()

        if base_fake_data is not None:
            cls._base_fake_data = base_fake_data

        return SensorsRecord(
            id=cls._fake_attribute("id", faker.uuid4()),
            soil_humidity=cls._fake_attribute(
                "soil_humidity", faker.pyint(min_value=0, max_value=100)
            ),
            ambient_humidity=cls._fake_attribute(
                "ambient_humidity", faker.pyint(min_value=0, max_value=100)
            ),
            water_volume=cls._fake_attribute(
                "water_volume", faker.pyfloat(min_value=0.0)
            ),
            temperature=cls._fake_attribute(
                "temperature", faker.pyfloat(min_value=-273)
            ),
            created_at=cls._fake_attribute("created_at", Datetime(faker.date_time())),
            weekday=cls._fake_attribute("weekday", Weekday(faker.date_this_year())),
            plant=cls._fake_attribute("plant", PlantsFaker.fake()),
        )
