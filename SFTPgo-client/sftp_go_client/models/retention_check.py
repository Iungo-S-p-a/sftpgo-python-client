from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.retention_check_notification import RetentionCheckNotification
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder_retention import FolderRetention


T = TypeVar("T", bound="RetentionCheck")


@_attrs_define
class RetentionCheck:
    """
    Attributes:
        username (Union[Unset, str]): username to which the retention check refers
        folders (Union[Unset, list['FolderRetention']]):
        start_time (Union[Unset, int]): check start time as unix timestamp in milliseconds
        notifications (Union[Unset, list[RetentionCheckNotification]]):
        email (Union[Unset, str]): if the notification method is set to "Email", this is the e-mail address that
            receives the retention check report. This field is automatically set to the email address associated with the
            administrator starting the check
    """

    username: Union[Unset, str] = UNSET
    folders: Union[Unset, list["FolderRetention"]] = UNSET
    start_time: Union[Unset, int] = UNSET
    notifications: Union[Unset, list[RetentionCheckNotification]] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        folders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)

        start_time = self.start_time

        notifications: Union[Unset, list[str]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.value
                notifications.append(notifications_item)

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if folders is not UNSET:
            field_dict["folders"] = folders
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.folder_retention import FolderRetention

        d = src_dict.copy()
        username = d.pop("username", UNSET)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = FolderRetention.from_dict(folders_item_data)

            folders.append(folders_item)

        start_time = d.pop("start_time", UNSET)

        notifications = []
        _notifications = d.pop("notifications", UNSET)
        for notifications_item_data in _notifications or []:
            notifications_item = RetentionCheckNotification(notifications_item_data)

            notifications.append(notifications_item)

        email = d.pop("email", UNSET)

        retention_check = cls(
            username=username,
            folders=folders,
            start_time=start_time,
            notifications=notifications,
            email=email,
        )

        retention_check.additional_properties = d
        return retention_check

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
