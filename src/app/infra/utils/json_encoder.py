import json
from decimal import Decimal


class JSONEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, Decimal):
            return float(value)
        return super().default(value)
