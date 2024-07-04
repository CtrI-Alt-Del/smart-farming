from abc import ABC, abstractmethod
from dataclasses import dataclass

from cowsay import func as cow_say


@dataclass
class BaseError(Exception, ABC):
    ui_message: str = "Pultz, algo deu errado"
    internal_message: str = "Internal Server Error"
    status_code: int = 500

    def __post_init__(
        self,
    ):
        super().__init__(self.ui_message)
        self.print_error()

    @abstractmethod
    def print_error(self):
        cow_say(self.internal_message)
