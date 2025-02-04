from enum import Enum


class TransferOperationType(str, Enum):
    DOWNLOAD = "download"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
