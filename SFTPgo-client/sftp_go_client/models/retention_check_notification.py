from enum import Enum


class RetentionCheckNotification(str, Enum):
    EMAIL = "Email"
    HOOK = "Hook"

    def __str__(self) -> str:
        return str(self.value)
