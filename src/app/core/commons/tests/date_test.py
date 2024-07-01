from datetime import date

from pytest import raises


from core.commons.date import Date
from core.errors.validation import DateNotValidError


def describe_date_common():

    def it_should_throw_error_if_it_could_not_convert_value_to_date():
        with raises(DateNotValidError):
            Date("invalid date value")

    def it_should_convert_value_to_date_if_it_is_not_date():
        assert Date("2024-12-10").get_value(is_date=True) == date(
            year=2024, month=12, day=10
        )

    def it_should_get_value_as_date():
        today = date.today()

        assert today == Date(today).get_value(is_date=True)

    def it_should_get_value_as_string():
        today = date.today()

        assert str(today) == Date(today).get_value(is_date=False)
