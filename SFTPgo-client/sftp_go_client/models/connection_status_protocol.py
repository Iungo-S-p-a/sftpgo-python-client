from enum import Enum


class ConnectionStatusProtocol(str, Enum):
    DAV = "DAV"
    FTP = "FTP"
    SCP = "SCP"
    SFTP = "SFTP"
    SSH = "SSH"

    def __str__(self) -> str:
        return str(self.value)
