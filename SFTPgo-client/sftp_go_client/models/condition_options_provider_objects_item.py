from enum import Enum


class ConditionOptionsProviderObjectsItem(str, Enum):
    ADMIN = "admin"
    API_KEY = "api_key"
    EVENT_ACTION = "event_action"
    EVENT_RULE = "event_rule"
    GROUP = "group"
    SHARE = "share"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
