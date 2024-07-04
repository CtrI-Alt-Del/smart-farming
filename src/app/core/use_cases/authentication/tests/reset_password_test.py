from pytest import fixture, raises

from core.use_cases.authentication import ResetPassword
from core.use_cases.tests.mocks.repositories import UsersRepositoryMock
from core.use_cases.tests.mocks.authentication import AuthMock
from core.entities.tests.fakers import UsersFaker
from core.errors.authentication import NewPasswordNotValidError
from core.constants import ADMIN_USER_EMAIL


def describe_reset_password_use_case():
    @fixture
    def repository():
        return UsersRepositoryMock()

    @fixture
    def auth():
        return AuthMock()

    @fixture
    def use_case(repository: UsersRepositoryMock, auth: AuthMock):
        return ResetPassword(repository, auth)

    def it_should_throw_an_error_if_new_password_is_not_string(
        use_case: ResetPassword,
    ):
        with raises(NewPasswordNotValidError):
            use_case.execute(
                new_password=42,
            )

    def it_should_reset_password(
        repository: UsersRepositoryMock,
        use_case: ResetPassword,
    ):

        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)
        repository.create_user(fake_user)

        new_password = "fake new password"

        use_case.execute(new_password=new_password)

        user = repository.get_user_by_id(fake_user.id)

        assert user.password == new_password
