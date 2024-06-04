from random import randint
from datetime import date

from core.commons import RecordsFilters, Error

from infra.repositories import checklist_records_repository
from infra.constants import FOLDERS
from infra.providers.data_analyser_provider import DataAnalyserProvider


class GetChecklistRecordsCsvFile:
    def execute(self, plant_id: str, start_date: date, end_date: date):
        try:
            filters = RecordsFilters(
                plant_id=plant_id, start_date=start_date, end_date=end_date
            )

            checklist_records = (
                checklist_records_repository.get_filtered_checklist_records(
                    page_number="all",
                    plant_id=filters.plant_id,
                    start_date=filters.start_date,
                    end_date=filters.end_date,
                )
            )

            csv_name = f"checklist-records-{randint(1, 100)}.xlsx"
            tmp_folder = FOLDERS["tmp"]

            data_analyser_provider = DataAnalyserProvider()
            data_analyser_provider.analyse(checklist_records)
            data_analyser_provider.convert_to_excel(tmp_folder, csv_name)

            return {
                "folder": tmp_folder,
                "filename": csv_name,
            }
        except Error as error:
            raise error
