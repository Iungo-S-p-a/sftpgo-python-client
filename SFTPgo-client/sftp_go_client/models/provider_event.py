from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_event_action import ProviderEventAction
from ..models.provider_event_object_type import ProviderEventObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderEvent")


@_attrs_define
class ProviderEvent:
    """
    Attributes:
        id (Union[Unset, str]):
        timestamp (Union[Unset, int]): unix timestamp in nanoseconds
        action (Union[Unset, ProviderEventAction]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        object_type (Union[Unset, ProviderEventObjectType]):
        object_name (Union[Unset, str]):
        object_data (Union[Unset, str]): base64 of the JSON serialized object with sensitive fields removed
        role (Union[Unset, str]):
        instance_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, int] = UNSET
    action: Union[Unset, ProviderEventAction] = UNSET
    username: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    object_type: Union[Unset, ProviderEventObjectType] = UNSET
    object_name: Union[Unset, str] = UNSET
    object_data: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        timestamp = self.timestamp

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        username = self.username

        ip = self.ip

        object_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        object_name = self.object_name

        object_data = self.object_data

        role = self.role

        instance_id = self.instance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if action is not UNSET:
            field_dict["action"] = action
        if username is not UNSET:
            field_dict["username"] = username
        if ip is not UNSET:
            field_dict["ip"] = ip
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if object_name is not UNSET:
            field_dict["object_name"] = object_name
        if object_data is not UNSET:
            field_dict["object_data"] = object_data
        if role is not UNSET:
            field_dict["role"] = role
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, ProviderEventAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ProviderEventAction(_action)

        username = d.pop("username", UNSET)

        ip = d.pop("ip", UNSET)

        _object_type = d.pop("object_type", UNSET)
        object_type: Union[Unset, ProviderEventObjectType]
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = ProviderEventObjectType(_object_type)

        object_name = d.pop("object_name", UNSET)

        object_data = d.pop("object_data", UNSET)

        role = d.pop("role", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        provider_event = cls(
            id=id,
            timestamp=timestamp,
            action=action,
            username=username,
            ip=ip,
            object_type=object_type,
            object_name=object_name,
            object_data=object_data,
            role=role,
            instance_id=instance_id,
        )

        provider_event.additional_properties = d
        return provider_event

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
