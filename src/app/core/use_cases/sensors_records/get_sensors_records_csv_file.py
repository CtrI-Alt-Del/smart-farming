from datetime import date

from core.commons import RecordsFilters
from core.constants import CSV_FILE_COLUMNS

from core.interfaces.repositories import SensorRecordsRepositoryInterface
from core.interfaces.providers import DataAnalyserProviderInterface


class GetSensorsRecordsCsvFile:
    def __init__(
        self,
        sensors_records_repository: SensorRecordsRepositoryInterface,
        data_analyser_provider: DataAnalyserProviderInterface,
    ):
        self._data_analyser_provider = data_analyser_provider
        self._sensors_records_repository = sensors_records_repository

    def execute(self, plant_id: str, start_date: date, end_date: date, folder: str):
        try:
            filters = RecordsFilters(
                plant_id=plant_id, start_date=start_date, end_date=end_date
            )

            data = self.__get_data(filters)

            csv_filename = "registros-dos-sensores.xlsx"

            self._data_analyser_provider.analyse(data)
            self._data_analyser_provider.convert_to_excel(folder, csv_filename)

            return csv_filename
        except Exception as error:
            print(error, flush=True)

    def __get_data(self, filters: RecordsFilters):
        sensors_records = self._sensors_records_repository.get_filtered_sensors_records(
            page_number="all",
            plant_id=filters.plant_id,
            start_date=filters.start_date,
            end_date=filters.end_date,
        )

        columns = CSV_FILE_COLUMNS["sensors_records"]
        data = {column: [] for column in columns}

        print(sensors_records, flush=True)

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
                        data["data"].append(value.format_value().get_value()[:10])
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
