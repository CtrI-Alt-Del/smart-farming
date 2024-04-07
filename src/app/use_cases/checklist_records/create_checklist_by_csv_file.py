from typing import List, Dict, Generator
from werkzeug.datastructures import FileStorage
from datetime import datetime

from commons.csv_file import CsvFile

from entities.checklist_record import CheckListRecord

from repositories import checklist_records_repository

from utils.error import Error

class CreateCheckListRecordsByCsvFile:
    def execute(self, file: FileStorage) -> None:
        try:
            csv_file = CsvFile(file)
            records = csv_file.get_records()

            converted_records = self.__convert_csv_records_to_checklist_records(records)

            for checklist_record in converted_records:
                checklist_records_repository.create_checklist_record(checklist_record)

        except Error as error:
            raise error
        
    def __convert_csv_records_to_checklist_records(
            self, records: List[Dict]
    ) -> Generator:
        for record in records:
            record_date = record["Data"].date()
            record_time = record["Hora"]
            
            yield CheckListRecord(
                soil_ph=["ph do solo"],
                soil_humidity=["umidade do solo"],
                water_consumption=["consumo de água"],
                air_humidity=["umidade do ar"],
                temperature=["temperatura"],
                illuminance=["iluminância"],
                lai=["lai"],
                leaf_apperance=["aparência da folha"],
                leaf_color=["cor da folha"],
                plantation_type=["tipo da plantação"],
                fertiliziation_date=datetime(
                    day=record_date.day,
                    month=record_date.month,
                    year=record_date.year,
                ),
                harvested_at=datetime(
                    day=record_date.day,
                    month=record_date.month,
                    year=record_date.year,
                    hour=record_time.hour,
                    minute=record_time.minute,
                report=["relatório"],
                ),
            )