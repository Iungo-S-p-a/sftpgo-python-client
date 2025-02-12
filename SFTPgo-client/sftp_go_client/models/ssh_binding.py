from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHBinding")


@_attrs_define
class SSHBinding:
    """
    Attributes:
        address (Union[Unset, str]): TCP address the server listen on
        port (Union[Unset, int]): the port used for serving requests
        apply_proxy_config (Union[Unset, bool]): apply the proxy configuration, if any
    """

    address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    apply_proxy_config: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        port = self.port

        apply_proxy_config = self.apply_proxy_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if apply_proxy_config is not UNSET:
            field_dict["apply_proxy_config"] = apply_proxy_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        apply_proxy_config = d.pop("apply_proxy_config", UNSET)

        ssh_binding = cls(
            address=address,
            port=port,
            apply_proxy_config=apply_proxy_config,
        )

        ssh_binding.additional_properties = d
        return ssh_binding

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
