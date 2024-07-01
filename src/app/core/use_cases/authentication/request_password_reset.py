from core.interfaces.providers import EmailProvideInterface
from core.constants import ADMIN_USER_EMAIL, SUPPORT_USER_EMAIL
from core.errors.authentication import (
    UserEmailNotProvidedError,
    EmailTemplateNotProvidedError,
    SenderPasswordNotProvidedError,
    IncorrectAdminUserEmailError,
)


class RequestPasswordReset:
    def __init__(self, email_provider: EmailProvideInterface):
        self._email_provider = email_provider

    def execute(
        self, user_email: str, template_email_string: str, sender_password: str
    ):
        if not isinstance(user_email, str):
            raise UserEmailNotProvidedError()

        if not isinstance(template_email_string, str):
            raise EmailTemplateNotProvidedError()

        if not isinstance(sender_password, str):
            raise SenderPasswordNotProvidedError()

        if user_email != ADMIN_USER_EMAIL:
            raise IncorrectAdminUserEmailError()

        self._email_provider.send_email(
            sender=SUPPORT_USER_EMAIL,
            receiver=user_email,
            template=template_email_string,
            password=sender_password,
        )
