from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaUsage")


@_attrs_define
class QuotaUsage:
    """
    Attributes:
        used_quota_size (Union[Unset, int]):
        used_quota_files (Union[Unset, int]):
    """

    used_quota_size: Union[Unset, int] = UNSET
    used_quota_files: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used_quota_size = self.used_quota_size

        used_quota_files = self.used_quota_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_quota_size is not UNSET:
            field_dict["used_quota_size"] = used_quota_size
        if used_quota_files is not UNSET:
            field_dict["used_quota_files"] = used_quota_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        used_quota_size = d.pop("used_quota_size", UNSET)

        used_quota_files = d.pop("used_quota_files", UNSET)

        quota_usage = cls(
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
        )

        quota_usage.additional_properties = d
        return quota_usage

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
