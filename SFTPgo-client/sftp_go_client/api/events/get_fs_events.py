from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_protocols import EventProtocols
from ...models.fs_event import FsEvent
from ...models.fs_event_action import FsEventAction
from ...models.fs_event_status import FsEventStatus
from ...models.fs_providers import FsProviders
from ...models.get_fs_events_order import GetFsEventsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    actions: Union[Unset, list[FsEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    ssh_cmd: Union[Unset, str] = UNSET,
    fs_provider: Union[Unset, FsProviders] = UNSET,
    bucket: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    statuses: Union[Unset, list[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetFsEventsOrder] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_timestamp"] = start_timestamp

    params["end_timestamp"] = end_timestamp

    json_actions: Union[Unset, list[str]] = UNSET
    if not isinstance(actions, Unset):
        json_actions = []
        for actions_item_data in actions:
            actions_item = actions_item_data.value
            json_actions.append(actions_item)

    params["actions"] = json_actions

    params["username"] = username

    params["ip"] = ip

    params["ssh_cmd"] = ssh_cmd

    json_fs_provider: Union[Unset, int] = UNSET
    if not isinstance(fs_provider, Unset):
        json_fs_provider = fs_provider.value

    params["fs_provider"] = json_fs_provider

    params["bucket"] = bucket

    params["endpoint"] = endpoint

    json_protocols: Union[Unset, list[str]] = UNSET
    if not isinstance(protocols, Unset):
        json_protocols = []
        for protocols_item_data in protocols:
            protocols_item = protocols_item_data.value
            json_protocols.append(protocols_item)

    params["protocols"] = json_protocols

    json_statuses: Union[Unset, list[int]] = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = []
        for statuses_item_data in statuses:
            statuses_item = statuses_item_data.value
            json_statuses.append(statuses_item)

    params["statuses"] = json_statuses

    json_instance_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(instance_ids, Unset):
        json_instance_ids = instance_ids

    params["instance_ids"] = json_instance_ids

    params["from_id"] = from_id

    params["role"] = role

    params["csv_export"] = csv_export

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/fs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["FsEvent"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FsEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["FsEvent"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    actions: Union[Unset, list[FsEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    ssh_cmd: Union[Unset, str] = UNSET,
    fs_provider: Union[Unset, FsProviders] = UNSET,
    bucket: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    statuses: Union[Unset, list[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetFsEventsOrder] = UNSET,
) -> Response[Union[Any, list["FsEvent"]]]:
    r"""Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[FsEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        ssh_cmd (Union[Unset, str]):
        fs_provider (Union[Unset, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        statuses (Union[Unset, list[FsEventStatus]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetFsEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['FsEvent']]]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        ssh_cmd=ssh_cmd,
        fs_provider=fs_provider,
        bucket=bucket,
        endpoint=endpoint,
        protocols=protocols,
        statuses=statuses,
        instance_ids=instance_ids,
        from_id=from_id,
        role=role,
        csv_export=csv_export,
        limit=limit,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    actions: Union[Unset, list[FsEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    ssh_cmd: Union[Unset, str] = UNSET,
    fs_provider: Union[Unset, FsProviders] = UNSET,
    bucket: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    statuses: Union[Unset, list[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetFsEventsOrder] = UNSET,
) -> Optional[Union[Any, list["FsEvent"]]]:
    r"""Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[FsEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        ssh_cmd (Union[Unset, str]):
        fs_provider (Union[Unset, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        statuses (Union[Unset, list[FsEventStatus]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetFsEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['FsEvent']]
    """

    return sync_detailed(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        ssh_cmd=ssh_cmd,
        fs_provider=fs_provider,
        bucket=bucket,
        endpoint=endpoint,
        protocols=protocols,
        statuses=statuses,
        instance_ids=instance_ids,
        from_id=from_id,
        role=role,
        csv_export=csv_export,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    actions: Union[Unset, list[FsEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    ssh_cmd: Union[Unset, str] = UNSET,
    fs_provider: Union[Unset, FsProviders] = UNSET,
    bucket: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    statuses: Union[Unset, list[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetFsEventsOrder] = UNSET,
) -> Response[Union[Any, list["FsEvent"]]]:
    r"""Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[FsEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        ssh_cmd (Union[Unset, str]):
        fs_provider (Union[Unset, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        statuses (Union[Unset, list[FsEventStatus]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetFsEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['FsEvent']]]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        ssh_cmd=ssh_cmd,
        fs_provider=fs_provider,
        bucket=bucket,
        endpoint=endpoint,
        protocols=protocols,
        statuses=statuses,
        instance_ids=instance_ids,
        from_id=from_id,
        role=role,
        csv_export=csv_export,
        limit=limit,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    actions: Union[Unset, list[FsEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    ssh_cmd: Union[Unset, str] = UNSET,
    fs_provider: Union[Unset, FsProviders] = UNSET,
    bucket: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    statuses: Union[Unset, list[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetFsEventsOrder] = UNSET,
) -> Optional[Union[Any, list["FsEvent"]]]:
    r"""Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[FsEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        ssh_cmd (Union[Unset, str]):
        fs_provider (Union[Unset, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        statuses (Union[Unset, list[FsEventStatus]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetFsEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['FsEvent']]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            actions=actions,
            username=username,
            ip=ip,
            ssh_cmd=ssh_cmd,
            fs_provider=fs_provider,
            bucket=bucket,
            endpoint=endpoint,
            protocols=protocols,
            statuses=statuses,
            instance_ids=instance_ids,
            from_id=from_id,
            role=role,
            csv_export=csv_export,
            limit=limit,
            order=order,
        )
    ).parsed
