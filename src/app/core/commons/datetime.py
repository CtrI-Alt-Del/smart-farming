from datetime import datetime


class Datetime:
    value: datetime

    def __init__(self, value: datetime):
        self.value = value

    def format_value(self):
        self.value = self.value.strftime("%d/%m/%Y %H:%M:%S")
        return self

    def get_hour(self) -> int:
        return self.value.hour

    def get_value(self, is_datetime: bool = False) -> str:
        if is_datetime:
            return self.value

        return str(self.value)
