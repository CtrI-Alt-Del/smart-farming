from core.use_cases.sensors_records import CreateSensorsRecordsByCsvFile

from infra.repositories import (
    plants_repository,
    sensors_records_repository,
)
from infra.providers import DataAnalyserProvider


class CreateSensorsRecordsByCsvFileFactory:
    @staticmethod
    def produce():
        data_analyser_provider = DataAnalyserProvider()

        return CreateSensorsRecordsByCsvFile(
            plants_repository=plants_repository,
            sensors_records_repository=sensors_records_repository,
            data_analyser_provider=data_analyser_provider,
        )
