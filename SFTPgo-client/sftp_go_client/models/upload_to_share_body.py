import json
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UploadToShareBody")


@_attrs_define
class UploadToShareBody:
    """
    Attributes:
        filenames (Union[Unset, list[File]]):
    """

    filenames: Union[Unset, list[File]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filenames: Union[Unset, list[FileJsonType]] = UNSET
        if not isinstance(self.filenames, Unset):
            filenames = []
            for filenames_item_data in self.filenames:
                filenames_item = filenames_item_data.to_tuple()

                filenames.append(filenames_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filenames is not UNSET:
            field_dict["filenames"] = filenames

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        filenames: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.filenames, Unset):
            _temp_filenames = []
            for filenames_item_data in self.filenames:
                filenames_item = filenames_item_data.to_tuple()

                _temp_filenames.append(filenames_item)
            filenames = (None, json.dumps(_temp_filenames).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if filenames is not UNSET:
            field_dict["filenames"] = filenames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        filenames = []
        _filenames = d.pop("filenames", UNSET)
        for filenames_item_data in _filenames or []:
            filenames_item = File(payload=BytesIO(filenames_item_data))

            filenames.append(filenames_item)

        upload_to_share_body = cls(
            filenames=filenames,
        )

        upload_to_share_body.additional_properties = d
        return upload_to_share_body

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
