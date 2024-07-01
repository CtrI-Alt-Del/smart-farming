from .login_user_factory import LoginUserFactory
from .request_password_reset_factory import RequestPasswordResetFactory
from .reset_password_factory import ResetPasswordFactory

login_user = LoginUserFactory.produce()
request_password_reset = RequestPasswordResetFactory.produce()
reset_password = ResetPasswordFactory.produce()
