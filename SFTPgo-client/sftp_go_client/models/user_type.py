from enum import Enum


class UserType(str, Enum):
    LDAPUSER = "LDAPUser"
    OSUSER = "OSUser"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
