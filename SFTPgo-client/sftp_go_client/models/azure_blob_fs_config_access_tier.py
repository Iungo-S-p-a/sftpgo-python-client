from enum import Enum


class AzureBlobFsConfigAccessTier(str, Enum):
    ARCHIVE = "Archive"
    COOL = "Cool"
    HOT = "Hot"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
