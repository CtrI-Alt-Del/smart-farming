from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    SubmitField,
    IntegerField,
    TextAreaField,
    StringField,
)
from wtforms.validators import NumberRange

from infra.repositories import plants_repository


class ChecklistRecordForm(FlaskForm):
    def __init__(self, formdata=None, **kwargs):
        super().__init__(formdata, **kwargs)

        plants = plants_repository.get_plants()

        self.plant_id.choices = [(plant.id, plant.name) for plant in plants]

    plantation_type = SelectField(
        "Local de plantio",
        choices=[
            ("PLANTIO INTERNO(FATEC)", "Interno"),
            ("PLANTIO EXTERNO(CASA)", "Externo"),
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
            ("VERDE CLARO DOMINANTE", "Verde claro dominante"),
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
    hour = IntegerField("Hora de coleta", validators=[NumberRange(min=0, max=23)])
    fertilizer_expiration_date = DateField(
        "Validade de adubação",
        render_kw={"max": datetime.now().strftime("%Y-%m-%d")},
    )
    soil_humidity = IntegerField(
        "Umidade do solo (%)", validators=[NumberRange(min=0, max=100)]
    )
    air_humidity = IntegerField(
        "Umidade do ar (%)", validators=[NumberRange(min=0, max=100)]
    )
    lai = IntegerField("Umidade do ar (%)", validators=[NumberRange(min=0, max=100)])
    water_consumption = IntegerField(
        "Consumo de água detectado (ml)", validators=[NumberRange(min=0)]
    )
    temperature = IntegerField(
        "Temperatura ambiente (°C)", validators=[NumberRange(min=-273, max=60)]
    )
    illuminance = IntegerField("Luminosidade (Lux)", validators=[NumberRange(min=0)])
    soil_ph = IntegerField("PH do solo", validators=[NumberRange(min=0, max=7)])
    report = TextAreaField("Algum desvio detectado?")
    plant_id = SelectField("Planta")
    id = StringField()
    submit_button = SubmitField("Enviar")


# 6979a7cc-01b0-11ef-88a9-0242ac1b0002
