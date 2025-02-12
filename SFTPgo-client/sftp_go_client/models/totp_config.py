from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.totph_mac_algo import TOTPHMacAlgo
from ..types import UNSET, Unset

T = TypeVar("T", bound="TOTPConfig")


@_attrs_define
class TOTPConfig:
    """
    Attributes:
        name (Union[Unset, str]):
        issuer (Union[Unset, str]):
        algo (Union[Unset, TOTPHMacAlgo]): Supported HMAC algorithms for Time-based one time passwords
    """

    name: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    algo: Union[Unset, TOTPHMacAlgo] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        issuer = self.issuer

        algo: Union[Unset, str] = UNSET
        if not isinstance(self.algo, Unset):
            algo = self.algo.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if algo is not UNSET:
            field_dict["algo"] = algo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        issuer = d.pop("issuer", UNSET)

        _algo = d.pop("algo", UNSET)
        algo: Union[Unset, TOTPHMacAlgo]
        if isinstance(_algo, Unset):
            algo = UNSET
        else:
            algo = TOTPHMacAlgo(_algo)

        totp_config = cls(
            name=name,
            issuer=issuer,
            algo=algo,
        )

        totp_config.additional_properties = d
        return totp_config

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
