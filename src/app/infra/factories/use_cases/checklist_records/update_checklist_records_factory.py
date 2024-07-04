from core.use_cases.checklist_records import UpdateChecklistRecord

from infra.repositories import (
    plants_repository,
)
from infra.providers.data_analyser_provider import DataAnalyserProvider


class UpdateChecklistRecordFactory:
    @staticmethod
    def produce():
        data_analyser_provider = DataAnalyserProvider()

        return UpdateChecklistRecord(
            plants_repository=plants_repository,
            data_analyser_provider=data_analyser_provider,
        )
