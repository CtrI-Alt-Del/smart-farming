from pytest import fixture, raises

from core.use_cases.authentication import LoginUser
from core.use_cases.tests.mocks.repositories import UsersRepositoryMock
from core.use_cases.tests.mocks.authentication import AuthMock
from core.entities.tests.fakers import UsersFaker
from core.errors.authentication import CredentialsNotValidError, UserNotFoundError
from core.constants import ADMIN_USER_EMAIL


def describe_login_user_use_case():
    @fixture
    def repository():
        return UsersRepositoryMock()

    @fixture
    def auth():
        return AuthMock()

    @fixture
    def use_case(repository: UsersRepositoryMock, auth: AuthMock):
        repository.clear_users()

        return LoginUser(repository, auth)

    def it_should_throw_an_error_if_provided_email_is_not_equal_to_admin_email(
        use_case: LoginUser,
    ):
        fake_user = UsersFaker.fake()

        with raises(CredentialsNotValidError):
            use_case.execute(
                email=fake_user.email,
                password=fake_user.password,
                should_remember_user=False,
            )

    def it_should_throw_an_error_if_no_user_is_found(
        use_case: LoginUser,
    ):
        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)

        with raises(UserNotFoundError):
            use_case.execute(
                email=fake_user.email,
                password=fake_user.password,
                should_remember_user=False,
            )

    def it_should_throw_an_error_if_password_is_incorrect(
        repository: UsersRepositoryMock,
        auth: AuthMock,
        use_case: LoginUser,
    ):
        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)
        repository.create_user(fake_user)

        auth.check_hash = lambda user, should_remember_user: False

        with raises(CredentialsNotValidError):
            use_case.execute(
                email=fake_user.email,
                password=fake_user.password,
                should_remember_user=False,
            )

    def it_should_throw_an_error_if_it_was_impossible_to_login_for_any_reason(
        repository: UsersRepositoryMock,
        auth: AuthMock,
        use_case: LoginUser,
    ):
        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)
        repository.create_user(fake_user)

        auth.login = lambda user, should_remember_user: False

        with raises(CredentialsNotValidError):
            use_case.execute(
                email=fake_user.email,
                password=fake_user.password,
                should_remember_user=False,
            )

    def it_should_set_should_remember_me(
        repository: UsersRepositoryMock,
        auth: AuthMock,
        use_case: LoginUser,
    ):
        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)
        repository.create_user(fake_user)

        should_remember_user = True

        use_case.execute(
            email=fake_user.email,
            password=fake_user.password,
            should_remember_user=should_remember_user,
        )

        assert auth.should_remember_user == should_remember_user

    def it_should_login_user(
        repository: UsersRepositoryMock,
        auth: AuthMock,
        use_case: LoginUser,
    ):
        fake_user = UsersFaker.fake(email=ADMIN_USER_EMAIL)
        repository.create_user(fake_user)

        use_case.execute(
            email=fake_user.email,
            password=fake_user.password,
            should_remember_user=False,
        )

        logged_in_user = auth.get_user()

        assert logged_in_user == fake_user
