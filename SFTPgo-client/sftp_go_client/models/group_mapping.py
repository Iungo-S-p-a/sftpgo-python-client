from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_mapping_type import GroupMappingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupMapping")


@_attrs_define
class GroupMapping:
    """
    Attributes:
        name (Union[Unset, str]): group name
        type_ (Union[Unset, GroupMappingType]): Group type:
              * `1` - Primary group
              * `2` - Secondary group
              * `3` - Membership only, no settings are inherited from this group type
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, GroupMappingType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[Unset, int] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, GroupMappingType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GroupMappingType(_type_)

        group_mapping = cls(
            name=name,
            type_=type_,
        )

        group_mapping.additional_properties = d
        return group_mapping

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
