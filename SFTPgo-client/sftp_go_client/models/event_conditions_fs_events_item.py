from enum import Enum


class EventConditionsFsEventsItem(str, Enum):
    COPY = "copy"
    DELETE = "delete"
    DOWNLOAD = "download"
    FIRST_DOWNLOAD = "first-download"
    FIRST_UPLOAD = "first-upload"
    MKDIR = "mkdir"
    PRE_DELETE = "pre-delete"
    PRE_DOWNLOAD = "pre-download"
    PRE_UPLOAD = "pre-upload"
    RENAME = "rename"
    RMDIR = "rmdir"
    SSH_CMD = "ssh_cmd"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
