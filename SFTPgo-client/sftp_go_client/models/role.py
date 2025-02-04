from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]): name is unique
        description (Union[Unset, str]): optional description
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds
        updated_at (Union[Unset, int]): last update time as unix timestamp in milliseconds
        users (Union[Unset, list[str]]): list of usernames associated with this group
        admins (Union[Unset, list[str]]): list of admins usernames associated with this group
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    users: Union[Unset, list[str]] = UNSET
    admins: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        admins: Union[Unset, list[str]] = UNSET
        if not isinstance(self.admins, Unset):
            admins = self.admins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if users is not UNSET:
            field_dict["users"] = users
        if admins is not UNSET:
            field_dict["admins"] = admins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        users = cast(list[str], d.pop("users", UNSET))

        admins = cast(list[str], d.pop("admins", UNSET))

        role = cls(
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            users=users,
            admins=admins,
        )

        role.additional_properties = d
        return role

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
