from dataclasses import dataclass

from .entity import Entity
from .plant import Plant
from core.commons.datetime import Datetime
from core.commons.weekday import Weekday


@dataclass
class SensorsRecord(Entity):
    soil_humidity: int = None
    ambient_humidity: int = None
    water_volume: float = None
    temperature: float = None
    created_at: Datetime = None
    plant: Plant = None
    weekday: Weekday = None
