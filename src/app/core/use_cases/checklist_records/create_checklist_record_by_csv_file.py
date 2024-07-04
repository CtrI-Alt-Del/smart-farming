from typing import Generator
from datetime import datetime, date
from werkzeug.datastructures import FileStorage

from core.commons import CsvFile, Datetime
from core.entities import CheckListRecord
from core.interfaces.repositories import (
    ChecklistRecordsRepositoryInterface,
    PlantsRepositoryInterface,
)
from core.errors.validation import DatetimeNotValidError, HourNotValidError
from core.errors.plants import PlantNotFoundError
from core.interfaces.providers import DataAnalyserProviderInterface
from core.constants import CSV_FILE_COLUMNS


class CreateChecklistRecordsByCsvFile:
    def __init__(
        self,
        checklist_records_repository: ChecklistRecordsRepositoryInterface,
        plants_repository: PlantsRepositoryInterface,
        data_analyser_provider: DataAnalyserProviderInterface,
    ):
        self._checklist_records_repository = checklist_records_repository
        self._plants_repository = plants_repository
        self._data_analyser_provider = data_analyser_provider

    def execute(self, file: FileStorage) -> None:
        csv_file = CsvFile(file, self._data_analyser_provider)
        csv_file.read()

        csv_file.validate_columns(CSV_FILE_COLUMNS["checklist_records"])

        records = csv_file.get_records()

        converted_records = self.__convert_csv_records_to_checklist_records(records)

        self._checklist_records_repository.create_many_checklist_records(
            converted_records
        )

    def __convert_csv_records_to_checklist_records(
        self, records: list[dict]
    ) -> Generator:
        plants = self._plants_repository.get_plants()

        for record in records:
            try:
                if not isinstance(record["data da coleta"], date):
                    record_date = datetime.strptime(
                        record["data da coleta"], "%d/%m/%Y"
                    ).date()
                else:
                    record_date = record["data da coleta"].date()

                if not isinstance(record["validade da adubação?"], date):
                    record_fertilizer_expiration_date = datetime.strptime(
                        record["validade da adubação?"], "%d/%m/%Y"
                    ).date()
                else:
                    record_fertilizer_expiration_date = record[
                        "validade da adubação?"
                    ].date()
            except Exception:
                raise DatetimeNotValidError()

            record_hour = record["hora da coleta (inserir valor de 0 a 23)"]

            try:
                if (
                    not isinstance(record_hour, int)
                    or record_hour < 0
                    or record_hour > 23
                ):
                    record_hour = int(record_hour)
            except Exception:
                raise HourNotValidError(
                    ui_message="Valor da hora precisa ser um número entre 0 e 23"
                )

            if record_hour < 0 or record_hour > 23:
                raise HourNotValidError(
                    ui_message="Valor da hora precisa ser um número entre 0 e 23"
                )

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

            if plant is None:
                raise PlantNotFoundError(
                    f"Planta não encontrada para o registro da data {created_at.format_value().get_value()}"
                )

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
