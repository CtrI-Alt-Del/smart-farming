from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    IntegerField,
    TextAreaField,
    TimeField,
    FloatField,
)
from wtforms.validators import NumberRange, DataRequired

from core.entities import CheckListRecord

from infra.repositories import plants_repository


class ChecklistRecordForm(FlaskForm):
    def __init__(self, formdata=None, checklist_record=None, **kwargs):
        super().__init__(formdata, **kwargs)

        plants = plants_repository.get_plants()
        self.plant_id.choices = [(plant.id, plant.name) for plant in plants]

        if isinstance(checklist_record, CheckListRecord):
            self.date.data = checklist_record.created_at.get_value(is_datetime=True)
            self.time.data = checklist_record.created_at.get_time()
            self.air_humidity.data = checklist_record.air_humidity
            self.illuminance.data = checklist_record.illuminance
            self.lai.data = checklist_record.lai
            self.temperature.data = checklist_record.temperature
            self.water_consumption.data = checklist_record.water_consumption
            self.report.data = checklist_record.report
            self.soil_ph.data = checklist_record.soil_ph
            self.soil_humidity.data = checklist_record.soil_humidity
            self.plantation_type.data = checklist_record.plantation_type
            self.leaf_color.data = checklist_record.leaf_color
            self.leaf_appearance.data = checklist_record.leaf_appearance
            self.plant_id.data = checklist_record.plant.id
            self.fertilizer_expiration_date.data = (
                checklist_record.fertilizer_expiration_date.get_value(is_date=True)
            )

    plantation_type = SelectField(
        "Local de plantio",
        choices=[
            ("PLANTIO INTERNO (FATEC)", "Interno"),
            ("PLANTIO EXTERNO (CASA)", "Externo"),
        ],
    )
    leaf_appearance = SelectField(
        "Aspecto das folhas",
        choices=[
            ("SAUDAVEL", "Saudável"),
            ("MURCHA", "Murcha"),
        ],
    )
    leaf_color = SelectField(
        "Coloração das folhas",
        choices=[
            ("VERDE CLARO PREDOMINANTE", "Verde claro predominante"),
            ("VERDE ESCURO PREDOMINANTE", "Verde escuro predominante"),
            (
                "VERDE CLARO COM ALGUMAS MANCHAS CLARAS",
                "Verde claro com algumas claras",
            ),
            (
                "VERDE CLARO COM VARIAS MANCHAS CLARAS",
                "Verde claro com várias manchas claras",
            ),
            (
                "VERDE CLARO COM ALGUMAS MANCHAS ESCURAS",
                "Verde claro com algumas manchas escuras",
            ),
            (
                "VERDE CLARO COM VARIAS MANCHAS ESCURAS",
                "Verde claro com várias manchas escuras",
            ),
            (
                "VERDE ESCURO COM ALGUMAS MANCHAS CLARAS",
                "Verde escuro com algumas manchas claras",
            ),
            (
                "VERDE ESCURO COM VARIAS MANCHAS CLARAS",
                "Verde escuro com várias manchas claras",
            ),
            (
                "VERDE ESCURO COM ALGUMAS MANCHAS ESCURAS",
                "Verde escuro com algumas manchas escuras",
            ),
            (
                "VERDE ESCURO COM VARIAS MANCHAS ESCURAS",
                "Verde escuro com várias manchas escuras",
            ),
            ("OPACO PREDOMINANTE", "Opaco predominante"),
            ("AVERMELHADO PREDOMINANTE", "Avermelhado predominante"),
        ],
    )
    date = DateField(
        "Data de coleta",
        render_kw={"max": datetime.now().strftime("%Y-%m-%d")},
    )
    fertilizer_expiration_date = DateField(
        "Validade de adubação",
        render_kw={"max": datetime.now().strftime("%Y-%m-%d")},
    )
    time = TimeField(
        "Hora de coleta",
        validators=[DataRequired()],
    )
    soil_humidity = IntegerField(
        "Umidade do solo (%)",
        validators=[
            NumberRange(min=0, max=100, message="O valor deve estar entre 0 e 100"),
        ],
    )
    air_humidity = IntegerField(
        "Umidade do ar (%)",
        validators=[
            NumberRange(min=0, max=100, message="O valor deve estar entre 0 e 100"),
        ],
    )
    soil_ph = IntegerField(
        "PH do solo",
        validators=[
            NumberRange(min=0, max=14, message="O valor deve estar entre 0 e 14"),
        ],
    )
    lai = FloatField(
        "Índice de área foliar (m²/m²)",
        validators=[
            NumberRange(min=0.0, message="O valor deve ser maior ou igual a 0"),
        ],
    )
    water_consumption = FloatField(
        "Consumo de água detectado (ml)",
        validators=[
            NumberRange(min=0, message="O valor deve ser maior ou igual a 0"),
        ],
    )
    temperature = FloatField(
        "Temperatura ambiente (°C)",
        validators=[
            NumberRange(
                min=-273, max=60, message="O valor deve estar entre -273ºC e 60ºC"
            ),
        ],
    )
    illuminance = FloatField(
        "Luminosidade (Lux)",
        validators=[
            NumberRange(min=0, message="O valor deve ser maior ou igual a 0"),
        ],
    )
    report = TextAreaField("Algum desvio detectado?")
    plant_id = SelectField("Planta", validators=[DataRequired()])
