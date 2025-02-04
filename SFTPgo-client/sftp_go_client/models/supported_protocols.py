from enum import Enum


class SupportedProtocols(str, Enum):
    DAV = "DAV"
    FTP = "FTP"
    HTTP = "HTTP"
    SSH = "SSH"

    def __str__(self) -> str:
        return str(self.value)
