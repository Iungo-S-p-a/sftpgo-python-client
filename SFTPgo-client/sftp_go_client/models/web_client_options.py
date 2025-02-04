from enum import Enum


class WebClientOptions(str, Enum):
    API_KEY_AUTH_CHANGE_DISABLED = "api-key-auth-change-disabled"
    INFO_CHANGE_DISABLED = "info-change-disabled"
    MFA_DISABLED = "mfa-disabled"
    PASSWORD_CHANGE_DISABLED = "password-change-disabled"
    PASSWORD_RESET_DISABLED = "password-reset-disabled"
    PUBLICKEY_CHANGE_DISABLED = "publickey-change-disabled"
    SHARES_DISABLED = "shares-disabled"
    SHARES_WITHOUT_PASSWORD_DISABLED = "shares-without-password-disabled"
    TLS_CERT_CHANGE_DISABLED = "tls-cert-change-disabled"
    WRITE_DISABLED = "write-disabled"

    def __str__(self) -> str:
        return str(self.value)
