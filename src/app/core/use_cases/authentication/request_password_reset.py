from os import getenv

from infra.providers import EmailProvider
from core.commons import Error
from core.constants import ADMIN_EMAIL, SUPPORT_USER_EMAIL


class RequestPasswordReset:
    def execute(self, user_email: str, template_email_string: str):
        try:
            if user_email != ADMIN_EMAIL:
                raise Error("E-mail fornecido não é o e-mail do administrador")
            EmailSender = EmailProvider
            app_password = getenv("SUPPORT_EMAIL_APP_PASSWORD")
            support_email = SUPPORT_USER_EMAIL
            EmailSender.send_email(
                support_email, user_email, template_email_string, app_password
            )

        except Error as error:
            raise Error(ui_message=error, internal_message=error)
