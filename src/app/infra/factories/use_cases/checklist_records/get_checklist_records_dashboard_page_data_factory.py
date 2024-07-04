from core.use_cases.checklist_records import GetChecklistRecordsDashboardPageData

from infra.repositories import (
    plants_repository,
    users_repository,
    checklist_records_repository,
)


class GetChecklistRecordsDashboardPageDataFactory:
    @staticmethod
    def produce():
        return GetChecklistRecordsDashboardPageData(
            plants_repository=plants_repository,
            users_repository=users_repository,
            checklist_records_repository=checklist_records_repository,
        )
