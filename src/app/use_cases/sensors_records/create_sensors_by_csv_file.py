from typing import List, Dict, Generator
from werkzeug.datastructures import FileStorage
from datetime import datetime

from common.csv_file import CsvFile

from entities.sensors_record import SensorsRecord

from repositories import sensors_records_repository

from utils.error import Error


class CreateSensorsRecordsByCsvFile:
    def execute(self, file: FileStorage) -> None:
        try:
            csv_file = CsvFile(file)
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
