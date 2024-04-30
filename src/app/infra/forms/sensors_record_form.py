from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    SubmitField,
    IntegerField,
    SelectField,
    StringField,
)
from wtforms.validators import DataRequired, NumberRange

from infra.repositories import plants_repository


class SensorsRecordsForm(FlaskForm):
    def __init__(self, formdata=None, **kwargs):
        super().__init__(formdata, **kwargs)
        plants = plants_repository.get_plants()

        self.plant_id.choices = [(plant.id, plant.name) for plant in plants]

    date = DateField(
        "Data de coleta", render_kw={"max": datetime.now().strftime("%Y-%m-%d")}
    )

    hour = IntegerField(
        "Hora da Coleta", validators=[DataRequired(), NumberRange(min=0, max=23)]
    )

    soil_humidity = IntegerField(
        "Umidade do Solo (%)", validators=[DataRequired(), NumberRange(min=0, max=100)]
    )

    ambient_humidity = IntegerField(
        "Umidade do Ambiente (%)",
        validators=[DataRequired(), NumberRange(min=0, max=100)],
    )

    temperature = IntegerField(
        "Temperatura ambiente (%)",
        validators=[DataRequired(), NumberRange(min=0, max=100)],
    )
    water_volume = IntegerField(
        "Vazão da água (mL)", validators=[DataRequired(), NumberRange(min=0, max=100)]
    )

    plant_id = SelectField("Planta")

    id = StringField()

    submit_button = SubmitField("Enviar")
