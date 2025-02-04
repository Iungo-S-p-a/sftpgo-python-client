from enum import Enum


class SSHAuthentications(str, Enum):
    KEYBOARD_INTERACTIVE = "keyboard-interactive"
    PASSWORD = "password"
    PUBLICKEY = "publickey"
    PUBLICKEYKEYBOARD_INTERACTIVE = "publickey+keyboard-interactive"
    PUBLICKEYPASSWORD = "publickey+password"

    def __str__(self) -> str:
        return str(self.value)
