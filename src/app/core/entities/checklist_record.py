from dataclasses import dataclass

from core.entities.entity import Entity
from core.entities.plant import Plant
from core.commons.datetime import Datetime
from core.commons.date import Date


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
    fertilizer_expiration_date: Date = None
    created_at: Datetime = None
    report: str = None
    plant: Plant = None
