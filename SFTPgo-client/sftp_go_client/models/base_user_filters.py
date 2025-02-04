from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_user_filters_ftp_security import BaseUserFiltersFtpSecurity
from ..models.login_methods import LoginMethods
from ..models.mfa_protocols import MFAProtocols
from ..models.supported_protocols import SupportedProtocols
from ..models.user_type import UserType
from ..models.web_client_options import WebClientOptions
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bandwidth_limit import BandwidthLimit
    from ..models.hooks_filter import HooksFilter
    from ..models.patterns_filter import PatternsFilter
    from ..models.time_period import TimePeriod


T = TypeVar("T", bound="BaseUserFilters")


@_attrs_define
class BaseUserFilters:
    """Additional user options

    Attributes:
        allowed_ip (Union[Unset, list[str]]): only clients connecting from these IP/Mask are allowed. IP/Mask must be in
            CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32" Example:
            ['192.0.2.0/24', '2001:db8::/32'].
        denied_ip (Union[Unset, list[str]]): clients connecting from these IP/Mask are not allowed. Denied rules are
            evaluated before allowed ones Example: ['172.16.0.0/16'].
        denied_login_methods (Union[Unset, list[LoginMethods]]): if null or empty any available login method is allowed
        denied_protocols (Union[Unset, list[SupportedProtocols]]): if null or empty any available protocol is allowed
        file_patterns (Union[Unset, list['PatternsFilter']]): filters based on shell like file patterns. These
            restrictions do not apply to files listing for performance reasons, so a denied file cannot be
            downloaded/overwritten/renamed but it will still be in the list of files. Please note that these restrictions
            can be easily bypassed
        max_upload_file_size (Union[Unset, int]): maximum allowed size, as bytes, for a single file upload. The upload
            will be aborted if/when the size of the file being sent exceeds this limit. 0 means unlimited. This restriction
            does not apply for SSH system commands such as `git` and `rsync`
        tls_username (Union[Unset, str]): defines the TLS certificate field to use as username. For FTP clients it must
            match the name provided using the "USER" command. For WebDAV, if no username is provided, the CN will be used as
            username. For WebDAV clients it must match the implicit or provided username. Ignored if mutual TLS is disabled.
            Currently the only supported value is `CommonName`
        tls_certs (Union[Unset, list[str]]):
        hooks (Union[Unset, HooksFilter]): User specific hook overrides
        disable_fs_checks (Union[Unset, bool]): Disable checks for existence and automatic creation of home directory
            and virtual folders. SFTPGo requires that the user's home directory, virtual folder root, and intermediate paths
            to virtual folders exist to work properly. If you already know that the required directories exist, disabling
            these checks will speed up login. You could, for example, disable these checks after the first login
        web_client (Union[Unset, list[WebClientOptions]]): WebClient/user REST API related configuration options
        allow_api_key_auth (Union[Unset, bool]): API key authentication allows to impersonate this user with an API key
        user_type (Union[Unset, UserType]): This is an hint for authentication plugins. It is ignored when using SFTPGo
            internal authentication
        bandwidth_limits (Union[Unset, list['BandwidthLimit']]):
        external_auth_cache_time (Union[Unset, int]): Defines the cache time, in seconds, for users authenticated using
            an external auth hook. 0 means no cache
        start_directory (Union[Unset, str]): Specifies an alternate starting directory. If not set, the default is "/".
            This option is supported for SFTP/SCP, FTP and HTTP (WebClient/REST API) protocols. Relative paths will use this
            directory as base.
        two_factor_protocols (Union[Unset, list[MFAProtocols]]): Defines protocols that require two factor
            authentication
        ftp_security (Union[Unset, BaseUserFiltersFtpSecurity]): Set to `1` to require TLS for both data and control
            connection. his setting is useful if you want to allow both encrypted and plain text FTP sessions globally and
            then you want to require encrypted sessions on a per-user basis. It has no effect if TLS is already required for
            all users in the configuration file.
        is_anonymous (Union[Unset, bool]): If enabled the user can login with any password or no password at all.
            Anonymous users are supported for FTP and WebDAV protocols and permissions will be automatically set to "list"
            and "download" (read only)
        default_shares_expiration (Union[Unset, int]): Defines the default expiration for newly created shares as number
            of days. 0 means no expiration
        max_shares_expiration (Union[Unset, int]): Defines the maximum allowed expiration, as a number of days, when a
            user creates or updates a share. 0 means no expiration
        password_expiration (Union[Unset, int]): The password expires after the defined number of days. 0 means no
            expiration
        password_strength (Union[Unset, int]): Defines the minimum password strength. 0 means disabled, any password
            will be accepted. Values in the 50-70 range are suggested for common use cases
        access_time (Union[Unset, list['TimePeriod']]):
    """

    allowed_ip: Union[Unset, list[str]] = UNSET
    denied_ip: Union[Unset, list[str]] = UNSET
    denied_login_methods: Union[Unset, list[LoginMethods]] = UNSET
    denied_protocols: Union[Unset, list[SupportedProtocols]] = UNSET
    file_patterns: Union[Unset, list["PatternsFilter"]] = UNSET
    max_upload_file_size: Union[Unset, int] = UNSET
    tls_username: Union[Unset, str] = UNSET
    tls_certs: Union[Unset, list[str]] = UNSET
    hooks: Union[Unset, "HooksFilter"] = UNSET
    disable_fs_checks: Union[Unset, bool] = UNSET
    web_client: Union[Unset, list[WebClientOptions]] = UNSET
    allow_api_key_auth: Union[Unset, bool] = UNSET
    user_type: Union[Unset, UserType] = UNSET
    bandwidth_limits: Union[Unset, list["BandwidthLimit"]] = UNSET
    external_auth_cache_time: Union[Unset, int] = UNSET
    start_directory: Union[Unset, str] = UNSET
    two_factor_protocols: Union[Unset, list[MFAProtocols]] = UNSET
    ftp_security: Union[Unset, BaseUserFiltersFtpSecurity] = UNSET
    is_anonymous: Union[Unset, bool] = UNSET
    default_shares_expiration: Union[Unset, int] = UNSET
    max_shares_expiration: Union[Unset, int] = UNSET
    password_expiration: Union[Unset, int] = UNSET
    password_strength: Union[Unset, int] = UNSET
    access_time: Union[Unset, list["TimePeriod"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_ip: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_ip, Unset):
            allowed_ip = self.allowed_ip

        denied_ip: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied_ip, Unset):
            denied_ip = self.denied_ip

        denied_login_methods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied_login_methods, Unset):
            denied_login_methods = []
            for denied_login_methods_item_data in self.denied_login_methods:
                denied_login_methods_item = denied_login_methods_item_data.value
                denied_login_methods.append(denied_login_methods_item)

        denied_protocols: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied_protocols, Unset):
            denied_protocols = []
            for denied_protocols_item_data in self.denied_protocols:
                denied_protocols_item = denied_protocols_item_data.value
                denied_protocols.append(denied_protocols_item)

        file_patterns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.file_patterns, Unset):
            file_patterns = []
            for file_patterns_item_data in self.file_patterns:
                file_patterns_item = file_patterns_item_data.to_dict()
                file_patterns.append(file_patterns_item)

        max_upload_file_size = self.max_upload_file_size

        tls_username = self.tls_username

        tls_certs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tls_certs, Unset):
            tls_certs = self.tls_certs

        hooks: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        disable_fs_checks = self.disable_fs_checks

        web_client: Union[Unset, list[str]] = UNSET
        if not isinstance(self.web_client, Unset):
            web_client = []
            for web_client_item_data in self.web_client:
                web_client_item = web_client_item_data.value
                web_client.append(web_client_item)

        allow_api_key_auth = self.allow_api_key_auth

        user_type: Union[Unset, str] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

        bandwidth_limits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bandwidth_limits, Unset):
            bandwidth_limits = []
            for bandwidth_limits_item_data in self.bandwidth_limits:
                bandwidth_limits_item = bandwidth_limits_item_data.to_dict()
                bandwidth_limits.append(bandwidth_limits_item)

        external_auth_cache_time = self.external_auth_cache_time

        start_directory = self.start_directory

        two_factor_protocols: Union[Unset, list[str]] = UNSET
        if not isinstance(self.two_factor_protocols, Unset):
            two_factor_protocols = []
            for two_factor_protocols_item_data in self.two_factor_protocols:
                two_factor_protocols_item = two_factor_protocols_item_data.value
                two_factor_protocols.append(two_factor_protocols_item)

        ftp_security: Union[Unset, int] = UNSET
        if not isinstance(self.ftp_security, Unset):
            ftp_security = self.ftp_security.value

        is_anonymous = self.is_anonymous

        default_shares_expiration = self.default_shares_expiration

        max_shares_expiration = self.max_shares_expiration

        password_expiration = self.password_expiration

        password_strength = self.password_strength

        access_time: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.access_time, Unset):
            access_time = []
            for access_time_item_data in self.access_time:
                access_time_item = access_time_item_data.to_dict()
                access_time.append(access_time_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_ip is not UNSET:
            field_dict["allowed_ip"] = allowed_ip
        if denied_ip is not UNSET:
            field_dict["denied_ip"] = denied_ip
        if denied_login_methods is not UNSET:
            field_dict["denied_login_methods"] = denied_login_methods
        if denied_protocols is not UNSET:
            field_dict["denied_protocols"] = denied_protocols
        if file_patterns is not UNSET:
            field_dict["file_patterns"] = file_patterns
        if max_upload_file_size is not UNSET:
            field_dict["max_upload_file_size"] = max_upload_file_size
        if tls_username is not UNSET:
            field_dict["tls_username"] = tls_username
        if tls_certs is not UNSET:
            field_dict["tls_certs"] = tls_certs
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if disable_fs_checks is not UNSET:
            field_dict["disable_fs_checks"] = disable_fs_checks
        if web_client is not UNSET:
            field_dict["web_client"] = web_client
        if allow_api_key_auth is not UNSET:
            field_dict["allow_api_key_auth"] = allow_api_key_auth
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if bandwidth_limits is not UNSET:
            field_dict["bandwidth_limits"] = bandwidth_limits
        if external_auth_cache_time is not UNSET:
            field_dict["external_auth_cache_time"] = external_auth_cache_time
        if start_directory is not UNSET:
            field_dict["start_directory"] = start_directory
        if two_factor_protocols is not UNSET:
            field_dict["two_factor_protocols"] = two_factor_protocols
        if ftp_security is not UNSET:
            field_dict["ftp_security"] = ftp_security
        if is_anonymous is not UNSET:
            field_dict["is_anonymous"] = is_anonymous
        if default_shares_expiration is not UNSET:
            field_dict["default_shares_expiration"] = default_shares_expiration
        if max_shares_expiration is not UNSET:
            field_dict["max_shares_expiration"] = max_shares_expiration
        if password_expiration is not UNSET:
            field_dict["password_expiration"] = password_expiration
        if password_strength is not UNSET:
            field_dict["password_strength"] = password_strength
        if access_time is not UNSET:
            field_dict["access_time"] = access_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.bandwidth_limit import BandwidthLimit
        from ..models.hooks_filter import HooksFilter
        from ..models.patterns_filter import PatternsFilter
        from ..models.time_period import TimePeriod

        d = src_dict.copy()
        allowed_ip = cast(list[str], d.pop("allowed_ip", UNSET))

        denied_ip = cast(list[str], d.pop("denied_ip", UNSET))

        denied_login_methods = []
        _denied_login_methods = d.pop("denied_login_methods", UNSET)
        for denied_login_methods_item_data in _denied_login_methods or []:
            denied_login_methods_item = LoginMethods(denied_login_methods_item_data)

            denied_login_methods.append(denied_login_methods_item)

        denied_protocols = []
        _denied_protocols = d.pop("denied_protocols", UNSET)
        for denied_protocols_item_data in _denied_protocols or []:
            denied_protocols_item = SupportedProtocols(denied_protocols_item_data)

            denied_protocols.append(denied_protocols_item)

        file_patterns = []
        _file_patterns = d.pop("file_patterns", UNSET)
        for file_patterns_item_data in _file_patterns or []:
            file_patterns_item = PatternsFilter.from_dict(file_patterns_item_data)

            file_patterns.append(file_patterns_item)

        max_upload_file_size = d.pop("max_upload_file_size", UNSET)

        tls_username = d.pop("tls_username", UNSET)

        tls_certs = cast(list[str], d.pop("tls_certs", UNSET))

        _hooks = d.pop("hooks", UNSET)
        hooks: Union[Unset, HooksFilter]
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = HooksFilter.from_dict(_hooks)

        disable_fs_checks = d.pop("disable_fs_checks", UNSET)

        web_client = []
        _web_client = d.pop("web_client", UNSET)
        for web_client_item_data in _web_client or []:
            web_client_item = WebClientOptions(web_client_item_data)

            web_client.append(web_client_item)

        allow_api_key_auth = d.pop("allow_api_key_auth", UNSET)

        _user_type = d.pop("user_type", UNSET)
        user_type: Union[Unset, UserType]
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = UserType(_user_type)

        bandwidth_limits = []
        _bandwidth_limits = d.pop("bandwidth_limits", UNSET)
        for bandwidth_limits_item_data in _bandwidth_limits or []:
            bandwidth_limits_item = BandwidthLimit.from_dict(bandwidth_limits_item_data)

            bandwidth_limits.append(bandwidth_limits_item)

        external_auth_cache_time = d.pop("external_auth_cache_time", UNSET)

        start_directory = d.pop("start_directory", UNSET)

        two_factor_protocols = []
        _two_factor_protocols = d.pop("two_factor_protocols", UNSET)
        for two_factor_protocols_item_data in _two_factor_protocols or []:
            two_factor_protocols_item = MFAProtocols(two_factor_protocols_item_data)

            two_factor_protocols.append(two_factor_protocols_item)

        _ftp_security = d.pop("ftp_security", UNSET)
        ftp_security: Union[Unset, BaseUserFiltersFtpSecurity]
        if isinstance(_ftp_security, Unset):
            ftp_security = UNSET
        else:
            ftp_security = BaseUserFiltersFtpSecurity(_ftp_security)

        is_anonymous = d.pop("is_anonymous", UNSET)

        default_shares_expiration = d.pop("default_shares_expiration", UNSET)

        max_shares_expiration = d.pop("max_shares_expiration", UNSET)

        password_expiration = d.pop("password_expiration", UNSET)

        password_strength = d.pop("password_strength", UNSET)

        access_time = []
        _access_time = d.pop("access_time", UNSET)
        for access_time_item_data in _access_time or []:
            access_time_item = TimePeriod.from_dict(access_time_item_data)

            access_time.append(access_time_item)

        base_user_filters = cls(
            allowed_ip=allowed_ip,
            denied_ip=denied_ip,
            denied_login_methods=denied_login_methods,
            denied_protocols=denied_protocols,
            file_patterns=file_patterns,
            max_upload_file_size=max_upload_file_size,
            tls_username=tls_username,
            tls_certs=tls_certs,
            hooks=hooks,
            disable_fs_checks=disable_fs_checks,
            web_client=web_client,
            allow_api_key_auth=allow_api_key_auth,
            user_type=user_type,
            bandwidth_limits=bandwidth_limits,
            external_auth_cache_time=external_auth_cache_time,
            start_directory=start_directory,
            two_factor_protocols=two_factor_protocols,
            ftp_security=ftp_security,
            is_anonymous=is_anonymous,
            default_shares_expiration=default_shares_expiration,
            max_shares_expiration=max_shares_expiration,
            password_expiration=password_expiration,
            password_strength=password_strength,
            access_time=access_time,
        )

        base_user_filters.additional_properties = d
        return base_user_filters

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
