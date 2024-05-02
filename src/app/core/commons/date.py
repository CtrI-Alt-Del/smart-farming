from datetime import date


class Date:
    def __init__(self, value: date):
        self.value = value

    def format_value(self):
        self.value = self.value.strftime("%d/%m/%Y")
        return self

    def get_value(self, is_date: bool = False) -> str:
        if is_date:
            return self.value

        return str(self.value)
