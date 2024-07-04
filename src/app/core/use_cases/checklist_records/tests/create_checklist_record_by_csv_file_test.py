from pathlib import Path

from pytest import fixture, raises
from werkzeug.datastructures import FileStorage

from core.use_cases.tests.mocks.repositories import (
    PlantsRepositoryMock,
    ChecklistRecordsRepositoryMock,
)
from core.use_cases.tests.mocks.providers import DataAnalyserProviderMock
from core.entities import Plant
from core.errors.plants import PlantNotFoundError
from core.entities.tests.fakers import PlantsFaker
from core.errors.validation import DatetimeNotValidError, HourNotValidError
from core.constants import CSV_FILE_COLUMNS


from ..create_checklist_record_by_csv_file import CreateChecklistRecordsByCsvFile


def fake_record(base_fake_record: dict = {}):
    return {
        "em qual plantio você quer coletar os dados?": "interno",
        "data da coleta": "15/12/2023",
        "hora da coleta (inserir valor de 0 a 23)": 12,
        "temperatura ambiente?": 24.7,
        "ph do solo?": 7,
        "umidade do solo?": 72,
        "umidade do ar?": 55,
        "validade da adubação?": "30/12/2023",
        "consumo de água (mililitros)?": 0,
        "luminosidade (lux)?": 2,
        "iaf (índice de área foliar)?": 0,
        "qual o aspecto das folhas?": "viscoca",
        "qual a coloração das folhas?": "verde",
        "algum desvio detectado durante o processo?": "não",
        "planta": "alface",
        **base_fake_record,
    }


def describe_create_checklist_records_by_csv_file_use_case():
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
    def checklist_records_repository():
        return ChecklistRecordsRepositoryMock()

    @fixture
    def data_analyser_provider():
        data_analyser_provider = DataAnalyserProviderMock()
        data_analyser_provider.get_columns = lambda: CSV_FILE_COLUMNS[
            "checklist_records"
        ]

        return data_analyser_provider

    @fixture
    def use_case(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        plants_repository: PlantsRepositoryMock,
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        checklist_records_repository.clear_records()
        return CreateChecklistRecordsByCsvFile(
            checklist_records_repository=checklist_records_repository,
            plants_repository=plants_repository,
            data_analyser_provider=data_analyser_provider,
        )

    @fixture
    def file(tmp_path: Path):
        return FileStorage(tmp_path / "fake_csv_.xlsx")

    def it_should_throw_error_if_datetime_from_any_record_is_not_valid(
        file: FileStorage,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: CreateChecklistRecordsByCsvFile,
    ):

        data_analyser_provider.convert_to_list_of_records = lambda: [
            fake_record({"data da coleta": "12/12-2024"})
        ]

        with raises(DatetimeNotValidError):
            use_case.execute(file)

        data_analyser_provider.convert_to_list_of_records = lambda: [
            fake_record({"validade da adubação?": "12/99/2024"})
        ]

        with raises(DatetimeNotValidError):
            use_case.execute(file)

        data_analyser_provider.convert_to_list_of_records = lambda: [
            fake_record(
                {
                    "hora da coleta (inserir valor de 0 a 23)": 99,
                }
            )
        ]

        with raises(HourNotValidError) as error:
            use_case.execute(file)

        assert str(error.value) == "Valor da hora precisa ser um número entre 0 e 23"

    def it_should_create_checklist_records(
        file: FileStorage,
        fake_plant: Plant,
        data_analyser_provider: DataAnalyserProviderMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: CreateChecklistRecordsByCsvFile,
    ):
        record = fake_record()

        data_analyser_provider.convert_to_list_of_records = lambda: [record]

        use_case.execute(file)

        last_record = checklist_records_repository.get_last_checklist_records(count=1)[
            0
        ]

        assert last_record.soil_humidity == record["umidade do solo?"]
        assert last_record.soil_ph == record["ph do solo?"]
        assert (
            last_record.plantation_type
            == record["em qual plantio você quer coletar os dados?"]
        )
        assert last_record.lai == record["iaf (índice de área foliar)?"]
        assert last_record.illuminance == record["luminosidade (lux)?"]
        assert last_record.leaf_appearance == record["qual o aspecto das folhas?"]
        assert last_record.leaf_color == record["qual a coloração das folhas?"]
        assert (
            last_record.report == record["algum desvio detectado durante o processo?"]
        )
        assert last_record.air_humidity == record["umidade do ar?"]
        assert last_record.temperature == record["temperatura ambiente?"]
        assert last_record.water_consumption == record["consumo de água (mililitros)?"]
        assert (
            last_record.fertilizer_expiration_date.get_value() == "2023-12-30 00:00:00"
        )
        assert last_record.created_at.get_value() == "2023-12-15 12:00:00"
        assert last_record.plant == fake_plant

    def it_should_throw_error_if_there_is_no_plant_in_repository(
        file: FileStorage,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: CreateChecklistRecordsByCsvFile,
    ):
        data_analyser_provider.convert_to_list_of_records = lambda: [
            fake_record({"planta": "beterraba"}),
        ]

        with raises(PlantNotFoundError) as error:
            use_case.execute(file)

        assert (
            str(error.value)
            == "Planta não encontrada para o registro da data 15/12/2023 12:00"
        )
