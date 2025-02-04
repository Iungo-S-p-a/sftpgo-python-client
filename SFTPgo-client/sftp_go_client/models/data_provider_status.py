from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataProviderStatus")


@_attrs_define
class DataProviderStatus:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        driver (Union[Unset, str]):
        error (Union[Unset, str]):
    """

    is_active: Union[Unset, bool] = UNSET
    driver: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_active = self.is_active

        driver = self.driver

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if driver is not UNSET:
            field_dict["driver"] = driver
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        driver = d.pop("driver", UNSET)

        error = d.pop("error", UNSET)

        data_provider_status = cls(
            is_active=is_active,
            driver=driver,
            error=error,
        )

        data_provider_status.additional_properties = d
        return data_provider_status

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
