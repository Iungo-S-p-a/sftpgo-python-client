from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateAdminTotpSecretResponse200")


@_attrs_define
class GenerateAdminTotpSecretResponse200:
    """
    Attributes:
        config_name (Union[Unset, str]):
        issuer (Union[Unset, str]):
        secret (Union[Unset, str]):
        url (Union[Unset, str]):
        qr_code (Union[Unset, str]): QR code png encoded as BASE64
    """

    config_name: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    qr_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_name = self.config_name

        issuer = self.issuer

        secret = self.secret

        url = self.url

        qr_code = self.qr_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_name is not UNSET:
            field_dict["config_name"] = config_name
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if secret is not UNSET:
            field_dict["secret"] = secret
        if url is not UNSET:
            field_dict["url"] = url
        if qr_code is not UNSET:
            field_dict["qr_code"] = qr_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        config_name = d.pop("config_name", UNSET)

        issuer = d.pop("issuer", UNSET)

        secret = d.pop("secret", UNSET)

        url = d.pop("url", UNSET)

        qr_code = d.pop("qr_code", UNSET)

        generate_admin_totp_secret_response_200 = cls(
            config_name=config_name,
            issuer=issuer,
            secret=secret,
            url=url,
            qr_code=qr_code,
        )

        generate_admin_totp_secret_response_200.additional_properties = d
        return generate_admin_totp_secret_response_200

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
