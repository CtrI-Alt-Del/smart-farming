from core.commons import Date
from core.errors.validation import DateNotValidError


class RecordsFilters:
    def __init__(
        self,
        start_date: str,
        end_date: str,
        plant_id: str,
    ) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.plant_id = plant_id

        self.__handle_filters()

    def __handle_filters(self):
        if self.plant_id == "all":
            self.plant_id = None

        try:
            if self.start_date != "" and isinstance(self.start_date, str):
                self.start_date = Date(self.start_date).get_value()

            if self.end_date != "" and isinstance(self.end_date, str):
                self.end_date = Date(self.end_date).get_value()
        except Exception:
            raise DateNotValidError()

        if self.start_date and (self.end_date is None or self.end_date == ""):
            self.end_date = self.start_date
