from enum import Enum


class ProviderEventObjectType(str, Enum):
    ADMIN = "admin"
    API_KEY = "api_key"
    EVENT_ACTION = "event_action"
    EVENT_RULE = "event_rule"
    FOLDER = "folder"
    GROUP = "group"
    ROLE = "role"
    SHARE = "share"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
