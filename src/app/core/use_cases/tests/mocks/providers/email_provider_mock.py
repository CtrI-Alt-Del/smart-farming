from core.interfaces.providers import EmailProvideInterface


class EmailProviderMock(EmailProvideInterface):
    _email = None

    def send_email(self, sender: str, receiver: str, template: str, password: str):
        self._email = f"sender: {sender}; receiver: {receiver}; template: {template}; password: {password}"

    @property
    def email(self):
        return self._email
