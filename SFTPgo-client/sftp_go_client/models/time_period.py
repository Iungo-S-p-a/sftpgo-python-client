from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_period_day_of_week import TimePeriodDayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimePeriod")


@_attrs_define
class TimePeriod:
    """
    Attributes:
        day_of_week (Union[Unset, TimePeriodDayOfWeek]): Day of week, 0 Sunday, 6 Saturday
        from_ (Union[Unset, str]): Start time in HH:MM format
        to (Union[Unset, str]): End time in HH:MM format
    """

    day_of_week: Union[Unset, TimePeriodDayOfWeek] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_of_week: Union[Unset, int] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day_of_week is not UNSET:
            field_dict["day_of_week"] = day_of_week
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _day_of_week = d.pop("day_of_week", UNSET)
        day_of_week: Union[Unset, TimePeriodDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = TimePeriodDayOfWeek(_day_of_week)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        time_period = cls(
            day_of_week=day_of_week,
            from_=from_,
            to=to,
        )

        time_period.additional_properties = d
        return time_period

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
