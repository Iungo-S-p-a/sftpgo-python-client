from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ftp_passive_port_range import FTPPassivePortRange
    from ..models.ftpd_binding import FTPDBinding


T = TypeVar("T", bound="FTPServiceStatus")


@_attrs_define
class FTPServiceStatus:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        bindings (Union[None, Unset, list['FTPDBinding']]):
        passive_port_range (Union[Unset, FTPPassivePortRange]):
    """

    is_active: Union[Unset, bool] = UNSET
    bindings: Union[None, Unset, list["FTPDBinding"]] = UNSET
    passive_port_range: Union[Unset, "FTPPassivePortRange"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_active = self.is_active

        bindings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.bindings, Unset):
            bindings = UNSET
        elif isinstance(self.bindings, list):
            bindings = []
            for bindings_type_0_item_data in self.bindings:
                bindings_type_0_item = bindings_type_0_item_data.to_dict()
                bindings.append(bindings_type_0_item)

        else:
            bindings = self.bindings

        passive_port_range: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.passive_port_range, Unset):
            passive_port_range = self.passive_port_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if bindings is not UNSET:
            field_dict["bindings"] = bindings
        if passive_port_range is not UNSET:
            field_dict["passive_port_range"] = passive_port_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ftp_passive_port_range import FTPPassivePortRange
        from ..models.ftpd_binding import FTPDBinding

        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        def _parse_bindings(data: object) -> Union[None, Unset, list["FTPDBinding"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bindings_type_0 = []
                _bindings_type_0 = data
                for bindings_type_0_item_data in _bindings_type_0:
                    bindings_type_0_item = FTPDBinding.from_dict(bindings_type_0_item_data)

                    bindings_type_0.append(bindings_type_0_item)

                return bindings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["FTPDBinding"]], data)

        bindings = _parse_bindings(d.pop("bindings", UNSET))

        _passive_port_range = d.pop("passive_port_range", UNSET)
        passive_port_range: Union[Unset, FTPPassivePortRange]
        if isinstance(_passive_port_range, Unset):
            passive_port_range = UNSET
        else:
            passive_port_range = FTPPassivePortRange.from_dict(_passive_port_range)

        ftp_service_status = cls(
            is_active=is_active,
            bindings=bindings,
            passive_port_range=passive_port_range,
        )

        ftp_service_status.additional_properties = d
        return ftp_service_status

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
