from enum import Enum


class DumpDataScopes(str, Enum):
    ACTIONS = "actions"
    ADMINS = "admins"
    API_KEYS = "api_keys"
    CONFIGS = "configs"
    FOLDERS = "folders"
    GROUPS = "groups"
    IP_LISTS = "ip_lists"
    ROLES = "roles"
    RULES = "rules"
    SHARES = "shares"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
