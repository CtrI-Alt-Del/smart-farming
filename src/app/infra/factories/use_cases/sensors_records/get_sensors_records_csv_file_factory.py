from core.use_cases.sensors_records import GetSensorsRecordsCsvFile

from infra.repositories import (
    sensors_records_repository,
)
from infra.providers.data_analyser_provider import DataAnalyserProvider


class GetSensorsRecordsCsvFileFactory:
    @staticmethod
    def produce():
        data_analyser_provider = DataAnalyserProvider()

        return GetSensorsRecordsCsvFile(
            sensors_records_repository=sensors_records_repository,
            data_analyser_provider=data_analyser_provider,
        )
