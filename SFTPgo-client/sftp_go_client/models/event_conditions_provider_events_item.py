from enum import Enum


class EventConditionsProviderEventsItem(str, Enum):
    ADD = "add"
    DELETE = "delete"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
