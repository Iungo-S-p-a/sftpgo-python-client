from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="HTTPPart")


@_attrs_define
class HTTPPart:
    """
    Attributes:
        name (Union[Unset, str]):
        headers (Union[Unset, list['KeyValue']]): Additional headers. Content-Disposition header is automatically set.
            Content-Type header is automatically detect for files to attach
        filepath (Union[Unset, str]): path to the file to be sent as an attachment
        body (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    headers: Union[Unset, list["KeyValue"]] = UNSET
    filepath: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        filepath = self.filepath

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if headers is not UNSET:
            field_dict["headers"] = headers
        if filepath is not UNSET:
            field_dict["filepath"] = filepath
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.key_value import KeyValue

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        headers = []
        _headers = d.pop("headers", UNSET)
        for headers_item_data in _headers or []:
            headers_item = KeyValue.from_dict(headers_item_data)

            headers.append(headers_item)

        filepath = d.pop("filepath", UNSET)

        body = d.pop("body", UNSET)

        http_part = cls(
            name=name,
            headers=headers,
            filepath=filepath,
            body=body,
        )

        http_part.additional_properties = d
        return http_part

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
