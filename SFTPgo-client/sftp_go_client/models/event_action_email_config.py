from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_action_email_config_content_type import EventActionEmailConfigContentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventActionEmailConfig")


@_attrs_define
class EventActionEmailConfig:
    """
    Attributes:
        recipients (Union[Unset, list[str]]):
        bcc (Union[Unset, list[str]]):
        subject (Union[Unset, str]):
        body (Union[Unset, str]):
        content_type (Union[Unset, EventActionEmailConfigContentType]): Content type:
              * `0` text/plain
              * `1` text/html
        attachments (Union[Unset, list[str]]): list of file paths to attach. The total size is limited to 10 MB
    """

    recipients: Union[Unset, list[str]] = UNSET
    bcc: Union[Unset, list[str]] = UNSET
    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    content_type: Union[Unset, EventActionEmailConfigContentType] = UNSET
    attachments: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipients: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        bcc: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bcc, Unset):
            bcc = self.bcc

        subject = self.subject

        body = self.body

        content_type: Union[Unset, int] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        attachments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        recipients = cast(list[str], d.pop("recipients", UNSET))

        bcc = cast(list[str], d.pop("bcc", UNSET))

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        _content_type = d.pop("content_type", UNSET)
        content_type: Union[Unset, EventActionEmailConfigContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = EventActionEmailConfigContentType(_content_type)

        attachments = cast(list[str], d.pop("attachments", UNSET))

        event_action_email_config = cls(
            recipients=recipients,
            bcc=bcc,
            subject=subject,
            body=body,
            content_type=content_type,
            attachments=attachments,
        )

        event_action_email_config.additional_properties = d
        return event_action_email_config

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
