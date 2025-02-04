from enum import Enum


class MFAProtocols(str, Enum):
    FTP = "FTP"
    HTTP = "HTTP"
    SSH = "SSH"

    def __str__(self) -> str:
        return str(self.value)
