from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_action_idp_account_check_mode import EventActionIDPAccountCheckMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventActionIDPAccountCheck")


@_attrs_define
class EventActionIDPAccountCheck:
    """
    Attributes:
        mode (Union[Unset, EventActionIDPAccountCheckMode]): Account check mode:
              * `0` Create or update the account
              * `1` Create the account if it doesn't exist
        template_user (Union[Unset, str]): SFTPGo user template in JSON format
        template_admin (Union[Unset, str]): SFTPGo admin template in JSON format
    """

    mode: Union[Unset, EventActionIDPAccountCheckMode] = UNSET
    template_user: Union[Unset, str] = UNSET
    template_admin: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, int] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        template_user = self.template_user

        template_admin = self.template_admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if template_user is not UNSET:
            field_dict["template_user"] = template_user
        if template_admin is not UNSET:
            field_dict["template_admin"] = template_admin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, EventActionIDPAccountCheckMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = EventActionIDPAccountCheckMode(_mode)

        template_user = d.pop("template_user", UNSET)

        template_admin = d.pop("template_admin", UNSET)

        event_action_idp_account_check = cls(
            mode=mode,
            template_user=template_user,
            template_admin=template_admin,
        )

        event_action_idp_account_check.additional_properties = d
        return event_action_idp_account_check

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
