from enum import Enum


class SecretStatus(str, Enum):
    AES_256_GCM = "AES-256-GCM"
    AWS = "AWS"
    AZUREKEYVAULT = "AzureKeyVault"
    GCP = "GCP"
    PLAIN = "Plain"
    REDACTED = "Redacted"
    SECRETBOX = "Secretbox"
    VAULTTRANSIT = "VaultTransit"

    def __str__(self) -> str:
        return str(self.value)
