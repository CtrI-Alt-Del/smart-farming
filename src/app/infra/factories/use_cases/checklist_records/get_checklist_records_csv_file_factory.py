from core.use_cases.checklist_records import GetChecklistRecordsCsvFile

from infra.repositories import (
    checklist_records_repository,
)
from infra.providers.data_analyser_provider import DataAnalyserProvider


class GetChecklistRecordsCsvFileFactory:
    @staticmethod
    def produce():
        data_analyser_provider = DataAnalyserProvider()

        return GetChecklistRecordsCsvFile(
            checklist_records_repository=checklist_records_repository,
            data_analyser_provider=data_analyser_provider,
        )
