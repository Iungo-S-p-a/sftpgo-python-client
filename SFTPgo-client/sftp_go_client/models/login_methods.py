from enum import Enum


class LoginMethods(str, Enum):
    KEYBOARD_INTERACTIVE = "keyboard-interactive"
    PASSWORD = "password"
    PASSWORD_OVER_SSH = "password-over-SSH"
    PUBLICKEY = "publickey"
    PUBLICKEYKEYBOARD_INTERACTIVE = "publickey+keyboard-interactive"
    PUBLICKEYPASSWORD = "publickey+password"
    TLSCERTIFICATE = "TLSCertificate"
    TLSCERTIFICATEPASSWORD = "TLSCertificate+password"

    def __str__(self) -> str:
        return str(self.value)
