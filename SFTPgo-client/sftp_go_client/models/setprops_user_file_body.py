from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetpropsUserFileBody")


@_attrs_define
class SetpropsUserFileBody:
    """
    Attributes:
        modification_time (Union[Unset, int]): File modification time as unix timestamp in milliseconds
    """

    modification_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modification_time = self.modification_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modification_time is not UNSET:
            field_dict["modification_time"] = modification_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        modification_time = d.pop("modification_time", UNSET)

        setprops_user_file_body = cls(
            modification_time=modification_time,
        )

        setprops_user_file_body.additional_properties = d
        return setprops_user_file_body

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
