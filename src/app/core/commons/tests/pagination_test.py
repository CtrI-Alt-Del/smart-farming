from pytest import raises

from core.commons.pagination import Pagination
from core.errors.validation import PageNumberNotValidError


def describe_pagination_common():
    def it_should_throw_error_if_page_number_records_count_are_not_integers():
        with raises(PageNumberNotValidError):
            Pagination(page_number=None, records_count=None)

    def it_should_get_the_current_and_last_page_numbers():
        pagination = Pagination(page_number=2, records_count=24)

        current_page_number, last_page_number = (
            pagination.get_current_and_last_page_numbers()
        )

        assert last_page_number == 4
        assert current_page_number == 2

    def it_should_ensure_the_page_number_does_not_exceed_the_max_of_possible_pages():
        pagination = Pagination(page_number=100, records_count=12)

        current_page_number, last_page_number = (
            pagination.get_current_and_last_page_numbers()
        )

        assert last_page_number == 2
        assert current_page_number == 2
