from faker import Faker

from core.entities import LineChartRecord

from .base_faker import BaseFaker


class LineChartRecordsFaker(BaseFaker):
    @classmethod
    def fake(cls, **base_fake_data):
        faker = Faker()

        if base_fake_data is not None:
            cls._base_fake_data = base_fake_data

        return LineChartRecord(
            id=cls._fake_attribute("id", faker.uuid4()),
            date=cls._fake_attribute("date", faker.date_this_month()),
            value=cls._fake_attribute("value", faker.pyint(min_value=0)),
            plant_id=cls._fake_attribute("plant_id", faker.uuid4()),
        )
