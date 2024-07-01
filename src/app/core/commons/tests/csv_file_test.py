from pathlib import Path
from werkzeug.datastructures import FileStorage

from pytest import fixture, raises, mark

from core.commons.csv_file import CsvFile
from core.errors.validation import CSVFileNotValidError, CSVColumnsNotValidError
from core.use_cases.tests.mocks.providers import DataAnalyserProviderMock


def describe_csv_file_common():
    @fixture
    def file(tmp_path: Path):
        return FileStorage(tmp_path / "fake_csv_.xlsx")

    @fixture
    def data_analyser_provider():
        return DataAnalyserProviderMock()

    @fixture
    def csv_file(file, data_analyser_provider):
        return CsvFile(file, data_analyser_provider)

    def it_should_throw_error_if_file_is_not_valid(
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        with raises(CSVFileNotValidError):
            CsvFile(None, data_analyser_provider)

    def it_should_throw_error_if_file_does_not_have_valid_extension(
        tmp_path: Path,
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        fake_file = FileStorage(tmp_path / "fake_csv.invalid_extension")

        csv_file = CsvFile(fake_file, data_analyser_provider)

        with raises(CSVFileNotValidError):
            csv_file.read()

    def it_should_read_file_as_excel_file(
        tmp_path,
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        fake_file = FileStorage(tmp_path / "fake_csv.xlsx")

        csv_file = CsvFile(fake_file, data_analyser_provider)

        csv_file.read()

        file_data = data_analyser_provider.get_data()

        assert file_data == "excel file data"

    @mark.parametrize("extension", ["csv", "txt"])
    def it_should_read_file_as_csv_text_file(
        tmp_path: Path,
        extension,
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        fake_file = FileStorage(tmp_path / f"fake_csv.{extension}")

        csv_file = CsvFile(fake_file, data_analyser_provider)

        csv_file.read()

        file_data = data_analyser_provider.get_data()

        assert file_data == "csv text file data"

    def it_should_throw_error_if_at_least_one_invalid_column_is_found(
        csv_file: CsvFile,
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        csv_file.read()

        fake_columns = ["column 1", "column 2", "column 3"]

        data_analyser_provider.get_columns = lambda: fake_columns

        csv_file.validate_columns(fake_columns)

        with raises(CSVColumnsNotValidError):
            csv_file.validate_columns(["column 1", "column 2", "column 4"])

    def it_should_get_records_with_key_of_each_of_them_as_lowercase(
        csv_file: CsvFile,
        data_analyser_provider: DataAnalyserProviderMock,
    ):
        csv_file.read()

        data_analyser_provider.convert_to_list_of_records = lambda: [
            {"KEY 1": "value", "KEY 2": "value", "KEY 3": "value"}
        ]

        records = csv_file.get_records()

        keys = []

        for record in records:
            keys.extend(record.keys())

        assert keys == ["key 1", "key 2", "key 3"]
