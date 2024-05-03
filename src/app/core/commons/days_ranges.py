from core.constants import DAYS_RANGES


class DaysRange:
    def __init__(self) -> None:
        self.value = [
            (f"{days_range} days", f"{days_range} dias") for days_range in DAYS_RANGES
        ]

    def get_value(self):
        return self.value
