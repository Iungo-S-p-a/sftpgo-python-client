from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventActionFsCompress")


@_attrs_define
class EventActionFsCompress:
    """
    Attributes:
        name (Union[Unset, str]): Full path to the (zip) archive to create. The parent dir must exist
        paths (Union[Unset, list[str]]): paths to add the archive
    """

    name: Union[Unset, str] = UNSET
    paths: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        paths: Union[Unset, list[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if paths is not UNSET:
            field_dict["paths"] = paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        paths = cast(list[str], d.pop("paths", UNSET))

        event_action_fs_compress = cls(
            name=name,
            paths=paths,
        )

        event_action_fs_compress.additional_properties = d
        return event_action_fs_compress

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
