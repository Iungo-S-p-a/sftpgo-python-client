from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminProfile")


@_attrs_define
class AdminProfile:
    """
    Attributes:
        email (Union[Unset, str]):
        description (Union[Unset, str]):
        allow_api_key_auth (Union[Unset, bool]): If enabled, you can impersonate this admin, in REST API, using an API
            key. If disabled admin credentials are required for impersonation
    """

    email: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    allow_api_key_auth: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        description = self.description

        allow_api_key_auth = self.allow_api_key_auth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if description is not UNSET:
            field_dict["description"] = description
        if allow_api_key_auth is not UNSET:
            field_dict["allow_api_key_auth"] = allow_api_key_auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        description = d.pop("description", UNSET)

        allow_api_key_auth = d.pop("allow_api_key_auth", UNSET)

        admin_profile = cls(
            email=email,
            description=description,
            allow_api_key_auth=allow_api_key_auth,
        )

        admin_profile.additional_properties = d
        return admin_profile

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
