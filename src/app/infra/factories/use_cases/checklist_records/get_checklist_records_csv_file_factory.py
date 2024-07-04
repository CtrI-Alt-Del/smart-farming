from core.use_cases.checklist_records import GetChecklistRecordsCsvFile

from infra.repositories import (
    sensors_records_repository,
)
from infra.providers.data_analyser_provider import DataAnalyserProvider


class GetChecklistRecordsCsvFileFactory:
    @staticmethod
    def produce():
        data_analyser_provider = DataAnalyserProvider()

        return GetChecklistRecordsCsvFile(
            sensors_records_repository=sensors_records_repository,
            data_analyser_provider=data_analyser_provider,
        )
