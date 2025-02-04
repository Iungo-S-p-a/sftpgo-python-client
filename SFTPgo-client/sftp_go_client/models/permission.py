from enum import Enum


class Permission(str, Enum):
    CHMOD = "chmod"
    CHOWN = "chown"
    CHTIMES = "chtimes"
    COPY = "copy"
    CREATE_DIRS = "create_dirs"
    CREATE_SYMLINKS = "create_symlinks"
    DELETE = "delete"
    DELETE_DIRS = "delete_dirs"
    DELETE_FILES = "delete_files"
    DOWNLOAD = "download"
    LIST = "list"
    OVERWRITE = "overwrite"
    RENAME = "rename"
    RENAME_DIRS = "rename_dirs"
    RENAME_FILES = "rename_files"
    UPLOAD = "upload"
    VALUE_0 = "*"

    def __str__(self) -> str:
        return str(self.value)
