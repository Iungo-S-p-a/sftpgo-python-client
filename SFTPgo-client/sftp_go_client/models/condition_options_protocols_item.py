from enum import Enum


class ConditionOptionsProtocolsItem(str, Enum):
    DAV = "DAV"
    FTP = "FTP"
    HTTP = "HTTP"
    HTTPSHARE = "HTTPShare"
    OIDC = "OIDC"
    SCP = "SCP"
    SFTP = "SFTP"
    SSH = "SSH"

    def __str__(self) -> str:
        return str(self.value)
