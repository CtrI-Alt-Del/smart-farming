from math import ceil

from core.constants import PAGINATION


class Pagination:
    def __init__(self, page_number: int, records_count: int):
        self.page_number = page_number
        self.records_count = records_count

    def get_current_and_last_page_numbers(self):
        last_page_number = ceil(self.records_count / PAGINATION["records_per_page"])

        if last_page_number > 0 and self.page_number > last_page_number:
            current_page_number = last_page_number
        else:
            current_page_number = self.page_number

        return current_page_number, last_page_number
