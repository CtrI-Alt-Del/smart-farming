from dataclasses import dataclass
from datetime import datetime

from core.entities.entity import Entity


@dataclass
class SensorsRecord(Entity):
    soil_humidity: int = None
    ambient_humidity: int = None
    temperature: int = None
    water_volume: int = None
    created_at: datetime = None
