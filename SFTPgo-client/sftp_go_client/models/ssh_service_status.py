from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ssh_authentications import SSHAuthentications
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssh_binding import SSHBinding
    from ..models.ssh_host_key import SSHHostKey


T = TypeVar("T", bound="SSHServiceStatus")


@_attrs_define
class SSHServiceStatus:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        bindings (Union[None, Unset, list['SSHBinding']]):
        host_keys (Union[None, Unset, list['SSHHostKey']]):
        ssh_commands (Union[Unset, list[str]]):
        authentications (Union[Unset, list[SSHAuthentications]]):
        public_key_algorithms (Union[Unset, list[str]]):
        macs (Union[Unset, list[str]]):
        kex_algorithms (Union[Unset, list[str]]):
        ciphers (Union[Unset, list[str]]):
    """

    is_active: Union[Unset, bool] = UNSET
    bindings: Union[None, Unset, list["SSHBinding"]] = UNSET
    host_keys: Union[None, Unset, list["SSHHostKey"]] = UNSET
    ssh_commands: Union[Unset, list[str]] = UNSET
    authentications: Union[Unset, list[SSHAuthentications]] = UNSET
    public_key_algorithms: Union[Unset, list[str]] = UNSET
    macs: Union[Unset, list[str]] = UNSET
    kex_algorithms: Union[Unset, list[str]] = UNSET
    ciphers: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_active = self.is_active

        bindings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.bindings, Unset):
            bindings = UNSET
        elif isinstance(self.bindings, list):
            bindings = []
            for bindings_type_0_item_data in self.bindings:
                bindings_type_0_item = bindings_type_0_item_data.to_dict()
                bindings.append(bindings_type_0_item)

        else:
            bindings = self.bindings

        host_keys: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.host_keys, Unset):
            host_keys = UNSET
        elif isinstance(self.host_keys, list):
            host_keys = []
            for host_keys_type_0_item_data in self.host_keys:
                host_keys_type_0_item = host_keys_type_0_item_data.to_dict()
                host_keys.append(host_keys_type_0_item)

        else:
            host_keys = self.host_keys

        ssh_commands: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ssh_commands, Unset):
            ssh_commands = self.ssh_commands

        authentications: Union[Unset, list[str]] = UNSET
        if not isinstance(self.authentications, Unset):
            authentications = []
            for authentications_item_data in self.authentications:
                authentications_item = authentications_item_data.value
                authentications.append(authentications_item)

        public_key_algorithms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.public_key_algorithms, Unset):
            public_key_algorithms = self.public_key_algorithms

        macs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        kex_algorithms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.kex_algorithms, Unset):
            kex_algorithms = self.kex_algorithms

        ciphers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ciphers, Unset):
            ciphers = self.ciphers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if bindings is not UNSET:
            field_dict["bindings"] = bindings
        if host_keys is not UNSET:
            field_dict["host_keys"] = host_keys
        if ssh_commands is not UNSET:
            field_dict["ssh_commands"] = ssh_commands
        if authentications is not UNSET:
            field_dict["authentications"] = authentications
        if public_key_algorithms is not UNSET:
            field_dict["public_key_algorithms"] = public_key_algorithms
        if macs is not UNSET:
            field_dict["macs"] = macs
        if kex_algorithms is not UNSET:
            field_dict["kex_algorithms"] = kex_algorithms
        if ciphers is not UNSET:
            field_dict["ciphers"] = ciphers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ssh_binding import SSHBinding
        from ..models.ssh_host_key import SSHHostKey

        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        def _parse_bindings(data: object) -> Union[None, Unset, list["SSHBinding"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bindings_type_0 = []
                _bindings_type_0 = data
                for bindings_type_0_item_data in _bindings_type_0:
                    bindings_type_0_item = SSHBinding.from_dict(bindings_type_0_item_data)

                    bindings_type_0.append(bindings_type_0_item)

                return bindings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SSHBinding"]], data)

        bindings = _parse_bindings(d.pop("bindings", UNSET))

        def _parse_host_keys(data: object) -> Union[None, Unset, list["SSHHostKey"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                host_keys_type_0 = []
                _host_keys_type_0 = data
                for host_keys_type_0_item_data in _host_keys_type_0:
                    host_keys_type_0_item = SSHHostKey.from_dict(host_keys_type_0_item_data)

                    host_keys_type_0.append(host_keys_type_0_item)

                return host_keys_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SSHHostKey"]], data)

        host_keys = _parse_host_keys(d.pop("host_keys", UNSET))

        ssh_commands = cast(list[str], d.pop("ssh_commands", UNSET))

        authentications = []
        _authentications = d.pop("authentications", UNSET)
        for authentications_item_data in _authentications or []:
            authentications_item = SSHAuthentications(authentications_item_data)

            authentications.append(authentications_item)

        public_key_algorithms = cast(list[str], d.pop("public_key_algorithms", UNSET))

        macs = cast(list[str], d.pop("macs", UNSET))

        kex_algorithms = cast(list[str], d.pop("kex_algorithms", UNSET))

        ciphers = cast(list[str], d.pop("ciphers", UNSET))

        ssh_service_status = cls(
            is_active=is_active,
            bindings=bindings,
            host_keys=host_keys,
            ssh_commands=ssh_commands,
            authentications=authentications,
            public_key_algorithms=public_key_algorithms,
            macs=macs,
            kex_algorithms=kex_algorithms,
            ciphers=ciphers,
        )

        ssh_service_status.additional_properties = d
        return ssh_service_status

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
