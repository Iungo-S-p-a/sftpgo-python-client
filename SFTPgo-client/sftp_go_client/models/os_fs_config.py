from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OSFsConfig")


@_attrs_define
class OSFsConfig:
    """
    Attributes:
        read_buffer_size (Union[Unset, int]): The read buffer size, as MB, to use for downloads. 0 means no buffering,
            that's fine in most use cases.
        write_buffer_size (Union[Unset, int]): The write buffer size, as MB, to use for uploads. 0 means no buffering,
            that's fine in most use cases.
    """

    read_buffer_size: Union[Unset, int] = UNSET
    write_buffer_size: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_buffer_size = self.read_buffer_size

        write_buffer_size = self.write_buffer_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read_buffer_size is not UNSET:
            field_dict["read_buffer_size"] = read_buffer_size
        if write_buffer_size is not UNSET:
            field_dict["write_buffer_size"] = write_buffer_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        read_buffer_size = d.pop("read_buffer_size", UNSET)

        write_buffer_size = d.pop("write_buffer_size", UNSET)

        os_fs_config = cls(
            read_buffer_size=read_buffer_size,
            write_buffer_size=write_buffer_size,
        )

        os_fs_config.additional_properties = d
        return os_fs_config

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
