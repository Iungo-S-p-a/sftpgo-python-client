from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="EventActionCommandConfig")


@_attrs_define
class EventActionCommandConfig:
    """
    Attributes:
        cmd (Union[Unset, str]): absolute path to the command to execute
        args (Union[Unset, list[str]]): command line arguments
        timeout (Union[Unset, int]):
        env_vars (Union[Unset, list['KeyValue']]):
    """

    cmd: Union[Unset, str] = UNSET
    args: Union[Unset, list[str]] = UNSET
    timeout: Union[Unset, int] = UNSET
    env_vars: Union[Unset, list["KeyValue"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cmd = self.cmd

        args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        timeout = self.timeout

        env_vars: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = []
            for env_vars_item_data in self.env_vars:
                env_vars_item = env_vars_item_data.to_dict()
                env_vars.append(env_vars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if args is not UNSET:
            field_dict["args"] = args
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.key_value import KeyValue

        d = src_dict.copy()
        cmd = d.pop("cmd", UNSET)

        args = cast(list[str], d.pop("args", UNSET))

        timeout = d.pop("timeout", UNSET)

        env_vars = []
        _env_vars = d.pop("env_vars", UNSET)
        for env_vars_item_data in _env_vars or []:
            env_vars_item = KeyValue.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        event_action_command_config = cls(
            cmd=cmd,
            args=args,
            timeout=timeout,
            env_vars=env_vars,
        )

        event_action_command_config.additional_properties = d
        return event_action_command_config

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
