from datetime import datetime, time

from pytest import raises


from core.commons.datetime import Datetime
from core.errors.validation import DatetimeValueNotValidError


def describe_datetime_common():

    def it_should_throw_error_if_value_is_not_valid():
        with raises(DatetimeValueNotValidError):
            Datetime("data")

    def it_should_get_value_as_datetime():
        currente_datetime = datetime.now()

        assert currente_datetime == Datetime(currente_datetime).get_value(
            is_datetime=True
        )

    def it_should_get_value_datetime_as_string():
        currente_datetime = datetime.now()

        assert str(currente_datetime) == Datetime(currente_datetime).get_value(
            is_datetime=False
        )

    def it_should_get_value():
        hour = 12
        minute = 24
        year = 2024
        month = 12
        day = 16

        currente_datetime = datetime(
            hour=hour, minute=minute, year=year, month=month, day=day
        )

        value = Datetime(currente_datetime).format_value().get_value()

        assert f"{day}/{month}/{year} {hour}:{minute}" == value

    def it_should_get_time():
        hour = 12
        minute = 40

        currente_datetime = datetime(
            hour=hour, minute=minute, year=2024, month=3, day=16
        )

        assert time(hour=hour, minute=minute) == Datetime(currente_datetime).get_time()
