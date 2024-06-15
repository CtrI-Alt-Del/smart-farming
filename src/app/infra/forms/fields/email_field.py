from wtforms import EmailField as Field
from wtforms.validators import DataRequired, Email


class EmailField:
    email = Field(
        "E-mail",
        validators=[DataRequired(), Email()],
    )
