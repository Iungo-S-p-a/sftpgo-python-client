from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_preferences import AdminPreferences
    from ..models.base_totp_config import BaseTOTPConfig
    from ..models.recovery_code import RecoveryCode


T = TypeVar("T", bound="AdminFilters")


@_attrs_define
class AdminFilters:
    """
    Attributes:
        allow_list (Union[Unset, list[str]]): only clients connecting from these IP/Mask are allowed. IP/Mask must be in
            CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32" Example:
            ['192.0.2.0/24', '2001:db8::/32'].
        allow_api_key_auth (Union[Unset, bool]): API key auth allows to impersonate this administrator with an API key
        require_two_factor (Union[Unset, bool]):
        require_password_change (Union[Unset, bool]):
        totp_config (Union[Unset, BaseTOTPConfig]):
        recovery_codes (Union[Unset, list['RecoveryCode']]):
        preferences (Union[Unset, AdminPreferences]):
    """

    allow_list: Union[Unset, list[str]] = UNSET
    allow_api_key_auth: Union[Unset, bool] = UNSET
    require_two_factor: Union[Unset, bool] = UNSET
    require_password_change: Union[Unset, bool] = UNSET
    totp_config: Union[Unset, "BaseTOTPConfig"] = UNSET
    recovery_codes: Union[Unset, list["RecoveryCode"]] = UNSET
    preferences: Union[Unset, "AdminPreferences"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allow_list, Unset):
            allow_list = self.allow_list

        allow_api_key_auth = self.allow_api_key_auth

        require_two_factor = self.require_two_factor

        require_password_change = self.require_password_change

        totp_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.totp_config, Unset):
            totp_config = self.totp_config.to_dict()

        recovery_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recovery_codes, Unset):
            recovery_codes = []
            for recovery_codes_item_data in self.recovery_codes:
                recovery_codes_item = recovery_codes_item_data.to_dict()
                recovery_codes.append(recovery_codes_item)

        preferences: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_list is not UNSET:
            field_dict["allow_list"] = allow_list
        if allow_api_key_auth is not UNSET:
            field_dict["allow_api_key_auth"] = allow_api_key_auth
        if require_two_factor is not UNSET:
            field_dict["require_two_factor"] = require_two_factor
        if require_password_change is not UNSET:
            field_dict["require_password_change"] = require_password_change
        if totp_config is not UNSET:
            field_dict["totp_config"] = totp_config
        if recovery_codes is not UNSET:
            field_dict["recovery_codes"] = recovery_codes
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.admin_preferences import AdminPreferences
        from ..models.base_totp_config import BaseTOTPConfig
        from ..models.recovery_code import RecoveryCode

        d = src_dict.copy()
        allow_list = cast(list[str], d.pop("allow_list", UNSET))

        allow_api_key_auth = d.pop("allow_api_key_auth", UNSET)

        require_two_factor = d.pop("require_two_factor", UNSET)

        require_password_change = d.pop("require_password_change", UNSET)

        _totp_config = d.pop("totp_config", UNSET)
        totp_config: Union[Unset, BaseTOTPConfig]
        if isinstance(_totp_config, Unset):
            totp_config = UNSET
        else:
            totp_config = BaseTOTPConfig.from_dict(_totp_config)

        recovery_codes = []
        _recovery_codes = d.pop("recovery_codes", UNSET)
        for recovery_codes_item_data in _recovery_codes or []:
            recovery_codes_item = RecoveryCode.from_dict(recovery_codes_item_data)

            recovery_codes.append(recovery_codes_item)

        _preferences = d.pop("preferences", UNSET)
        preferences: Union[Unset, AdminPreferences]
        if isinstance(_preferences, Unset):
            preferences = UNSET
        else:
            preferences = AdminPreferences.from_dict(_preferences)

        admin_filters = cls(
            allow_list=allow_list,
            allow_api_key_auth=allow_api_key_auth,
            require_two_factor=require_two_factor,
            require_password_change=require_password_change,
            totp_config=totp_config,
            recovery_codes=recovery_codes,
            preferences=preferences,
        )

        admin_filters.additional_properties = d
        return admin_filters

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
