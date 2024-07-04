from faker import Faker

from core.entities import CheckListRecord
from core.commons import Date, Datetime

from .base_faker import BaseFaker
from .plants_faker import PlantsFaker


class ChecklistRecordsFaker(BaseFaker):
    @classmethod
    def fake(cls, **base_fake_data):
        faker = Faker()

        if base_fake_data is not None:
            cls._base_fake_data = base_fake_data

        return CheckListRecord(
            id=cls._fake_attribute("id", faker.uuid4()),
            soil_ph=cls._fake_attribute(
                "soil_ph", faker.pyint(min_value=0, max_value=100)
            ),
            water_consumption=cls._fake_attribute(
                "water_consumption", faker.pyint(min_value=0, max_value=100)
            ),
            lai=cls._fake_attribute("lai", faker.pyfloat(min_value=0.0)),
            temperature=cls._fake_attribute(
                "temperature", faker.pyfloat(min_value=-273)
            ),
            illuminance=cls._fake_attribute(
                "illuminance", faker.pyfloat(min_value=0.0)
            ),
            leaf_appearance=cls._fake_attribute("leaf_appearance", faker.pystr()),
            leaf_color=cls._fake_attribute("leaf_color", faker.pystr()),
            plantation_type=cls._fake_attribute("plantation_type", faker.pystr()),
            report=cls._fake_attribute("report", faker.pystr()),
            fertilizer_expiration_date=cls._fake_attribute(
                "fertilizer_expiration_date", Date(faker.date_this_year())
            ),
            created_at=cls._fake_attribute("created_at", Datetime(faker.date_time())),
            plant=cls._fake_attribute("plant", PlantsFaker.fake()),
        )
