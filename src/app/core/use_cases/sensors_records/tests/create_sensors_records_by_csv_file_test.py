from pathlib import Path

from pytest import fixture, raises
from werkzeug.datastructures import FileStorage

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    SensorRecordsRepositoryMock,
)
from core.use_cases.tests.mocks.providers import DataAnalyserProviderMock
from core.entities import Plant
from core.errors.plants import PlantNotFoundError
from core.entities.tests.fakers import PlantsFaker
from core.errors.validation import DatetimeNotValidError
from core.constants import CSV_FILE_COLUMNS


from ..create_sensors_records_by_csv_file import CreateSensorsRecordsByCsvFile


def describe_create_sensors_records_by_csv_file_use_case():
    @fixture
    def fake_plant():
        return PlantsFaker.fake(name="alface")

    @fixture
    def plants_repository(fake_plant):
        plants_repository = PlantsRepositoryMock()
        plants_repository.clear_plants()
        plants_repository.create_plant(fake_plant)

        return plants_repository

    @fixture
    def sensors_records_repository():
        return SensorRecordsRepositoryMock()

    @fixture
    def data_analyser_provider():
        data_analyser_provider = DataAnalyserProviderMock()
        data_analyser_provider.get_columns = lambda: CSV_FILE_COLUMNS["sensors_records"]

        return data_analyser_provider

    @fixture
    def use_case(
        sensors_records_repository: SensorRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        sensors_records_repository.clear_records()
        return CreateSensorsRecordsByCsvFile(
            sensors_records_repository=sensors_records_repository,
            plants_repository=plants_repository,
            data_analyser_provider=data_analyser_provider,
        )

    @fixture
    def file(tmp_path: Path):
        return FileStorage(tmp_path / "fake_csv_.xlsx")

    def it_should_throw_error_if_datetime_from_any_record_is_not_valid(
        file: FileStorage,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: CreateSensorsRecordsByCsvFile,
    ):

        data_analyser_provider.convert_to_list_of_records = lambda: [
            {
                "data": "15/09/2023",
                "hora": "12:56",  # invalid time format
                "dia da semana": "quarta",
                "umidade solo": 72,
                "umidade Ambiente": 55,
                "temperatura": 24.7,
                "volume de Água (ml)": 0,
                "planta": "alface",
            }
        ]

        with raises(DatetimeNotValidError):
            use_case.execute(file)

        data_analyser_provider.convert_to_list_of_records = lambda: [
            {
                "data": "15-09-2023",  # invalid date format
                "hora": "12:56",
                "dia da semana": "quarta",
                "umidade solo": 72,
                "umidade Ambiente": 55,
                "temperatura": 24.7,
                "volume de Água (ml)": 0,
                "planta": "alface",
            }
        ]

        with raises(DatetimeNotValidError):
            use_case.execute(file)

        data_analyser_provider.convert_to_list_of_records = lambda: [
            {
                "data": "15/42/2023",  # invalid date
                "hora": "12:56:00",
                "dia da semana": "quarta",
                "umidade solo": 72,
                "umidade Ambiente": 55,
                "temperatura": 24.7,
                "volume de Água (ml)": 0,
                "planta": "alface",
            }
        ]

        with raises(DatetimeNotValidError):
            use_case.execute(file)

        data_analyser_provider.convert_to_list_of_records = lambda: [
            {
                "data": "15/09/2023",
                "hora": "12:99:00",  # invalid time
                "dia da semana": "quarta",
                "umidade solo": 72,
                "umidade Ambiente": 55,
                "temperatura": 24.7,
                "volume de Água (ml)": 0,
                "planta": "alface",
            }
        ]

        with raises(DatetimeNotValidError):
            use_case.execute(file)

    def it_should_create_sensors_records(
        file: FileStorage,
        fake_plant: Plant,
        data_analyser_provider: DataAnalyserProviderMock,
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: CreateSensorsRecordsByCsvFile,
    ):
        data_analyser_provider.convert_to_list_of_records = lambda: [
            {
                "data": "17/09/2023",
                "hora": "12:09:00",
                "dia da semana": "quarta",
                "umidade solo": 72,
                "umidade Ambiente": 55,
                "temperatura": 24.7,
                "volume de Água (ml)": 0,
                "planta": "alface",
            },
        ]

        use_case.execute(file)

        last_record = sensors_records_repository.get_last_sensors_records(count=1)[0]

        assert last_record.soil_humidity == 72
        assert last_record.ambient_humidity == 55
        assert last_record.temperature == 24.7
        assert last_record.water_volume == 0
        assert last_record.created_at.get_value() == "2023-09-17 12:09:00"
        assert last_record.plant == fake_plant

    def it_should_throw_error_if_there_is_no_plant_in_repository(
        file: FileStorage,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: CreateSensorsRecordsByCsvFile,
    ):
        data_analyser_provider.convert_to_list_of_records = lambda: [
            {
                "data": "17/09/2023",
                "hora": "12:09:00",
                "dia da semana": "quarta",
                "umidade solo": 72,
                "umidade Ambiente": 55,
                "temperatura": 24.7,
                "volume de Água (ml)": 0,
                "planta": "beterraba",  # Non-existing plant
            },
        ]

        with raises(PlantNotFoundError) as error:
            use_case.execute(file)

        assert (
            str(error.value)
            == "Planta não encontrada para o registro da data 17/09/2023 12:09"
        )
