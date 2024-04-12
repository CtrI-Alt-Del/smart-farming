from pathlib import Path
from typing import Union


class File:
    def __init__(self, folder, name) -> None:
        self.path = Path(f"{folder}/{name}")

    def read_text(self) -> Union[str, None]:
        if self.exists():
            return self.path.read_text()

        return None

    def exists(self) -> bool:
        print(self.path.absolute())
        return self.path.exists()
