from datetime import datetime, date

from typing import List, Dict, Generator
from werkzeug.datastructures import FileStorage

from core.commons import CsvFile, Error, Datetime
from core.interfaces.repositories import (
    SensorRecordsRepositoryInterface,
    PlantsRepositoryInterface,
)
from core.entities.sensors_record import SensorsRecord
from core.constants import CSV_FILE_COLUMNS


class CreateSensorsRecordsByCsvFile:
    def __init__(
        self,
        sensors_records_repository: SensorRecordsRepositoryInterface,
        plants_repository: PlantsRepositoryInterface,
    ):
        self._sensors_records_repository = sensors_records_repository
        self._plants_repository = plants_repository

    def execute(self, file: FileStorage):
        try:
            csv_file = CsvFile(file)
            csv_file.read()

            csv_file.validate_columns(CSV_FILE_COLUMNS["sensors_records"])

            records = csv_file.get_records()

            converted_records = self.__convert_csv_records_to_sensors_records(records)

            self._sensors_records_repository.create_many_sensors_records(
                converted_records
            )

        except Error as error:
            raise error

    def __convert_csv_records_to_sensors_records(
        self, records: List[Dict]
    ) -> Generator:
        plants = self._plants_repository.get_plants()

        for record in records:
            try:
                if not isinstance(record["data"], date):
                    record_date = datetime.strptime(
                        str(record["data"]), "%d/%m/%Y"
                    ).date()
                else:
                    record_date = record["data"].date()

                if not isinstance(record["hora"], datetime):
                    record_time = datetime.strptime(str(record["hora"]), "%H:%M:%S")
                else:
                    record_time = record["hora"]

            except Exception as exception:
                raise Error(
                    internal_message=exception,
                    ui_message="Valor de data ou hora mal formatado",
                    status_code=400,
                )

            record_plant_name = record["planta"]

            created_at = Datetime(
                value=datetime(
                    day=record_date.day,
                    month=record_date.month,
                    year=record_date.year,
                    hour=record_time.hour,
                    minute=record_time.minute,
                )
            )

            plant = None

            for current_plant in plants:
                if current_plant.name.lower() == record_plant_name.lower():
                    plant = current_plant
                    break

            yield SensorsRecord(
                ambient_humidity=record["umidade ambiente"],
                soil_humidity=record["umidade solo"],
                temperature=record["temperatura"],
                water_volume=record["volume de água (ml)"],
                created_at=created_at,
                plant=plant,
            )
