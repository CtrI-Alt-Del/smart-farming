from core.use_cases.authentication import RequestPasswordReset

from infra.providers import EmailProvider


class RequestPasswordResetFactory:
    @staticmethod
    def produce():
        return RequestPasswordReset(EmailProvider())
