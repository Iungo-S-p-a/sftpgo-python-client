from enum import Enum


class FsEventAction(str, Enum):
    DELETE = "delete"
    DOWNLOAD = "download"
    FIRST_DOWNLOAD = "first-download"
    FIRST_UPLOAD = "first-upload"
    MKDIR = "mkdir"
    RENAME = "rename"
    RMDIR = "rmdir"
    SSH_CMD = "ssh_cmd"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
