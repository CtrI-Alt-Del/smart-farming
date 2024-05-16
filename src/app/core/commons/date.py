from datetime import date, datetime

from core.commons import Error


class Date:
    value: date = None

    def __init__(self, value: date):
        try:
            if not isinstance(value, date):
                self.value = self.__confert_to_date(value)
                return

            self.value = value
        except:
            raise Error("Valor de data inválido")

    def format_value(self):
        self.value = self.value.strftime("%d/%m/%Y")
        return self

    def get_value(self, is_date: bool = False) -> str:
        if is_date:
            return self.value

        return str(self.value)

    def __confert_to_date(self, value):
        return datetime.strptime(value, "%Y-%m-%d").date()
