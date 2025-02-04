from enum import Enum


class AdminPermissions(str, Enum):
    ADD_USERS = "add_users"
    CLOSE_CONNS = "close_conns"
    DEL_USERS = "del_users"
    DISABLE_MFA = "disable_mfa"
    EDIT_USERS = "edit_users"
    MANAGE_DEFENDER = "manage_defender"
    MANAGE_FOLDERS = "manage_folders"
    MANAGE_GROUPS = "manage_groups"
    QUOTA_SCANS = "quota_scans"
    VALUE_0 = "*"
    VIEW_CONNS = "view_conns"
    VIEW_DEFENDER = "view_defender"
    VIEW_EVENTS = "view_events"
    VIEW_STATUS = "view_status"
    VIEW_USERS = "view_users"

    def __str__(self) -> str:
        return str(self.value)
