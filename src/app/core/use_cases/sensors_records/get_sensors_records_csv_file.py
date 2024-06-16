from datetime import date, datetime

from core.commons import RecordsFilters, Error
from core.constants import CSV_FILE_COLUMNS

from infra.repositories import sensors_records_repository
from infra.constants import FOLDERS
from infra.providers.data_analyser_provider import DataAnalyserProvider


class GetSensorsRecordsCsvFile:
    def execute(self, plant_id: str, start_date: date, end_date: date):
        try:
            filters = RecordsFilters(
                plant_id=plant_id, start_date=start_date, end_date=end_date
            )

            data = self.__get_data(filters)

            csv_name = "registros-dos-sensores.xlsx"
            tmp_folder = FOLDERS["tmp"]

            data_analyser_provider = DataAnalyserProvider()
            data_analyser_provider.analyse(data)
            data_analyser_provider.convert_to_excel(tmp_folder, csv_name)

            return {
                "folder": tmp_folder,
                "filename": csv_name,
            }
        except Error as error:
            raise error

    def __get_data(self, filters: RecordsFilters):
        sensors_records = sensors_records_repository.get_filtered_sensors_records(
            page_number="all",
            plant_id=filters.plant_id,
            start_date=filters.start_date,
            end_date=filters.end_date,
        )

        columns = CSV_FILE_COLUMNS["sensors_records"]
        data = {column: [] for column in columns}

        if len(sensors_records) == 0:
            return data

        attributes = sensors_records[0].__dict__.keys()

        for record in sensors_records:
            for attribute in attributes:
                value = getattr(record, attribute)

                match attribute:
                    case "plant":
                        data["planta"].append(value.name)
                    case "created_at":
                        data["hora"].append(value.get_time())
                        data["data"].append(
                            datetime.strptime(
                                value.format_value().get_value()[:10], "%d/%m/%Y"
                            ).date()
                        )
                    case "weekday":
                        data["dia da semana"].append(value.get_value())
                    case "soil_humidity":
                        data["umidade solo"].append(value)
                    case "ambient_humidity":
                        data["umidade Ambiente"].append(value)
                    case "water_volume":
                        data["volume de Água (ml)"].append(value)
                    case "temperature":
                        data["temperatura"].append(value)
        return data
