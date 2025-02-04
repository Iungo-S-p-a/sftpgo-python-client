from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesStatusRateLimiters")


@_attrs_define
class ServicesStatusRateLimiters:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        protocols (Union[Unset, list[str]]):
    """

    is_active: Union[Unset, bool] = UNSET
    protocols: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_active = self.is_active

        protocols: Union[Unset, list[str]] = UNSET
        if not isinstance(self.protocols, Unset):
            protocols = self.protocols

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if protocols is not UNSET:
            field_dict["protocols"] = protocols

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        protocols = cast(list[str], d.pop("protocols", UNSET))

        services_status_rate_limiters = cls(
            is_active=is_active,
            protocols=protocols,
        )

        services_status_rate_limiters.additional_properties = d
        return services_status_rate_limiters

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
