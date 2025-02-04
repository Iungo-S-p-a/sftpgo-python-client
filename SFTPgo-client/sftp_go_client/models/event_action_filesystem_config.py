from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filesystem_action_types import FilesystemActionTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_action_fs_compress import EventActionFsCompress
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="EventActionFilesystemConfig")


@_attrs_define
class EventActionFilesystemConfig:
    """
    Attributes:
        type_ (Union[Unset, FilesystemActionTypes]): Supported filesystem action types:
              * `1` - Rename
              * `2` - Delete
              * `3` - Mkdis
              * `4` - Exist
              * `5` - Compress
              * `6` - Copy
        renames (Union[Unset, list['KeyValue']]):
        mkdirs (Union[Unset, list[str]]):
        deletes (Union[Unset, list[str]]):
        exist (Union[Unset, list[str]]):
        copy (Union[Unset, list['KeyValue']]):
        compress (Union[Unset, EventActionFsCompress]):
    """

    type_: Union[Unset, FilesystemActionTypes] = UNSET
    renames: Union[Unset, list["KeyValue"]] = UNSET
    mkdirs: Union[Unset, list[str]] = UNSET
    deletes: Union[Unset, list[str]] = UNSET
    exist: Union[Unset, list[str]] = UNSET
    copy: Union[Unset, list["KeyValue"]] = UNSET
    compress: Union[Unset, "EventActionFsCompress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, int] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        renames: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.renames, Unset):
            renames = []
            for renames_item_data in self.renames:
                renames_item = renames_item_data.to_dict()
                renames.append(renames_item)

        mkdirs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mkdirs, Unset):
            mkdirs = self.mkdirs

        deletes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.deletes, Unset):
            deletes = self.deletes

        exist: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exist, Unset):
            exist = self.exist

        copy: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.copy, Unset):
            copy = []
            for copy_item_data in self.copy:
                copy_item = copy_item_data.to_dict()
                copy.append(copy_item)

        compress: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compress, Unset):
            compress = self.compress.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if renames is not UNSET:
            field_dict["renames"] = renames
        if mkdirs is not UNSET:
            field_dict["mkdirs"] = mkdirs
        if deletes is not UNSET:
            field_dict["deletes"] = deletes
        if exist is not UNSET:
            field_dict["exist"] = exist
        if copy is not UNSET:
            field_dict["copy"] = copy
        if compress is not UNSET:
            field_dict["compress"] = compress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.event_action_fs_compress import EventActionFsCompress
        from ..models.key_value import KeyValue

        d = src_dict.copy()
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FilesystemActionTypes]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FilesystemActionTypes(_type_)

        renames = []
        _renames = d.pop("renames", UNSET)
        for renames_item_data in _renames or []:
            renames_item = KeyValue.from_dict(renames_item_data)

            renames.append(renames_item)

        mkdirs = cast(list[str], d.pop("mkdirs", UNSET))

        deletes = cast(list[str], d.pop("deletes", UNSET))

        exist = cast(list[str], d.pop("exist", UNSET))

        copy = []
        _copy = d.pop("copy", UNSET)
        for copy_item_data in _copy or []:
            copy_item = KeyValue.from_dict(copy_item_data)

            copy.append(copy_item)

        _compress = d.pop("compress", UNSET)
        compress: Union[Unset, EventActionFsCompress]
        if isinstance(_compress, Unset):
            compress = UNSET
        else:
            compress = EventActionFsCompress.from_dict(_compress)

        event_action_filesystem_config = cls(
            type_=type_,
            renames=renames,
            mkdirs=mkdirs,
            deletes=deletes,
            exist=exist,
            copy=copy,
            compress=compress,
        )

        event_action_filesystem_config.additional_properties = d
        return event_action_filesystem_config

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
