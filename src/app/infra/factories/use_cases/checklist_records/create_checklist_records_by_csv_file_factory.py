from core.use_cases.checklist_records import CreateChecklistRecordsByCsvFile

from infra.repositories import plants_repository, checklist_records_repository
from infra.providers import DataAnalyserProvider


class CreateChecklistRecordsByCsvFileFactory:
    @staticmethod
    def produce():
        data_analyser_provider = DataAnalyserProvider()

        return CreateChecklistRecordsByCsvFile(
            plants_repository=plants_repository,
            checklist_records_repository=checklist_records_repository,
            data_analyser_provider=data_analyser_provider,
        )
