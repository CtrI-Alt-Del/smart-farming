from datetime import date
from calendar import day_name

from core.constants import WEEKDAYS

from core.errors.validation import DateNotValidError


class Weekday:
    def __init__(self, value: date):
        if not isinstance(value, date):
            raise DateNotValidError()

        self.value = WEEKDAYS[day_name[value.weekday()].lower()]

    def get_value(self):
        return self.value
