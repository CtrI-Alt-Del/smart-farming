from core.interfaces.providers import EmailProvideInterface
from core.constants import ADMIN_USER_EMAIL, SUPPORT_USER_EMAIL
from core.errors.authentication import (
    UserEmailNotValidError,
    EmailTemplateNotValidError,
    SenderPasswordNotValidError,
    AdminUserEmailNotMatchedError,
)


class RequestPasswordReset:
    def __init__(self, email_provider: EmailProvideInterface):
        self._email_provider = email_provider

    def execute(self, user_email: str, email_template: str, sender_password: str):
        if not isinstance(user_email, str):
            raise UserEmailNotValidError()

        if not isinstance(email_template, str):
            raise EmailTemplateNotValidError()

        if not isinstance(sender_password, str):
            raise SenderPasswordNotValidError()

        if user_email != ADMIN_USER_EMAIL:
            raise AdminUserEmailNotMatchedError()

        self._email_provider.send_email(
            sender=SUPPORT_USER_EMAIL,
            receiver=user_email,
            template=email_template,
            password=sender_password,
        )
