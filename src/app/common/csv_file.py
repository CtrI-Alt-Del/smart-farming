from werkzeug.datastructures import FileStorage

from utils.error import Error


class CsvFile:
    def __init__(self, csv_file: FileStorage) -> None:
        self.csv_file = csv_file

    def validate(self):
        if not isinstance(self.csv_file, FileStorage):
            raise Error("Arquivo de cursos precisa ser um arquivo csv")

        extension = self.get_extension()

        if extension not in ["xlsx", "csv", "txt"]:
            raise Error(
                "Arquivo contendo os cursos precisam ser must um arquivo csv em formato de texto ou excel válido"
            )

    def get_extension(self):
        return self.csv_file.filename.split(".")[1]
