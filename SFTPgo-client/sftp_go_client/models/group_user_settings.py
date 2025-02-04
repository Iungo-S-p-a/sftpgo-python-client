from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_user_filters import BaseUserFilters
    from ..models.filesystem_config import FilesystemConfig
    from ..models.group_user_settings_permissions import GroupUserSettingsPermissions


T = TypeVar("T", bound="GroupUserSettings")


@_attrs_define
class GroupUserSettings:
    """
    Attributes:
        home_dir (Union[Unset, str]):
        max_sessions (Union[Unset, int]):
        quota_size (Union[Unset, int]):
        quota_files (Union[Unset, int]):
        permissions (Union[Unset, GroupUserSettingsPermissions]): hash map with directory as key and an array of
            permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required
            Example: {'/': ['*'], '/somedir': ['list', 'download']}.
        upload_bandwidth (Union[Unset, int]): Maximum upload bandwidth as KB/s
        download_bandwidth (Union[Unset, int]): Maximum download bandwidth as KB/s
        upload_data_transfer (Union[Unset, int]): Maximum data transfer allowed for uploads as MB
        download_data_transfer (Union[Unset, int]): Maximum data transfer allowed for downloads as MB
        total_data_transfer (Union[Unset, int]): Maximum total data transfer as MB
        expires_in (Union[Unset, int]): Account expiration in number of days from creation. 0 means no expiration
        filters (Union[Unset, BaseUserFilters]): Additional user options
        filesystem (Union[Unset, FilesystemConfig]): Storage filesystem details
    """

    home_dir: Union[Unset, str] = UNSET
    max_sessions: Union[Unset, int] = UNSET
    quota_size: Union[Unset, int] = UNSET
    quota_files: Union[Unset, int] = UNSET
    permissions: Union[Unset, "GroupUserSettingsPermissions"] = UNSET
    upload_bandwidth: Union[Unset, int] = UNSET
    download_bandwidth: Union[Unset, int] = UNSET
    upload_data_transfer: Union[Unset, int] = UNSET
    download_data_transfer: Union[Unset, int] = UNSET
    total_data_transfer: Union[Unset, int] = UNSET
    expires_in: Union[Unset, int] = UNSET
    filters: Union[Unset, "BaseUserFilters"] = UNSET
    filesystem: Union[Unset, "FilesystemConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        home_dir = self.home_dir

        max_sessions = self.max_sessions

        quota_size = self.quota_size

        quota_files = self.quota_files

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        upload_bandwidth = self.upload_bandwidth

        download_bandwidth = self.download_bandwidth

        upload_data_transfer = self.upload_data_transfer

        download_data_transfer = self.download_data_transfer

        total_data_transfer = self.total_data_transfer

        expires_in = self.expires_in

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        filesystem: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filesystem, Unset):
            filesystem = self.filesystem.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if home_dir is not UNSET:
            field_dict["home_dir"] = home_dir
        if max_sessions is not UNSET:
            field_dict["max_sessions"] = max_sessions
        if quota_size is not UNSET:
            field_dict["quota_size"] = quota_size
        if quota_files is not UNSET:
            field_dict["quota_files"] = quota_files
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if upload_bandwidth is not UNSET:
            field_dict["upload_bandwidth"] = upload_bandwidth
        if download_bandwidth is not UNSET:
            field_dict["download_bandwidth"] = download_bandwidth
        if upload_data_transfer is not UNSET:
            field_dict["upload_data_transfer"] = upload_data_transfer
        if download_data_transfer is not UNSET:
            field_dict["download_data_transfer"] = download_data_transfer
        if total_data_transfer is not UNSET:
            field_dict["total_data_transfer"] = total_data_transfer
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if filters is not UNSET:
            field_dict["filters"] = filters
        if filesystem is not UNSET:
            field_dict["filesystem"] = filesystem

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.base_user_filters import BaseUserFilters
        from ..models.filesystem_config import FilesystemConfig
        from ..models.group_user_settings_permissions import GroupUserSettingsPermissions

        d = src_dict.copy()
        home_dir = d.pop("home_dir", UNSET)

        max_sessions = d.pop("max_sessions", UNSET)

        quota_size = d.pop("quota_size", UNSET)

        quota_files = d.pop("quota_files", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, GroupUserSettingsPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = GroupUserSettingsPermissions.from_dict(_permissions)

        upload_bandwidth = d.pop("upload_bandwidth", UNSET)

        download_bandwidth = d.pop("download_bandwidth", UNSET)

        upload_data_transfer = d.pop("upload_data_transfer", UNSET)

        download_data_transfer = d.pop("download_data_transfer", UNSET)

        total_data_transfer = d.pop("total_data_transfer", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, BaseUserFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = BaseUserFilters.from_dict(_filters)

        _filesystem = d.pop("filesystem", UNSET)
        filesystem: Union[Unset, FilesystemConfig]
        if isinstance(_filesystem, Unset):
            filesystem = UNSET
        else:
            filesystem = FilesystemConfig.from_dict(_filesystem)

        group_user_settings = cls(
            home_dir=home_dir,
            max_sessions=max_sessions,
            quota_size=quota_size,
            quota_files=quota_files,
            permissions=permissions,
            upload_bandwidth=upload_bandwidth,
            download_bandwidth=download_bandwidth,
            upload_data_transfer=upload_data_transfer,
            download_data_transfer=download_data_transfer,
            total_data_transfer=total_data_transfer,
            expires_in=expires_in,
            filters=filters,
            filesystem=filesystem,
        )

        group_user_settings.additional_properties = d
        return group_user_settings

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
