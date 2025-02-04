from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission import Permission

T = TypeVar("T", bound="GroupUserSettingsPermissions")


@_attrs_define
class GroupUserSettingsPermissions:
    """hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions
    for root directory ("/") are required

        Example:
            {'/': ['*'], '/somedir': ['list', 'download']}

    """

    additional_properties: dict[str, list[Permission]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.value
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        group_user_settings_permissions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = Permission(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        group_user_settings_permissions.additional_properties = additional_properties
        return group_user_settings_permissions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[Permission]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[Permission]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
