from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gcs_config_automatic_credentials import GCSConfigAutomaticCredentials
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret import Secret


T = TypeVar("T", bound="GCSConfig")


@_attrs_define
class GCSConfig:
    """Google Cloud Storage configuration details. The "credentials" field must be populated only when adding/updating a
    user. It will be always omitted, since there are sensitive data, when you search/get users

        Attributes:
            bucket (Union[Unset, str]):
            credentials (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must
                provide a payload and set the status to "Plain". The encryption key and additional data will be generated
                automatically. If you set the status to "Redacted" the existing secret will be preserved
            automatic_credentials (Union[Unset, GCSConfigAutomaticCredentials]): Automatic credentials:
                  * `0` - disabled, explicit credentials, using a JSON credentials file, must be provided. This is the default
                value if the field is null
                  * `1` - enabled, we try to use the Application Default Credentials (ADC) strategy to find your application's
                credentials
            storage_class (Union[Unset, str]):
            acl (Union[Unset, str]): The ACL to apply to uploaded objects. Leave empty to use the default ACL. For more
                information and available ACLs, refer to the JSON API here: https://cloud.google.com/storage/docs/access-
                control/lists#predefined-acl
            key_prefix (Union[Unset, str]): key_prefix is similar to a chroot directory for a local filesystem. If specified
                the user will only see contents that starts with this prefix and so you can restrict access to a specific
                virtual folder. The prefix, if not empty, must not start with "/" and must end with "/". If empty the whole
                bucket contents will be available Example: folder/subfolder/.
            upload_part_size (Union[Unset, int]): The buffer size (in MB) to use for multipart uploads. The default value is
                16MB. 0 means use the default
            upload_part_max_time (Union[Unset, int]): The maximum time allowed, in seconds, to upload a single chunk. The
                default value is 32. 0 means use the default
    """

    bucket: Union[Unset, str] = UNSET
    credentials: Union[Unset, "Secret"] = UNSET
    automatic_credentials: Union[Unset, GCSConfigAutomaticCredentials] = UNSET
    storage_class: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    key_prefix: Union[Unset, str] = UNSET
    upload_part_size: Union[Unset, int] = UNSET
    upload_part_max_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        automatic_credentials: Union[Unset, int] = UNSET
        if not isinstance(self.automatic_credentials, Unset):
            automatic_credentials = self.automatic_credentials.value

        storage_class = self.storage_class

        acl = self.acl

        key_prefix = self.key_prefix

        upload_part_size = self.upload_part_size

        upload_part_max_time = self.upload_part_max_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if automatic_credentials is not UNSET:
            field_dict["automatic_credentials"] = automatic_credentials
        if storage_class is not UNSET:
            field_dict["storage_class"] = storage_class
        if acl is not UNSET:
            field_dict["acl"] = acl
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix
        if upload_part_size is not UNSET:
            field_dict["upload_part_size"] = upload_part_size
        if upload_part_max_time is not UNSET:
            field_dict["upload_part_max_time"] = upload_part_max_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.secret import Secret

        d = src_dict.copy()
        bucket = d.pop("bucket", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, Secret]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = Secret.from_dict(_credentials)

        _automatic_credentials = d.pop("automatic_credentials", UNSET)
        automatic_credentials: Union[Unset, GCSConfigAutomaticCredentials]
        if isinstance(_automatic_credentials, Unset):
            automatic_credentials = UNSET
        else:
            automatic_credentials = GCSConfigAutomaticCredentials(_automatic_credentials)

        storage_class = d.pop("storage_class", UNSET)

        acl = d.pop("acl", UNSET)

        key_prefix = d.pop("key_prefix", UNSET)

        upload_part_size = d.pop("upload_part_size", UNSET)

        upload_part_max_time = d.pop("upload_part_max_time", UNSET)

        gcs_config = cls(
            bucket=bucket,
            credentials=credentials,
            automatic_credentials=automatic_credentials,
            storage_class=storage_class,
            acl=acl,
            key_prefix=key_prefix,
            upload_part_size=upload_part_size,
            upload_part_max_time=upload_part_max_time,
        )

        gcs_config.additional_properties = d
        return gcs_config

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
