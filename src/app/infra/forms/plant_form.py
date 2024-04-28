from flask_wtf import FlaskForm

from wtforms import (
    SubmitField,
    StringField,
)
from wtforms.validators import DataRequired, Regexp


class PlantForm(FlaskForm):
    def __init__(self, formdata=None, **kwargs):
        super().__init__(formdata, **kwargs)

    plant_name = StringField("Nome da planta", validators=[DataRequired()])
    hex_color = StringField(
        "Cor", validators=[Regexp(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")]
    )
    submit_button = SubmitField("Enviar")
