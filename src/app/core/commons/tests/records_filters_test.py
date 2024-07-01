from pytest import raises

from core.commons.records_filters import RecordsFilters
from core.errors.validation import DateNotValidError


def describe_records_filter_common():

    def it_should_throw_error_if_it_could_not_convert_start_date_value_to_date():
        with raises(DateNotValidError):
            RecordsFilters(plant_id=None, start_date="invalid date", end_date=None)

    def it_should_throw_error_if_it_could_not_convert_end_date_value_to_date():
        with raises(DateNotValidError):
            RecordsFilters(plant_id=None, start_date=None, end_date="invalid date")

    def it_should_set_plant_id_to_none_if_it_is_equal_to_all():
        filters = RecordsFilters(plant_id="all", start_date=None, end_date=None)

        assert filters.plant_id is None

    def it_should_set_end_date_to_start_date_if_start_date_is_valid_but_end_date_is_not():
        start_date = "2024-12-12"

        filters = RecordsFilters(plant_id=None, start_date=start_date, end_date=None)

        assert filters.end_date == start_date
