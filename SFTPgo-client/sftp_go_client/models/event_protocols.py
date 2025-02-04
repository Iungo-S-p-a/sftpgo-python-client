from enum import Enum


class EventProtocols(str, Enum):
    DATARETENTION = "DataRetention"
    DAV = "DAV"
    EVENTACTION = "EventAction"
    FTP = "FTP"
    HTTP = "HTTP"
    HTTPSHARE = "HTTPShare"
    OIDC = "OIDC"
    SCP = "SCP"
    SFTP = "SFTP"
    SSH = "SSH"

    def __str__(self) -> str:
        return str(self.value)
