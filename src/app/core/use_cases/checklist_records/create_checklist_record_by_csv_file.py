from typing import Generator
from datetime import datetime
from werkzeug.datastructures import FileStorage

from core.commons import CsvFile, Error, Datetime
from core.entities import CheckListRecord
from core.constants import CSV_FILE_COLUMNS

from infra.repositories import checklist_records_repository, plants_repository


class CreateChecklistRecordsByCsvFile:
    def execute(self, file: FileStorage) -> None:
        try:
            csv_file = CsvFile(file)
            csv_file.read()

            csv_file.validate_columns(CSV_FILE_COLUMNS["checklist_records"])

            records = csv_file.get_records()

            converted_records = self.__convert_csv_records_to_checklist_records(records)

            for checklist_record in converted_records:
                checklist_records_repository.create_checklist_record(checklist_record)

        except Error as error:
            raise error

    def __convert_csv_records_to_checklist_records(
        self, records: list[dict]
    ) -> Generator:
        plants = plants_repository.get_plants()

        for record in records:
            record_date = record["data da coleta"].date()
            record_hour = record["hora da coleta (inserir valor de 0 a 23)"]
            record_fertilizer_expiration_date = record["validade da adubação?"].date()
            record_plant_name = record["planta"]

            created_at = Datetime(
                value=datetime(
                    day=record_date.day,
                    month=record_date.month,
                    year=record_date.year,
                    hour=record_hour,
                )
            )

            fertilizer_expiration_date = Datetime(
                value=datetime(
                    day=record_fertilizer_expiration_date.day,
                    month=record_fertilizer_expiration_date.month,
                    year=record_fertilizer_expiration_date.year,
                )
            )

            plant = None

            for current_plant in plants:
                if current_plant.name.lower() == record_plant_name.lower():
                    plant = current_plant
                    break

            yield CheckListRecord(
                soil_ph=record["ph do solo?"],
                soil_humidity=record["umidade do solo?"],
                water_consumption=record["consumo de água (mililitros)?"],
                air_humidity=record["umidade do ar?"],
                temperature=record["temperatura ambiente?"],
                illuminance=record["luminosidade (lux)?"],
                lai=record["iaf (índice de área foliar)?"],
                leaf_appearance=record["qual o aspecto das folhas?"],
                leaf_color=record["qual a coloração das folhas?"],
                plantation_type=record["em qual plantio você quer coletar os dados?"],
                report=record["algum desvio detectado durante o processo?"],
                fertilizer_expiration_date=fertilizer_expiration_date,
                created_at=created_at,
                plant=plant,
            )
