from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_event_rule_status import BaseEventRuleStatus
from ..models.event_trigger_types import EventTriggerTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_action_minimal import EventActionMinimal
    from ..models.event_conditions import EventConditions


T = TypeVar("T", bound="EventRuleMinimal")


@_attrs_define
class EventRuleMinimal:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]): unique name
        status (Union[Unset, BaseEventRuleStatus]): status:
              * `0` disabled
              * `1` enabled
        description (Union[Unset, str]): optional description
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds
        updated_at (Union[Unset, int]): last update time as unix timestamp in millisecond
        trigger (Union[Unset, EventTriggerTypes]): Supported event trigger types:
              * `1` - Filesystem event
              * `2` - Provider event
              * `3` - Schedule
              * `4` - IP blocked
              * `5` - Certificate renewal
              * `6` - On demand, like schedule but executed on demand
              * `7` - Identity provider login
        conditions (Union[Unset, EventConditions]):
        actions (Union[Unset, list['EventActionMinimal']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, BaseEventRuleStatus] = UNSET
    description: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    trigger: Union[Unset, EventTriggerTypes] = UNSET
    conditions: Union[Unset, "EventConditions"] = UNSET
    actions: Union[Unset, list["EventActionMinimal"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        trigger: Union[Unset, int] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        conditions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.event_action_minimal import EventActionMinimal
        from ..models.event_conditions import EventConditions

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BaseEventRuleStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BaseEventRuleStatus(_status)

        description = d.pop("description", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, EventTriggerTypes]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = EventTriggerTypes(_trigger)

        _conditions = d.pop("conditions", UNSET)
        conditions: Union[Unset, EventConditions]
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = EventConditions.from_dict(_conditions)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = EventActionMinimal.from_dict(actions_item_data)

            actions.append(actions_item)

        event_rule_minimal = cls(
            id=id,
            name=name,
            status=status,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            trigger=trigger,
            conditions=conditions,
            actions=actions,
        )

        event_rule_minimal.additional_properties = d
        return event_rule_minimal

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
