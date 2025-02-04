from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret import Secret


T = TypeVar("T", bound="CryptFsConfig")


@_attrs_define
class CryptFsConfig:
    """Crypt filesystem configuration details

    Attributes:
        passphrase (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must
            provide a payload and set the status to "Plain". The encryption key and additional data will be generated
            automatically. If you set the status to "Redacted" the existing secret will be preserved
        read_buffer_size (Union[Unset, int]): The read buffer size, as MB, to use for downloads. 0 means no buffering,
            that's fine in most use cases.
        write_buffer_size (Union[Unset, int]): The write buffer size, as MB, to use for uploads. 0 means no buffering,
            that's fine in most use cases.
    """

    passphrase: Union[Unset, "Secret"] = UNSET
    read_buffer_size: Union[Unset, int] = UNSET
    write_buffer_size: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        passphrase: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.passphrase, Unset):
            passphrase = self.passphrase.to_dict()

        read_buffer_size = self.read_buffer_size

        write_buffer_size = self.write_buffer_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase
        if read_buffer_size is not UNSET:
            field_dict["read_buffer_size"] = read_buffer_size
        if write_buffer_size is not UNSET:
            field_dict["write_buffer_size"] = write_buffer_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.secret import Secret

        d = src_dict.copy()
        _passphrase = d.pop("passphrase", UNSET)
        passphrase: Union[Unset, Secret]
        if isinstance(_passphrase, Unset):
            passphrase = UNSET
        else:
            passphrase = Secret.from_dict(_passphrase)

        read_buffer_size = d.pop("read_buffer_size", UNSET)

        write_buffer_size = d.pop("write_buffer_size", UNSET)

        crypt_fs_config = cls(
            passphrase=passphrase,
            read_buffer_size=read_buffer_size,
            write_buffer_size=write_buffer_size,
        )

        crypt_fs_config.additional_properties = d
        return crypt_fs_config

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
