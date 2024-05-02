from datetime import datetime, time


class Datetime:
    value: datetime

    def __init__(self, value: datetime):
        self.value = value

    def format_value(self):
        self.value = self.value.strftime("%d/%m/%Y %H:%M")
        return self

    def get_time(self) -> time:
        return time(
            hour=self.value.hour,
            minute=self.value.minute,
        )

    def get_value(self, is_datetime: bool = False) -> str:
        if is_datetime:
            return self.value

        return str(self.value)
