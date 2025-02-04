from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_list_mode import IPListMode
from ..models.ip_list_type import IPListType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IPListEntry")


@_attrs_define
class IPListEntry:
    """
    Attributes:
        ipornet (Union[Unset, str]): IP address or network in CIDR format, for example `192.168.1.2/32`,
            `192.168.0.0/24`, `2001:db8::/32`
        description (Union[Unset, str]): optional description
        type_ (Union[Unset, IPListType]): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        mode (Union[Unset, IPListMode]): IP list modes
              * `1` - allow
              * `2` - deny, supported for defender list type only
        protocols (Union[Unset, int]): Defines the protocol the entry applies to. `0` means all the supported protocols,
            1 SSH, 2 FTP, 4 WebDAV, 8 HTTP. Protocols can be combined, for example 3 means SSH and FTP
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds
        updated_at (Union[Unset, int]): last update time as unix timestamp in millisecond
    """

    ipornet: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, IPListType] = UNSET
    mode: Union[Unset, IPListMode] = UNSET
    protocols: Union[Unset, int] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipornet = self.ipornet

        description = self.description

        type_: Union[Unset, int] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        mode: Union[Unset, int] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        protocols = self.protocols

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipornet is not UNSET:
            field_dict["ipornet"] = ipornet
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if protocols is not UNSET:
            field_dict["protocols"] = protocols
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ipornet = d.pop("ipornet", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, IPListType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IPListType(_type_)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, IPListMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IPListMode(_mode)

        protocols = d.pop("protocols", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        ip_list_entry = cls(
            ipornet=ipornet,
            description=description,
            type_=type_,
            mode=mode,
            protocols=protocols,
            created_at=created_at,
            updated_at=updated_at,
        )

        ip_list_entry.additional_properties = d
        return ip_list_entry

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
