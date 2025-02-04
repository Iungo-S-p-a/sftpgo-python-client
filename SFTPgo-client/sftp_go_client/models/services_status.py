from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_provider_status import DataProviderStatus
    from ..models.ftp_service_status import FTPServiceStatus
    from ..models.mfa_status import MFAStatus
    from ..models.services_status_allow_list import ServicesStatusAllowList
    from ..models.services_status_defender import ServicesStatusDefender
    from ..models.services_status_rate_limiters import ServicesStatusRateLimiters
    from ..models.ssh_service_status import SSHServiceStatus
    from ..models.web_dav_service_status import WebDAVServiceStatus


T = TypeVar("T", bound="ServicesStatus")


@_attrs_define
class ServicesStatus:
    """
    Attributes:
        ssh (Union[Unset, SSHServiceStatus]):
        ftp (Union[Unset, FTPServiceStatus]):
        webdav (Union[Unset, WebDAVServiceStatus]):
        data_provider (Union[Unset, DataProviderStatus]):
        defender (Union[Unset, ServicesStatusDefender]):
        mfa (Union[Unset, MFAStatus]):
        allow_list (Union[Unset, ServicesStatusAllowList]):
        rate_limiters (Union[Unset, ServicesStatusRateLimiters]):
    """

    ssh: Union[Unset, "SSHServiceStatus"] = UNSET
    ftp: Union[Unset, "FTPServiceStatus"] = UNSET
    webdav: Union[Unset, "WebDAVServiceStatus"] = UNSET
    data_provider: Union[Unset, "DataProviderStatus"] = UNSET
    defender: Union[Unset, "ServicesStatusDefender"] = UNSET
    mfa: Union[Unset, "MFAStatus"] = UNSET
    allow_list: Union[Unset, "ServicesStatusAllowList"] = UNSET
    rate_limiters: Union[Unset, "ServicesStatusRateLimiters"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssh: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        ftp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ftp, Unset):
            ftp = self.ftp.to_dict()

        webdav: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.webdav, Unset):
            webdav = self.webdav.to_dict()

        data_provider: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_provider, Unset):
            data_provider = self.data_provider.to_dict()

        defender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defender, Unset):
            defender = self.defender.to_dict()

        mfa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mfa, Unset):
            mfa = self.mfa.to_dict()

        allow_list: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.allow_list, Unset):
            allow_list = self.allow_list.to_dict()

        rate_limiters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rate_limiters, Unset):
            rate_limiters = self.rate_limiters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if ftp is not UNSET:
            field_dict["ftp"] = ftp
        if webdav is not UNSET:
            field_dict["webdav"] = webdav
        if data_provider is not UNSET:
            field_dict["data_provider"] = data_provider
        if defender is not UNSET:
            field_dict["defender"] = defender
        if mfa is not UNSET:
            field_dict["mfa"] = mfa
        if allow_list is not UNSET:
            field_dict["allow_list"] = allow_list
        if rate_limiters is not UNSET:
            field_dict["rate_limiters"] = rate_limiters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_provider_status import DataProviderStatus
        from ..models.ftp_service_status import FTPServiceStatus
        from ..models.mfa_status import MFAStatus
        from ..models.services_status_allow_list import ServicesStatusAllowList
        from ..models.services_status_defender import ServicesStatusDefender
        from ..models.services_status_rate_limiters import ServicesStatusRateLimiters
        from ..models.ssh_service_status import SSHServiceStatus
        from ..models.web_dav_service_status import WebDAVServiceStatus

        d = src_dict.copy()
        _ssh = d.pop("ssh", UNSET)
        ssh: Union[Unset, SSHServiceStatus]
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = SSHServiceStatus.from_dict(_ssh)

        _ftp = d.pop("ftp", UNSET)
        ftp: Union[Unset, FTPServiceStatus]
        if isinstance(_ftp, Unset):
            ftp = UNSET
        else:
            ftp = FTPServiceStatus.from_dict(_ftp)

        _webdav = d.pop("webdav", UNSET)
        webdav: Union[Unset, WebDAVServiceStatus]
        if isinstance(_webdav, Unset):
            webdav = UNSET
        else:
            webdav = WebDAVServiceStatus.from_dict(_webdav)

        _data_provider = d.pop("data_provider", UNSET)
        data_provider: Union[Unset, DataProviderStatus]
        if isinstance(_data_provider, Unset):
            data_provider = UNSET
        else:
            data_provider = DataProviderStatus.from_dict(_data_provider)

        _defender = d.pop("defender", UNSET)
        defender: Union[Unset, ServicesStatusDefender]
        if isinstance(_defender, Unset):
            defender = UNSET
        else:
            defender = ServicesStatusDefender.from_dict(_defender)

        _mfa = d.pop("mfa", UNSET)
        mfa: Union[Unset, MFAStatus]
        if isinstance(_mfa, Unset):
            mfa = UNSET
        else:
            mfa = MFAStatus.from_dict(_mfa)

        _allow_list = d.pop("allow_list", UNSET)
        allow_list: Union[Unset, ServicesStatusAllowList]
        if isinstance(_allow_list, Unset):
            allow_list = UNSET
        else:
            allow_list = ServicesStatusAllowList.from_dict(_allow_list)

        _rate_limiters = d.pop("rate_limiters", UNSET)
        rate_limiters: Union[Unset, ServicesStatusRateLimiters]
        if isinstance(_rate_limiters, Unset):
            rate_limiters = UNSET
        else:
            rate_limiters = ServicesStatusRateLimiters.from_dict(_rate_limiters)

        services_status = cls(
            ssh=ssh,
            ftp=ftp,
            webdav=webdav,
            data_provider=data_provider,
            defender=defender,
            mfa=mfa,
            allow_list=allow_list,
            rate_limiters=rate_limiters,
        )

        services_status.additional_properties = d
        return services_status

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
