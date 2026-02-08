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

        # Normalize empty strings and None to None
        if self.start_date == "" or self.start_date is None:
            self.start_date = None
        
        if self.end_date == "" or self.end_date is None:
            self.end_date = None

        try:
            # Only process if we have actual date strings
            if self.start_date is not None and isinstance(self.start_date, str):
                self.start_date = Date(self.start_date).get_value(is_date=True)

            if self.end_date is not None and isinstance(self.end_date, str):
                self.end_date = Date(self.end_date).get_value(is_date=True)
        except Exception:
            raise DateNotValidError()

        # If only start_date is provided, use it as end_date too
        if self.start_date and self.end_date is None:
            self.end_date = self.start_date
