from typing import List, Dict, Generator
from werkzeug.datastructures import FileStorage
from datetime import datetime

from core.commons.csv_file import CsvFile
from core.commons.error import Error
from core.entities.sensors_record import SensorsRecord
from core.constants.csv_file_columns import CSV_FILE_COLUMNS

from infra.repositories import sensors_records_repository


class CreateSensorsRecordsByCsvFile:
    def execute(self, file: FileStorage) -> None:
        try:
            csv_file = CsvFile(file)
            csv_file.read()

            has_valid_columns = csv_file.validate_columns(
                CSV_FILE_COLUMNS["sensors_records"]
            )

            if not has_valid_columns:
                raise Error("As colunas não estão corretas")

            records = csv_file.get_records()

            converted_records = self.__convert_csv_records_to_sensors_records(records)

            for sensors_record in converted_records:
                sensors_records_repository.create_sensors_record(sensors_record)

        except Error as error:
            raise error

    def __convert_csv_records_to_sensors_records(
        self, records: List[Dict]
    ) -> Generator:
        for record in records:
            record_date = record["Data"].date()
            record_time = record["Hora"]

            yield SensorsRecord(
                ambient_humidity=record["Umidade Ambiente"],
                soil_humidity=record["Umidade solo"],
                temperature=record["Temperatura"],
                water_volume=record["Volume Água (L)"],
                created_at=datetime(
                    day=record_date.day,
                    month=record_date.month,
                    year=record_date.year,
                    hour=record_time.hour,
                    minute=record_time.minute,
                ),
            )
