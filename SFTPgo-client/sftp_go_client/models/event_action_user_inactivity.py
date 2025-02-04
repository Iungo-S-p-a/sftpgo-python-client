from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventActionUserInactivity")


@_attrs_define
class EventActionUserInactivity:
    """
    Attributes:
        disable_threshold (Union[Unset, int]): Inactivity threshold, in days, before disabling the account
        delete_threshold (Union[Unset, int]): Inactivity threshold, in days, before deleting the account
    """

    disable_threshold: Union[Unset, int] = UNSET
    delete_threshold: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_threshold = self.disable_threshold

        delete_threshold = self.delete_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable_threshold is not UNSET:
            field_dict["disable_threshold"] = disable_threshold
        if delete_threshold is not UNSET:
            field_dict["delete_threshold"] = delete_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        disable_threshold = d.pop("disable_threshold", UNSET)

        delete_threshold = d.pop("delete_threshold", UNSET)

        event_action_user_inactivity = cls(
            disable_threshold=disable_threshold,
            delete_threshold=delete_threshold,
        )

        event_action_user_inactivity.additional_properties = d
        return event_action_user_inactivity

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
