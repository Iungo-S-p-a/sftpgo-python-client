from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filesystem_config import FilesystemConfig


T = TypeVar("T", bound="BaseVirtualFolder")


@_attrs_define
class BaseVirtualFolder:
    """Defines the filesystem for the virtual folder and the used quota limits. The same folder can be shared among
    multiple users and each user can have different quota limits or a different virtual path.

        Attributes:
            id (Union[Unset, int]):
            name (Union[Unset, str]): unique name for this virtual folder
            mapped_path (Union[Unset, str]): absolute filesystem path to use as virtual folder
            description (Union[Unset, str]): optional description
            used_quota_size (Union[Unset, int]):
            used_quota_files (Union[Unset, int]):
            last_quota_update (Union[Unset, int]): Last quota update as unix timestamp in milliseconds
            users (Union[Unset, list[str]]): list of usernames associated with this virtual folder
            filesystem (Union[Unset, FilesystemConfig]): Storage filesystem details
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    mapped_path: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    used_quota_size: Union[Unset, int] = UNSET
    used_quota_files: Union[Unset, int] = UNSET
    last_quota_update: Union[Unset, int] = UNSET
    users: Union[Unset, list[str]] = UNSET
    filesystem: Union[Unset, "FilesystemConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        mapped_path = self.mapped_path

        description = self.description

        used_quota_size = self.used_quota_size

        used_quota_files = self.used_quota_files

        last_quota_update = self.last_quota_update

        users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        filesystem: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filesystem, Unset):
            filesystem = self.filesystem.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if mapped_path is not UNSET:
            field_dict["mapped_path"] = mapped_path
        if description is not UNSET:
            field_dict["description"] = description
        if used_quota_size is not UNSET:
            field_dict["used_quota_size"] = used_quota_size
        if used_quota_files is not UNSET:
            field_dict["used_quota_files"] = used_quota_files
        if last_quota_update is not UNSET:
            field_dict["last_quota_update"] = last_quota_update
        if users is not UNSET:
            field_dict["users"] = users
        if filesystem is not UNSET:
            field_dict["filesystem"] = filesystem

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.filesystem_config import FilesystemConfig

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        mapped_path = d.pop("mapped_path", UNSET)

        description = d.pop("description", UNSET)

        used_quota_size = d.pop("used_quota_size", UNSET)

        used_quota_files = d.pop("used_quota_files", UNSET)

        last_quota_update = d.pop("last_quota_update", UNSET)

        users = cast(list[str], d.pop("users", UNSET))

        _filesystem = d.pop("filesystem", UNSET)
        filesystem: Union[Unset, FilesystemConfig]
        if isinstance(_filesystem, Unset):
            filesystem = UNSET
        else:
            filesystem = FilesystemConfig.from_dict(_filesystem)

        base_virtual_folder = cls(
            id=id,
            name=name,
            mapped_path=mapped_path,
            description=description,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            users=users,
            filesystem=filesystem,
        )

        base_virtual_folder.additional_properties = d
        return base_virtual_folder

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
