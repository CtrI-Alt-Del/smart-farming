from dataclasses import dataclass
from datetime import datetime, date

from core.entities.entity import Entity


@dataclass
class CheckListRecord(Entity):
    soil_ph: int = None
    soil_humidity: int = None
    water_consumption: int = None
    air_humidity: int = None
    temperature: int = None
    illuminance: int = None
    lai: int = None
    leaf_apperance: str = None
    leaf_color: str = None
    plantation_type: str = None
    fertiliziation_date: date = None
    harvested_at: datetime = None
    report: str = None
