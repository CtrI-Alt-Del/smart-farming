from typing import List, Dict, Generator
from werkzeug.datastructures import FileStorage

from core.commons.csv_file import CsvFile
from core.commons.error import Error
from app.core.entities.plant import PlantsRecord
from core.constants.csv_file_columns import CSV_FILE_COLUMNS

from infra.repositories import plants_records_repository


class CreatePlantsRecordsByCsvFile:
    def execute(self, file: FileStorage) -> None:
        try:
            csv_file = CsvFile(file)
            csv_file.read()

            csv_file.validate_columns(CSV_FILE_COLUMNS["plants_records"])

            records = csv_file.get_records()

            converted_records = self.__convert_csv_records_to_plants_records(records)

            for plants_record in converted_records:
                plants_records_repository.create_plants_record(plants_record)

        except Error as error:
            raise error

    def __convert_csv_records_to_plants_records(self, records: List[Dict]) -> Generator:
        for record in records:
            yield PlantsRecord(
                name=record["name"],
                hex_color=record["hex_color"],
            )
