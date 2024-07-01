from datetime import datetime, time

from core.errors.validation import DatetimeValueNotValidError


class Datetime:
    value: datetime

    def __init__(self, value: datetime):
        if not isinstance(value, datetime):
            raise DatetimeValueNotValidError()
        
        self.value = value

    def format_value(self):
        self.value = self.value.strftime("%d/%m/%Y %H:%M")
        return self

    def get_time(self):
        return time(
            hour=self.value.hour,
            minute=self.value.minute,
        )

    def get_value(self, is_datetime: bool = False):
        if is_datetime:
            return self.value

        return str(self.value)
