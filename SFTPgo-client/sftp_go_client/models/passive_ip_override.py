from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PassiveIPOverride")


@_attrs_define
class PassiveIPOverride:
    """
    Attributes:
        networks (Union[Unset, list[str]]):
        ip (Union[Unset, str]):
    """

    networks: Union[Unset, list[str]] = UNSET
    ip: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        networks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = self.networks

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if networks is not UNSET:
            field_dict["networks"] = networks
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        networks = cast(list[str], d.pop("networks", UNSET))

        ip = d.pop("ip", UNSET)

        passive_ip_override = cls(
            networks=networks,
            ip=ip,
        )

        passive_ip_override.additional_properties = d
        return passive_ip_override

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
