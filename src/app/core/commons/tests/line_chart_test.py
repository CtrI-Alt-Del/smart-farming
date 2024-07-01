from datetime import date, timedelta

from pytest import fixture

from core.commons.line_chart import LineChart
from core.entities.tests.fakers import LineChartRecordsFaker, PlantsFaker


def fake_record(plant_id: str, value: int, days_range: date):
    current_date = date.today()

    return LineChartRecordsFaker.fake(
        plant_id=plant_id, value=value, date=current_date - timedelta(days=days_range)
    )


def describe_line_chart_common():
    @fixture
    def plant():
        return PlantsFaker.fake()

    @fixture
    def records(plant):
        fake_records_of_last_90_days = [
            fake_record(plant.id, value=90, days_range=90),
            fake_record(plant.id, value=90, days_range=52),
            fake_record(plant.id, value=90, days_range=40),
        ]
        fake_records_of_last_30_days = [
            fake_record(plant.id, value=30, days_range=30),
            fake_record(plant.id, value=30, days_range=24),
            fake_record(plant.id, value=30, days_range=12),
        ]
        fake_records_of_last_7_days = [
            fake_record(plant.id, value=7, days_range=7),
            fake_record(plant.id, value=7, days_range=3),
            fake_record(plant.id, value=7, days_range=1),
        ]

        fake_records = []
        fake_records.extend(fake_records_of_last_90_days)
        fake_records.extend(fake_records_of_last_30_days)
        fake_records.extend(fake_records_of_last_7_days)

        return fake_records

    def it_should_return_dates_for_each_days_range(records, plant):

        line_chart = LineChart(records)

        data = line_chart.get_data(plants=[plant])

        assert data[plant.id]["7 days"]["dates"] == [
            "24/06/2024",
            "28/06/2024",
            "30/06/2024",
        ]
        assert data[plant.id]["30 days"]["dates"] == [
            "01/06/2024",
            "07/06/2024",
            "19/06/2024",
            "24/06/2024",
            "28/06/2024",
            "30/06/2024",
        ]
        assert data[plant.id]["90 days"]["dates"] == [
            "02/04/2024",
            "10/05/2024",
            "22/05/2024",
            "01/06/2024",
            "07/06/2024",
            "19/06/2024",
            "24/06/2024",
            "28/06/2024",
            "30/06/2024",
        ]

    def it_should_return_values_for_each_days_range(records, plant):

        line_chart = LineChart(records)

        data = line_chart.get_data(plants=[plant])

        assert data[plant.id]["7 days"]["values"] == [7, 7, 7]
        assert data[plant.id]["30 days"]["values"] == [30, 30, 30, 7, 7, 7]
        assert data[plant.id]["90 days"]["values"] == [90, 90, 90, 30, 30, 30, 7, 7, 7]

    def it_should_calculate_average_for_each_days_range(records, plant):
        line_chart = LineChart(records)

        data = line_chart.get_data(plants=[plant])

        assert round(data[plant.id]["7 days"]["average"], 2) == 7.00
        assert round(data[plant.id]["30 days"]["average"], 2) == 18.5
        assert round(data[plant.id]["90 days"]["average"], 2) == 42.33

    def it_should_get_data_for_each_plant(records, plant):
        fake_plants = [plant]
        line_chart = LineChart(records)

        other_fake_plants = PlantsFaker.fake_many(3)
        fake_plants.extend(other_fake_plants)

        data = line_chart.get_data(plants=fake_plants)

        for fake_plant in fake_plants:
            assert fake_plant.id in data
