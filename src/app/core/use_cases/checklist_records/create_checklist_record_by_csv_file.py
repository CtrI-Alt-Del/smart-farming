from typing import List, Dict, Generator
from werkzeug.datastructures import FileStorage
from datetime import datetime

from core.commons import CsvFile, Error, Datetime
from core.entities import CheckListRecord

from infra.repositories import checklist_records_repository


class CreateChecklistRecordsByCsvFile:
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

            fertilizer_expiration_date = Datetime(
                value=datetime(
                    day=record_date.day,
                    month=record_date.month,
                    year=record_date.year,
                )
            )

            created_at = Datetime(
                value=datetime(
                    day=record_date.day,
                    month=record_date.month,
                    year=record_date.year,
                    hour=record_time.hour,
                    minute=record_time.minute,
                )
            )

            yield CheckListRecord(
                soil_ph=record["ph do solo"],
                soil_humidity=record["umidade do solo"],
                water_consumption=record["consumo de água"],
                air_humidity=record["umidade do ar"],
                temperature=record["temperatura"],
                illuminance=record["iluminância"],
                lai=record["lai"],
                leaf_appearance=record["aparência da folha"],
                leaf_color=record["cor da folha"],
                plantation_type=record["tipo da plantação"],
                report=record["relatório"],
                fertilizer_expiration_date=fertilizer_expiration_date,
                created_at=created_at,
            )
