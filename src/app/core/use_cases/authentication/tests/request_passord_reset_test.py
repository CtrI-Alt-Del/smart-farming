from pytest import fixture, raises

from core.use_cases.authentication import RequestPasswordReset
from core.use_cases.tests.mocks.providers import EmailProviderMock
from core.entities.tests.fakers import UsersFaker
from core.errors.authentication import (
    UserEmailNotValidError,
    EmailTemplateNotValidError,
    SenderPasswordNotValidError,
    AdminUserEmailNotMatchedError,
)

from core.constants import ADMIN_USER_EMAIL, SUPPORT_USER_EMAIL


def describe_request_password_reset_use_case():
    @fixture
    def email_provider():
        return EmailProviderMock()

    @fixture
    def use_case(email_provider: EmailProviderMock):
        return RequestPasswordReset(email_provider)

    def it_should_throw_an_error_if_user_email_is_not_string(
        use_case: RequestPasswordReset,
    ):
        with raises(UserEmailNotValidError):
            use_case.execute(user_email=None, email_template=None, sender_password=None)

    def it_should_throw_an_error_if_template_email_is_not_string(
        use_case: RequestPasswordReset,
    ):
        fake_user = UsersFaker.fake()

        with raises(EmailTemplateNotValidError):
            use_case.execute(
                user_email=fake_user.email,
                email_template=None,
                sender_password=fake_user.password,
            )

    def it_should_throw_an_error_if_sender_password_is_not_string(
        use_case: RequestPasswordReset,
    ):
        fake_user = UsersFaker.fake()

        with raises(SenderPasswordNotValidError):
            use_case.execute(
                user_email=fake_user.email,
                email_template="fake template email string",
                sender_password=444,
            )

    def it_should_throw_an_error_if_user_email_is_not_equal_to_admin_email(
        use_case: RequestPasswordReset,
    ):
        fake_user = UsersFaker.fake()

        with raises(AdminUserEmailNotMatchedError):
            use_case.execute(
                user_email=fake_user.email,
                email_template="fake template email string",
                sender_password=fake_user.password,
            )

    def it_should_send_request_password_email(
        use_case: RequestPasswordReset,
        email_provider: EmailProviderMock,
    ):
        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)

        fake_email_template = "fake template email string"

        use_case.execute(
            user_email=fake_user.email,
            email_template=fake_email_template,
            sender_password=fake_user.password,
        )

        assert (
            email_provider.email
            == f"sender: {SUPPORT_USER_EMAIL}; receiver: {fake_user.email}; template: {fake_email_template}; password: {fake_user.password}"
        )
