from abc import ABC, abstractmethod


class EmailProvideInterface(ABC):
    @abstractmethod
    def send_email(
        self, sender: str, receiver: str, template: str, password: str
    ) -> None: ...
