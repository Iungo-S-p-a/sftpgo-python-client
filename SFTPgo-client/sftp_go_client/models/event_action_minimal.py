from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_action_options import EventActionOptions


T = TypeVar("T", bound="EventActionMinimal")


@_attrs_define
class EventActionMinimal:
    """
    Attributes:
        name (Union[Unset, str]):
        order (Union[Unset, int]): execution order
        relation_options (Union[Unset, EventActionOptions]):
    """

    name: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    relation_options: Union[Unset, "EventActionOptions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        order = self.order

        relation_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relation_options, Unset):
            relation_options = self.relation_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if relation_options is not UNSET:
            field_dict["relation_options"] = relation_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.event_action_options import EventActionOptions

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        _relation_options = d.pop("relation_options", UNSET)
        relation_options: Union[Unset, EventActionOptions]
        if isinstance(_relation_options, Unset):
            relation_options = UNSET
        else:
            relation_options = EventActionOptions.from_dict(_relation_options)

        event_action_minimal = cls(
            name=name,
            order=order,
            relation_options=relation_options,
        )

        event_action_minimal.additional_properties = d
        return event_action_minimal

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
