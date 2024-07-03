from core.use_cases.sensors_records import UpdateSensorsRecord

from infra.repositories import (
    plants_repository,
)
from infra.providers.data_analyser_provider import DataAnalyserProvider


class UpdateSensorsRecordFactory:
    @staticmethod
    def produce():
        data_analyser_provider = DataAnalyserProvider()

        return UpdateSensorsRecord(
            plants_repository=plants_repository,
            data_analyser_provider=data_analyser_provider,
        )
