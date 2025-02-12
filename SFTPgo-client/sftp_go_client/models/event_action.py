from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_action_types import EventActionTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_event_action_options import BaseEventActionOptions
    from ..models.event_action_options import EventActionOptions


T = TypeVar("T", bound="EventAction")


@_attrs_define
class EventAction:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]): unique name
        description (Union[Unset, str]): optional description
        type_ (Union[Unset, EventActionTypes]): Supported event action types:
              * `1` - HTTP
              * `2` - Command
              * `3` - Email
              * `4` - Backup
              * `5` - User quota reset
              * `6` - Folder quota reset
              * `7` - Transfer quota reset
              * `8` - Data retention check
              * `9` - Filesystem
              * `11` - Password expiration check
              * `12` - User expiration check
              * `13` - Identity Provider account check
              * `14` - User inactivity check
              * `15` - Rotate log file
        options (Union[Unset, BaseEventActionOptions]):
        rules (Union[Unset, list[str]]): list of event rules names associated with this action
        order (Union[Unset, int]): execution order
        relation_options (Union[Unset, EventActionOptions]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, EventActionTypes] = UNSET
    options: Union[Unset, "BaseEventActionOptions"] = UNSET
    rules: Union[Unset, list[str]] = UNSET
    order: Union[Unset, int] = UNSET
    relation_options: Union[Unset, "EventActionOptions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        type_: Union[Unset, int] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        rules: Union[Unset, list[str]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules

        order = self.order

        relation_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relation_options, Unset):
            relation_options = self.relation_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if options is not UNSET:
            field_dict["options"] = options
        if rules is not UNSET:
            field_dict["rules"] = rules
        if order is not UNSET:
            field_dict["order"] = order
        if relation_options is not UNSET:
            field_dict["relation_options"] = relation_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.base_event_action_options import BaseEventActionOptions
        from ..models.event_action_options import EventActionOptions

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, EventActionTypes]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EventActionTypes(_type_)

        _options = d.pop("options", UNSET)
        options: Union[Unset, BaseEventActionOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BaseEventActionOptions.from_dict(_options)

        rules = cast(list[str], d.pop("rules", UNSET))

        order = d.pop("order", UNSET)

        _relation_options = d.pop("relation_options", UNSET)
        relation_options: Union[Unset, EventActionOptions]
        if isinstance(_relation_options, Unset):
            relation_options = UNSET
        else:
            relation_options = EventActionOptions.from_dict(_relation_options)

        event_action = cls(
            id=id,
            name=name,
            description=description,
            type_=type_,
            options=options,
            rules=rules,
            order=order,
            relation_options=relation_options,
        )

        event_action.additional_properties = d
        return event_action

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
