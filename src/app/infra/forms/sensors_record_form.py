from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    TimeField,
    IntegerField,
    FloatField,
    SelectField,
)
from wtforms.validators import DataRequired, NumberRange

from core.entities import SensorsRecord

from infra.repositories import plants_repository


class SensorsRecordForm(FlaskForm):
    def __init__(self, formdata=None, sensors_record=None, **kwargs):
        super().__init__(formdata, **kwargs)
        plants = plants_repository.get_plants()
        self.plant_id.choices = [(plant.id, plant.name) for plant in plants]

        if isinstance(sensors_record, SensorsRecord):
            self.date.data = sensors_record.created_at.get_value(is_datetime=True)
            self.time.data = sensors_record.created_at.get_time()
            self.ambient_humidity.data = sensors_record.ambient_humidity
            self.soil_humidity.data = sensors_record.soil_humidity
            self.water_volume.data = sensors_record.water_volume
            self.temperature.data = sensors_record.temperature
            self.plant_id.data = sensors_record.plant.id

    date = DateField(
        "Data de coleta", render_kw={"max": datetime.now().strftime("%Y-%m-%d")}
    )

    time = TimeField("Hora da Coleta", validators=[DataRequired()])

    soil_humidity = IntegerField(
        "Umidade do Solo (%)",
        validators=[
            NumberRange(min=1, max=100, message="O valor deve estar entre 0 e 100"),
        ],
    )
    ambient_humidity = IntegerField(
        "Umidade do Ambiente (%)",
        validators=[
            NumberRange(min=1, max=100, message="O valor deve estar entre 1 e 100"),
        ],
    )

    temperature = FloatField(
        "Temperatura ambiente (%)",
        validators=[
            NumberRange(
                min=-273, max=60, message="O valor deve estar entre -273ºC e 60ºC"
            ),
        ],
    )
    water_volume = FloatField(
        "Vazão da água (mL)",
        validators=[
            NumberRange(min=0, message="o valor deve ser maior ou igual a 0"),
        ],
    )

    plant_id = SelectField("Planta", validators=[DataRequired()])
