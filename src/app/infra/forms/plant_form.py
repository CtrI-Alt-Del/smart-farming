from flask_wtf import FlaskForm

from wtforms import StringField, ColorField
from wtforms.validators import DataRequired

from core.entities import Plant


class PlantForm(FlaskForm):
    def __init__(self, formdata=None, plant=None, **kwargs):
        super().__init__(formdata, **kwargs)

        if isinstance(plant, Plant):
            self.name.data = plant.name
            self.hex_color.data = plant.hex_color
            self.hex_color.default = plant.hex_color

    name = StringField(
        "Nome da planta",
        validators=[DataRequired()],
    )
    hex_color = ColorField("Cor", validators=[DataRequired()], default="#1c64f2d9")
