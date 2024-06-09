from pathlib import Path
from gzip import open as open_compressed_file

from core.commons import Error


class File:
    path: Path

    def __init__(self, folder, filename) -> None:
        self.path = Path(f"{folder}/{filename}")

    def read_text(self) -> str:
        try:
            return self.path.read_text(encoding="utf-8")
        except Exception as exception:
            raise Error(
                f"Failed to read {self.path.absolute()} file. Error: {exception}"
            ) from exception

    def delete(self):
        try:
            self.path.unlink()
        except Exception as exception:
            raise Error(
                f"Failed to delete {self.path.absolute()} file. Error: {exception}"
            ) from exception

    def compress(self):
        file_path = self.path.absolute()
        compress_file_path = str(file_path) + ".gz"

        with open(file_path, "rb") as file:
            with open_compressed_file(compress_file_path, "wb") as compressed_file:
                compressed_file.write(file.read())

        self.delete()
        self.path = Path(compress_file_path)
