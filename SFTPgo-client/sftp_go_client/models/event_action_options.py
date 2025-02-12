from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventActionOptions")


@_attrs_define
class EventActionOptions:
    """
    Attributes:
        is_failure_action (Union[Unset, bool]):
        stop_on_failure (Union[Unset, bool]):
        execute_sync (Union[Unset, bool]):
    """

    is_failure_action: Union[Unset, bool] = UNSET
    stop_on_failure: Union[Unset, bool] = UNSET
    execute_sync: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_failure_action = self.is_failure_action

        stop_on_failure = self.stop_on_failure

        execute_sync = self.execute_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_failure_action is not UNSET:
            field_dict["is_failure_action"] = is_failure_action
        if stop_on_failure is not UNSET:
            field_dict["stop_on_failure"] = stop_on_failure
        if execute_sync is not UNSET:
            field_dict["execute_sync"] = execute_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        is_failure_action = d.pop("is_failure_action", UNSET)

        stop_on_failure = d.pop("stop_on_failure", UNSET)

        execute_sync = d.pop("execute_sync", UNSET)

        event_action_options = cls(
            is_failure_action=is_failure_action,
            stop_on_failure=stop_on_failure,
            execute_sync=execute_sync,
        )

        event_action_options.additional_properties = d
        return event_action_options

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
