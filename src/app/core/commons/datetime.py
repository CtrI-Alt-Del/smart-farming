from datetime import datetime


class Datetime:
    def __init__(self, value: datetime):
        self.value = value

    def format_value(self):
        self.value = self.value.strftime("%d/%m/%Y %H:%M:%S")
        return self

    def get_value(self) -> str:
        return str(self.value)
