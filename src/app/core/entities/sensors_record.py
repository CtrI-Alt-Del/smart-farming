from dataclasses import dataclass
from datetime import datetime

from core.entities.entity import Entity
from core.commons.datetime import Datetime


@dataclass
class SensorsRecord(Entity):
    soil_humidity: int = None
    ambient_humidity: int = None
    temperature: int = None
    water_volume: int = None
    created_at: datetime = None
    
    def __post_init__(self) -> None:
        if self.created_at is not None:
            datetime_formatter = Datetime(self.created_at)
            self.created_at = datetime_formatter.get_value()