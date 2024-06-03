from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError

import re

class LoginForm(FlaskForm):
  email = StringField(
        "email",
        validators=[DataRequired(), Email()],
    )

  password = StringField("password", validators=[DataRequired()])

  def validate_password(self, password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{6,}$'
        
        if not re.match(pattern, password.data):
            raise ValidationError('Senha inválida. Deve conter pelo menos 6 caracteres, uma letra minúscula, uma letra maiúscula e um caractere especial.')

 