from datetime import date
from calendar import day_name

from core.constants import WEEKDAYS


class Weekday:
    def __init__(self, value: date):
        self.value = WEEKDAYS[day_name[value.weekday()].lower()]

    def get_value(self):
        return self.value
