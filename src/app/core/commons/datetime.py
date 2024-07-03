from datetime import datetime, time

from core.errors.validation import DatetimeNotValidError


class Datetime:
    value: datetime

    def __init__(self, value: datetime):
        if not isinstance(value, datetime):
            raise DatetimeNotValidError()

        self.value = value

    def format_value(self):
        if isinstance(self.value, datetime):
            self.value = self.value.strftime("%d/%m/%Y %H:%M")

        return self

    def get_time(self):
        if isinstance(self.value, str):
            return datetime.strptime(self.value, "%d/%m/%Y %H:%M").time()

        return time(
            hour=self.value.hour,
            minute=self.value.minute,
        )

    def get_value(self, is_datetime: bool = False):
        if is_datetime:
            return self.value

        return str(self.value)
