from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandwidthLimit")


@_attrs_define
class BandwidthLimit:
    """
    Attributes:
        sources (Union[Unset, list[str]]): Source networks in CIDR notation as defined in RFC 4632 and RFC 4291 for
            example `192.0.2.0/24` or `2001:db8::/32`. The limit applies if the defined networks contain the client IP
        upload_bandwidth (Union[Unset, int]): Maximum upload bandwidth as KB/s, 0 means unlimited
        download_bandwidth (Union[Unset, int]): Maximum download bandwidth as KB/s, 0 means unlimited
    """

    sources: Union[Unset, list[str]] = UNSET
    upload_bandwidth: Union[Unset, int] = UNSET
    download_bandwidth: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sources: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources

        upload_bandwidth = self.upload_bandwidth

        download_bandwidth = self.download_bandwidth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sources is not UNSET:
            field_dict["sources"] = sources
        if upload_bandwidth is not UNSET:
            field_dict["upload_bandwidth"] = upload_bandwidth
        if download_bandwidth is not UNSET:
            field_dict["download_bandwidth"] = download_bandwidth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sources = cast(list[str], d.pop("sources", UNSET))

        upload_bandwidth = d.pop("upload_bandwidth", UNSET)

        download_bandwidth = d.pop("download_bandwidth", UNSET)

        bandwidth_limit = cls(
            sources=sources,
            upload_bandwidth=upload_bandwidth,
            download_bandwidth=download_bandwidth,
        )

        bandwidth_limit.additional_properties = d
        return bandwidth_limit

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
