from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHHostKey")


@_attrs_define
class SSHHostKey:
    """
    Attributes:
        path (Union[Unset, str]):
        fingerprint (Union[Unset, str]):
        algorithms (Union[Unset, list[str]]):
    """

    path: Union[Unset, str] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    algorithms: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        fingerprint = self.fingerprint

        algorithms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.algorithms, Unset):
            algorithms = self.algorithms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if algorithms is not UNSET:
            field_dict["algorithms"] = algorithms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        algorithms = cast(list[str], d.pop("algorithms", UNSET))

        ssh_host_key = cls(
            path=path,
            fingerprint=fingerprint,
            algorithms=algorithms,
        )

        ssh_host_key.additional_properties = d
        return ssh_host_key

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
