from flask_wtf import FlaskForm
from wtforms import FileField
from flask_wtf.file import FileRequired, FileAllowed


class CsvForm(FlaskForm):
    field = FileField(
        label="Arquivo CSV",
        name="csv",
        validators=[
            FileRequired(),
            FileAllowed(
                upload_set=["csv", "txt", "xlsx"],
                message="Insira um arquivo csv válido (com extensão csv, txt ou xlsx)",
            ),
        ],
    )
