from datetime import date

from pytest import raises

from core.commons.weekday import Weekday
from core.errors.validation import DateNotValidError


def describe_weekday_common():

    def it_should_throw_error_if_date_value_is_not_valid():
        with raises(DateNotValidError):
            Weekday("invalid date value")

    def it_should_get_value():
        sunday_date = date(
            year=2024,
            month=6,
            day=30,
        )
        monday_date = date(
            year=2024,
            month=7,
            day=1,
        )
        tuesday_date = date(
            year=2024,
            month=7,
            day=2,
        )
        wednesday_date = date(
            year=2024,
            month=7,
            day=3,
        )
        thursday_date = date(
            year=2024,
            month=7,
            day=4,
        )
        friday_date = date(
            year=2024,
            month=7,
            day=5,
        )
        saturday_date = date(
            year=2024,
            month=7,
            day=6,
        )

        weekday = Weekday(sunday_date)
        assert weekday.get_value() == "domingo"

        weekday = Weekday(monday_date)
        assert weekday.get_value() == "segunda"

        weekday = Weekday(tuesday_date)
        assert weekday.get_value() == "terça"

        weekday = Weekday(wednesday_date)
        assert weekday.get_value() == "quarta"

        weekday = Weekday(thursday_date)
        assert weekday.get_value() == "quinta"

        weekday = Weekday(friday_date)
        assert weekday.get_value() == "sexta"

        weekday = Weekday(saturday_date)
        assert weekday.get_value() == "sábado"
