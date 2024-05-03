from flask_wtf import FlaskForm

from wtforms import StringField, ColorField
from wtforms.validators import DataRequired


class PlantForm(FlaskForm):
    def __init__(self, formdata=None, **kwargs):
        super().__init__(formdata, **kwargs)

    name = StringField(
        "Nome da planta",
        validators=[DataRequired()],
        render_kw={"data-color-picker": "name"},
    )
    hex_color = ColorField(
        "Cor", validators=[DataRequired()], render_kw={"data-color-picker": "control"}
    )
