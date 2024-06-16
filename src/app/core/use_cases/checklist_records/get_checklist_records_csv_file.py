from datetime import date, datetime

from core.commons import RecordsFilters, Error
from core.constants import CSV_FILE_COLUMNS

from infra.repositories import checklist_records_repository
from infra.constants import FOLDERS
from infra.providers.data_analyser_provider import DataAnalyserProvider


class GetChecklistRecordsCsvFile:
    def execute(self, plant_id: str, start_date: date, end_date: date):
        try:
            filters = RecordsFilters(
                plant_id=plant_id, start_date=start_date, end_date=end_date
            )

            data = self.__get_data(filters)

            csv_name = "registros-checklist.xlsx"
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
        checklist_records = checklist_records_repository.get_filtered_checklist_records(
            page_number="all",
            plant_id=filters.plant_id,
            start_date=filters.start_date,
            end_date=filters.end_date,
        )

        columns = CSV_FILE_COLUMNS["checklist_records"]
        data = {column: [] for column in columns}

        if len(checklist_records) == 0:
            return data

        attributes = checklist_records[0].__dict__.keys()

        for record in checklist_records:
            for attribute in attributes:
                value = getattr(record, attribute)

                match attribute:
                    case "plant":
                        data["planta"].append(value.name)
                    case "created_at":
                        data["hora da coleta (inserir valor de 0 a 23)"].append(
                            value.get_time(is_datetime=True)
                        )
                        data["data da coleta"].append(
                            datetime.strptime(
                                value.format_value().get_value()[:10], "%d/%m/%Y"
                            ).date()
                        )
                    case "fertilizer_expiration_date":
                        data["validade da adubação?"].append(
                            datetime.strptime(
                                value.format_value().get_value()[:10], "%d/%m/%Y"
                            ).date()
                        )
                    case "soil_ph":
                        data["ph do solo?"].append(value)
                    case "soil_humidity":
                        data["umidade do solo?"].append(value)
                    case "air_humidity":
                        data["umidade do ar?"].append(value)
                    case "temperature":
                        data["temperatura ambiente?"].append(value)
                    case "water_consumption":
                        data["consumo de água (mililitros)?"].append(value)
                    case "illuminance":
                        data["luminosidade (lux)?"].append(value)
                    case "lai":
                        data["iaf (índice de área foliar)?"].append(value)
                    case "leaf_appearance":
                        data["qual o aspecto das folhas?"].append(value)
                    case "leaf_appearance":
                        data["qual o aspecto das folhas?"].append(value)
                    case "leaf_color":
                        data["qual a coloração das folhas?"].append(value)
                    case "plantation_type":
                        data["em qual plantio você quer coletar os dados?"].append(
                            value
                        )
                    case "report":
                        data["algum desvio detectado durante o processo?"].append(value)

        return data
