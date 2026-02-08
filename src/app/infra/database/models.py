from sqlalchemy import (
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    text,
)

from .extensions import db

DEFAULT_PLANT_ID = "4544afe3-0661-11ef-9512-0242ac140002"

LEAF_APPEARANCE_VALUES = (
    "SAUDAVEL",
    "MURCHA",
    "NÃO REGISTRADO",
)

LEAF_COLOR_VALUES = (
    "VERDE CLARO PREDOMINANTE",
    "VERDE ESCURO PREDOMINANTE",
    "VERDE CLARO COM ALGUMAS MANCHAS CLARAS",
    "VERDE CLARO COM VARIAS MANCHAS CLARAS",
    "VERDE CLARO COM ALGUMAS MANCHAS ESCURAS",
    "VERDE CLARO COM VARIAS MANCHAS ESCURAS",
    "VERDE ESCURO COM ALGUMAS MANCHAS CLARAS",
    "VERDE ESCURO COM VARIAS MANCHAS CLARAS",
    "VERDE ESCURO COM ALGUMAS MANCHAS ESCURAS",
    "VERDE ESCURO COM VARIAS MANCHAS ESCURAS",
    "OPACO PREDOMINANTE",
    "AVERMELHADO PREDOMINANTE",
    "NÃO REGISTRADO",
)

PLANTATION_TYPE_VALUES = (
    "PLANTIO INTERNO (FATEC)",
    "PLANTIO EXTERNO (CASA)",
)


class PlantModel(db.Model):
    __tablename__ = "plants"

    id = db.Column(
        String(36), primary_key=True, nullable=False, server_default=text("(UUID())")
    )
    name = db.Column(String(255), nullable=False, unique=True)
    hex_color = db.Column(String(7), nullable=False)
    created_at = db.Column(
        DateTime,
        nullable=False,
        server_default=text("(NOW())"),
    )


class SensorsRecordModel(db.Model):
    __tablename__ = "sensors_records"

    id = db.Column(
        String(36), primary_key=True, nullable=False, server_default=text("(UUID())")
    )
    soil_humidity = db.Column(Integer, nullable=False)
    ambient_humidity = db.Column(Integer, nullable=False)
    temperature = db.Column(Numeric(10, 2), nullable=False)
    water_volume = db.Column(Numeric(10, 2), nullable=False)
    created_at = db.Column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    plant_id = db.Column(
        String(36),
        ForeignKey("plants.id", ondelete="CASCADE"),
        nullable=True,
        server_default=text(f"'{DEFAULT_PLANT_ID}'"),
    )


class ChecklistRecordModel(db.Model):
    __tablename__ = "checklist_records"

    id = db.Column(
        String(36), primary_key=True, nullable=False, server_default=text("(UUID())")
    )
    soil_ph = db.Column(Integer, nullable=False)
    soil_humidity = db.Column(Integer, nullable=False)
    air_humidity = db.Column(Integer, nullable=False)
    water_consumption = db.Column(Numeric(10, 2), nullable=False)
    temperature = db.Column(Numeric(10, 1), nullable=False)
    illuminance = db.Column(Numeric(10, 2), nullable=False)
    lai = db.Column(Numeric(10, 2), nullable=True)
    leaf_appearance = db.Column(
        Enum(*LEAF_APPEARANCE_VALUES, name="checklist_leaf_appearance"),
        nullable=True,
        server_default=text("'NÃO REGISTRADO'"),
    )
    leaf_color = db.Column(
        Enum(*LEAF_COLOR_VALUES, name="checklist_leaf_color"),
        nullable=True,
        server_default=text("'NÃO REGISTRADO'"),
    )
    plantation_type = db.Column(
        Enum(*PLANTATION_TYPE_VALUES, name="checklist_plantation_type"),
        nullable=True,
        server_default=text("'PLANTIO INTERNO (FATEC)'"),
    )
    fertilizer_expiration_date = db.Column(Date, nullable=False)
    created_at = db.Column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    report = db.Column(Text, nullable=True)
    plant_id = db.Column(
        String(36),
        ForeignKey("plants.id", ondelete="CASCADE"),
        nullable=True,
        server_default=text(f"'{DEFAULT_PLANT_ID}'"),
    )


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(
        String(36), primary_key=True, nullable=False, server_default=text("(UUID())")
    )
    email = db.Column(String(255), nullable=False)
    password = db.Column(Text, nullable=False)
    active_plant_id = db.Column(
        String(36),
        ForeignKey("plants.id", ondelete="SET NULL"),
        nullable=True,
        server_default=text(f"'{DEFAULT_PLANT_ID}'"),
    )
