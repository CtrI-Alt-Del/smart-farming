from pytest import fixture, raises

from core.use_cases.tests.mocks.repositories import ChecklistRecordsRepositoryMock
from core.errors.checklist_records import ChecklistRecordNotFoundError
from core.errors.validation import ChecklistRecordNotValidError
from core.entities.tests.fakers import ChecklistRecordsFaker

from core.use_cases.checklist_records import DeleteChecklistRecords


def describe_delete_checklist_records_use_case():
    @fixture
    def checklist_records_repository():
        return ChecklistRecordsRepositoryMock()

    @fixture
    def use_case(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
    ):
        checklist_records_repository.clear_records()
        return DeleteChecklistRecords(
            checklist_records_repository=checklist_records_repository,
        )

    def it_should_throw_error_if_at_least_one_checklist_record_id_is_not_valid(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: DeleteChecklistRecords,
    ):
        fake_records = ChecklistRecordsFaker.fake_many(3)
        checklist_records_repository.create_many_checklist_records(fake_records)

        ids = [fake_record.id for fake_record in fake_records]

        ids.append(42)

        with raises(ChecklistRecordNotValidError):
            use_case.execute(ids)

    def it_should_throw_error_if_at_least_one_checklist_record_is_not_found(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: DeleteChecklistRecords,
    ):
        fake_records = ChecklistRecordsFaker.fake_many(3)
        checklist_records_repository.create_many_checklist_records(fake_records[:2])

        with raises(ChecklistRecordNotFoundError):
            use_case.execute([fake_record.id for fake_record in fake_records])

    def it_should_delete_many_records(
        checklist_records_repository: ChecklistRecordsRepositoryMock,
        use_case: DeleteChecklistRecords,
    ):
        count = 3
        fake_records = ChecklistRecordsFaker.fake_many(count)

        checklist_records_repository.create_many_checklist_records(fake_records)

        use_case.execute([fake_record.id for fake_record in fake_records])

        records = checklist_records_repository.get_last_checklist_records(count=count)

        assert len(records) == 0
