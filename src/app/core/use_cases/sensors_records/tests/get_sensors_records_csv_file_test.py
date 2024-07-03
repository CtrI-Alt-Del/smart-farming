from datetime import datetime

from pytest import fixture

from core.use_cases.tests.mocks.repositories import SensorRecordsRepositoryMock
from core.use_cases.tests.mocks.providers import DataAnalyserProviderMock
from core.entities.tests.fakers import SensorsRecordsFaker, PlantsFaker
from core.commons import Datetime
from core.constants import CSV_FILE_COLUMNS

from ..get_sensors_records_csv_file import GetSensorsRecordsCsvFile


def describe_get_sensors_records_csv_file_use_case():
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
        data_analyser_provider: DataAnalyserProviderMock,
        sensors_records_repository: SensorRecordsRepositoryMock,
    ):
        sensors_records_repository.clear_records()
        return GetSensorsRecordsCsvFile(
            sensors_records_repository=sensors_records_repository,
            data_analyser_provider=data_analyser_provider,
        )

    @fixture
    def folder():
        return "fake_csv_folder"

    def it_should_create_csv_file_in_a_specific_path(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: GetSensorsRecordsCsvFile,
    ):
        use_case.execute(plant_id=None, start_date=None, end_date=None, folder=folder)

        csv_file = data_analyser_provider.csv_file

        assert csv_file["path"] == f"{folder}/registros-dos-sensores.xlsx"

    def it_should_create_csv_file_with_empty_data_if_there_is_no_any_sensors_record_in_repository(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        use_case: GetSensorsRecordsCsvFile,
    ):
        use_case.execute(plant_id=None, start_date=None, end_date=None, folder=folder)

        csv_file = data_analyser_provider.csv_file

        for data in csv_file["data"].values():
            assert data == []

    def it_should_create_csv_file_containing_sensors_records(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: GetSensorsRecordsCsvFile,
    ):
        fake_records = SensorsRecordsFaker.fake_many()

        sensors_records_repository.create_many_sensors_records(fake_records)

        use_case.execute(plant_id=None, start_date=None, end_date=None, folder=folder)

        csv_file = data_analyser_provider.csv_file
        data = csv_file["data"]

        assert data["data"] == [
            fake_record.created_at.get_value()[:10] for fake_record in fake_records
        ]
        assert data["hora"] == [
            fake_record.created_at.get_time() for fake_record in fake_records
        ]
        assert data["umidade Ambiente"] == [
            fake_record.ambient_humidity for fake_record in fake_records
        ]
        assert data["umidade solo"] == [
            fake_record.soil_humidity for fake_record in fake_records
        ]
        assert data["temperatura"] == [
            fake_record.temperature for fake_record in fake_records
        ]
        assert data["volume de Água (ml)"] == [
            fake_record.water_volume for fake_record in fake_records
        ]
        assert data["dia da semana"] == [
            fake_record.weekday.get_value() for fake_record in fake_records
        ]
        assert data["planta"] == [
            fake_record.plant.name for fake_record in fake_records
        ]

    def it_should_create_csv_file_with_sensors_records_filtered_by_plant(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: GetSensorsRecordsCsvFile,
    ):
        fake_records = SensorsRecordsFaker.fake_many(10)
        fake_plant = PlantsFaker.fake()

        fake_records.append(SensorsRecordsFaker.fake(plant=fake_plant))
        fake_records.append(SensorsRecordsFaker.fake(plant=fake_plant))
        fake_records.append(SensorsRecordsFaker.fake(plant=fake_plant))

        sensors_records_repository.create_many_sensors_records(fake_records)

        use_case.execute(
            plant_id=fake_plant.id, start_date=None, end_date=None, folder=folder
        )

        csv_file = data_analyser_provider.csv_file
        data = csv_file["data"]

        assert len(data["planta"]) == 3
        assert data["planta"] == [fake_plant.name for _ in range(3)]

    def it_should_create_csv_file_with_sensors_records_filtered_by_date(
        folder: str,
        data_analyser_provider: DataAnalyserProviderMock,
        sensors_records_repository: SensorRecordsRepositoryMock,
        use_case: GetSensorsRecordsCsvFile,
    ):
        fake_records = SensorsRecordsFaker.fake_many(10)

        fake_records.append(
            SensorsRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=12, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records.append(
            SensorsRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=25, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records.append(
            SensorsRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=12, day=30, hour=0, minute=0, second=0)
                )
            )
        )
        fake_records.append(
            SensorsRecordsFaker.fake(
                created_at=Datetime(
                    datetime(year=2024, month=11, day=12, hour=0, minute=0, second=0)
                )
            )
        )

        sensors_records_repository.create_many_sensors_records(fake_records)

        use_case.execute(
            plant_id=None,
            start_date="2024-12-12",
            end_date="2024-12-30",
            folder=folder,
        )

        csv_file = data_analyser_provider.csv_file
        data = csv_file["data"]

        assert len(data["data"]) == 3
        assert data["data"] == ["12/12/2024", "25/12/2024", "30/12/2024"]
