from datetime import datetime

from pytest import fixture

from core.use_cases.tests.mocks.repositories import ChecklistRecordsRepositoryMock
from core.use_cases.tests.mocks.providers import DataAnalyserProviderMock
from core.entities.tests.fakers import ChecklistRecordsFaker, PlantsFaker
from core.commons import Datetime
from core.constants import CSV_FILE_COLUMNS

from ..get_checklist_records_csv_file import GetChecklistRecordsCsvFile


def describe_get_checklist_records_csv_file_use_case():
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
        data_analyser_provider: DataAnalyserProviderMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
    ):
        checklist_records_repository.clear_records()
        return GetChecklistRecordsCsvFile(
            checklist_records_repository=checklist_records_repository,
            data_analyser_provider=data_analyser_provider,
        )

    @fixture
    def folder():
        return "fake_csv_folder"

    def it_should_create_csv_file_in_a_specific_path(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: GetChecklistRecordsCsvFile,
    ):
        use_case.execute(plant_id=None, start_date=None, end_date=None, folder=folder)

        csv_file = data_analyser_provider.csv_file

        assert csv_file["path"] == f"{folder}/registros-checklist.xlsx"

    def it_should_create_csv_file_with_empty_data_if_there_is_no_any_checklist_record_in_repository(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: GetChecklistRecordsCsvFile,
    ):
        use_case.execute(plant_id=None, start_date=None, end_date=None, folder=folder)

        csv_file = data_analyser_provider.csv_file

        for data in csv_file["data"].values():
            assert data == []

    def it_should_create_csv_file_containing_checklist_records(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: GetChecklistRecordsCsvFile,
    ):
        fake_records = ChecklistRecordsFaker.fake_many()

        fake_records.sort(
            key=lambda record: record.created_at.get_value(is_datetime=True)
        )

        checklist_records_repository.create_many_checklist_records(fake_records)

        use_case.execute(plant_id=None, start_date=None, end_date=None, folder=folder)

        csv_file = data_analyser_provider.csv_file
        data = csv_file["data"]

        assert data["data da coleta"] == [
            fake_record.created_at.get_value()[:10] for fake_record in fake_records
        ]
        assert data["validade da adubação?"] == [
            fake_record.fertilizer_expiration_date.get_value()[:10]
            for fake_record in fake_records
        ]
        assert data["hora da coleta (inserir valor de 0 a 23)"] == [
            fake_record.created_at.get_time().hour for fake_record in fake_records
        ]
        assert data["umidade do ar?"] == [
            fake_record.air_humidity for fake_record in fake_records
        ]
        assert data["umidade do solo?"] == [
            fake_record.soil_humidity for fake_record in fake_records
        ]
        assert data["temperatura ambiente?"] == [
            fake_record.temperature for fake_record in fake_records
        ]
        assert data["consumo de água (mililitros)?"] == [
            fake_record.water_consumption for fake_record in fake_records
        ]
        assert data["luminosidade (lux)?"] == [
            fake_record.illuminance for fake_record in fake_records
        ]
        assert data["iaf (índice de área foliar)?"] == [
            fake_record.lai for fake_record in fake_records
        ]
        assert data["qual o aspecto das folhas?"] == [
            fake_record.leaf_appearance for fake_record in fake_records
        ]
        assert data["qual a coloração das folhas?"] == [
            fake_record.leaf_color for fake_record in fake_records
        ]
        assert data["em qual plantio você quer coletar os dados?"] == [
            fake_record.plantation_type for fake_record in fake_records
        ]
        assert data["algum desvio detectado durante o processo?"] == [
            fake_record.report for fake_record in fake_records
        ]
        assert data["planta"] == [
            fake_record.plant.name for fake_record in fake_records
        ]

    def it_should_create_csv_file_with_checklist_records_filtered_by_plant(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: GetChecklistRecordsCsvFile,
    ):
        fake_records = ChecklistRecordsFaker.fake_many(10)
        fake_plant = PlantsFaker.fake()

        fake_records.append(ChecklistRecordsFaker.fake(plant=fake_plant))
        fake_records.append(ChecklistRecordsFaker.fake(plant=fake_plant))
        fake_records.append(ChecklistRecordsFaker.fake(plant=fake_plant))

        checklist_records_repository.create_many_checklist_records(fake_records)

        use_case.execute(
            plant_id=fake_plant.id, start_date=None, end_date=None, folder=folder
        )

        csv_file = data_analyser_provider.csv_file
        data = csv_file["data"]

        assert len(data["planta"]) == 3
        assert data["planta"] == [fake_plant.name for _ in range(3)]

    def it_should_create_csv_file_with_checklist_records_filtered_by_date(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: GetChecklistRecordsCsvFile,
    ):
        fake_records = ChecklistRecordsFaker.fake_many(10)

        fake_records.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=12, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=25, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=30, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records.append(
            ChecklistRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=11, day=12, hour=0, minute=0, second=0)
                )
            )
        )

        checklist_records_repository.create_many_checklist_records(fake_records)

        use_case.execute(
            plant_id=None,
            start_date="2024-12-12",
            end_date="2024-12-30",
            folder=folder,
        )

        csv_file = data_analyser_provider.csv_file
        data = csv_file["data"]

        assert len(data["data da coleta"]) == 3
        assert data["data da coleta"] == ["12/12/2024", "25/12/2024", "30/12/2024"]
