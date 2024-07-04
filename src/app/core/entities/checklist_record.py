from dataclasses import dataclass

from .entity import Entity
from .plant import Plant
from core.commons.datetime import Datetime
from core.commons.date import Date


@dataclass
class CheckListRecord(Entity):
    soil_ph: int = None
    water_consumption: int = None
    air_humidity: int = None
    soil_humidity: int = None
    lai: float = None
    temperature: float = None
    illuminance: float = None
    leaf_appearance: str = None
    leaf_color: str = None
    plantation_type: str = None
    report: str = None
    fertilizer_expiration_date: Date = None
    created_at: Datetime = None
    plant: Plant = None
