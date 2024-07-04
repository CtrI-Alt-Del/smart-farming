from dataclasses import dataclass
from datetime import date as date_value

from .entity import Entity


@dataclass
class LineChartRecord(Entity):
    date: date_value = None
    value: int = None
    plant_id: str = None
