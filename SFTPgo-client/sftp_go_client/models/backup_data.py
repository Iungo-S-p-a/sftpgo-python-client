from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.api_key import APIKey
    from ..models.base_virtual_folder import BaseVirtualFolder
    from ..models.event_action import EventAction
    from ..models.event_rule import EventRule
    from ..models.group import Group
    from ..models.role import Role
    from ..models.share import Share
    from ..models.user import User


T = TypeVar("T", bound="BackupData")


@_attrs_define
class BackupData:
    """
    Attributes:
        users (Union[Unset, list['User']]):
        folders (Union[Unset, list['BaseVirtualFolder']]):
        groups (Union[Unset, list['Group']]):
        admins (Union[Unset, list['Admin']]):
        api_keys (Union[Unset, list['APIKey']]):
        shares (Union[Unset, list['Share']]):
        event_actions (Union[Unset, list['EventAction']]):
        event_rules (Union[Unset, list['EventRule']]):
        roles (Union[Unset, list['Role']]):
        version (Union[Unset, int]):
    """

    users: Union[Unset, list["User"]] = UNSET
    folders: Union[Unset, list["BaseVirtualFolder"]] = UNSET
    groups: Union[Unset, list["Group"]] = UNSET
    admins: Union[Unset, list["Admin"]] = UNSET
    api_keys: Union[Unset, list["APIKey"]] = UNSET
    shares: Union[Unset, list["Share"]] = UNSET
    event_actions: Union[Unset, list["EventAction"]] = UNSET
    event_rules: Union[Unset, list["EventRule"]] = UNSET
    roles: Union[Unset, list["Role"]] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        folders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        admins: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.admins, Unset):
            admins = []
            for admins_item_data in self.admins:
                admins_item = admins_item_data.to_dict()
                admins.append(admins_item)

        api_keys: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.api_keys, Unset):
            api_keys = []
            for api_keys_item_data in self.api_keys:
                api_keys_item = api_keys_item_data.to_dict()
                api_keys.append(api_keys_item)

        shares: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shares, Unset):
            shares = []
            for shares_item_data in self.shares:
                shares_item = shares_item_data.to_dict()
                shares.append(shares_item)

        event_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_actions, Unset):
            event_actions = []
            for event_actions_item_data in self.event_actions:
                event_actions_item = event_actions_item_data.to_dict()
                event_actions.append(event_actions_item)

        event_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_rules, Unset):
            event_rules = []
            for event_rules_item_data in self.event_rules:
                event_rules_item = event_rules_item_data.to_dict()
                event_rules.append(event_rules_item)

        roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if folders is not UNSET:
            field_dict["folders"] = folders
        if groups is not UNSET:
            field_dict["groups"] = groups
        if admins is not UNSET:
            field_dict["admins"] = admins
        if api_keys is not UNSET:
            field_dict["api_keys"] = api_keys
        if shares is not UNSET:
            field_dict["shares"] = shares
        if event_actions is not UNSET:
            field_dict["event_actions"] = event_actions
        if event_rules is not UNSET:
            field_dict["event_rules"] = event_rules
        if roles is not UNSET:
            field_dict["roles"] = roles
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.admin import Admin
        from ..models.api_key import APIKey
        from ..models.base_virtual_folder import BaseVirtualFolder
        from ..models.event_action import EventAction
        from ..models.event_rule import EventRule
        from ..models.group import Group
        from ..models.role import Role
        from ..models.share import Share
        from ..models.user import User

        d = src_dict.copy()
        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = BaseVirtualFolder.from_dict(folders_item_data)

            folders.append(folders_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = Group.from_dict(groups_item_data)

            groups.append(groups_item)

        admins = []
        _admins = d.pop("admins", UNSET)
        for admins_item_data in _admins or []:
            admins_item = Admin.from_dict(admins_item_data)

            admins.append(admins_item)

        api_keys = []
        _api_keys = d.pop("api_keys", UNSET)
        for api_keys_item_data in _api_keys or []:
            api_keys_item = APIKey.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        shares = []
        _shares = d.pop("shares", UNSET)
        for shares_item_data in _shares or []:
            shares_item = Share.from_dict(shares_item_data)

            shares.append(shares_item)

        event_actions = []
        _event_actions = d.pop("event_actions", UNSET)
        for event_actions_item_data in _event_actions or []:
            event_actions_item = EventAction.from_dict(event_actions_item_data)

            event_actions.append(event_actions_item)

        event_rules = []
        _event_rules = d.pop("event_rules", UNSET)
        for event_rules_item_data in _event_rules or []:
            event_rules_item = EventRule.from_dict(event_rules_item_data)

            event_rules.append(event_rules_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = Role.from_dict(roles_item_data)

            roles.append(roles_item)

        version = d.pop("version", UNSET)

        backup_data = cls(
            users=users,
            folders=folders,
            groups=groups,
            admins=admins,
            api_keys=api_keys,
            shares=shares,
            event_actions=event_actions,
            event_rules=event_rules,
            roles=roles,
            version=version,
        )

        backup_data.additional_properties = d
        return backup_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
