from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_protocols import EventProtocols
from ...models.get_log_events_order import GetLogEventsOrder
from ...models.log_event import LogEvent
from ...models.log_event_type import LogEventType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    events: Union[Unset, list[LogEventType]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetLogEventsOrder] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start_timestamp"] = start_timestamp

    params["end_timestamp"] = end_timestamp

    json_events: Union[Unset, list[int]] = UNSET
    if not isinstance(events, Unset):
        json_events = []
        for events_item_data in events:
            events_item = events_item_data.value
            json_events.append(events_item)

    params["events"] = json_events

    params["username"] = username

    params["ip"] = ip

    json_protocols: Union[Unset, list[str]] = UNSET
    if not isinstance(protocols, Unset):
        json_protocols = []
        for protocols_item_data in protocols:
            protocols_item = protocols_item_data.value
            json_protocols.append(protocols_item)

    params["protocols"] = json_protocols

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
        "url": "/events/log",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["LogEvent"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LogEvent.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["LogEvent"]]]:
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
    events: Union[Unset, list[LogEventType]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetLogEventsOrder] = UNSET,
) -> Response[Union[Any, list["LogEvent"]]]:
    r"""Get log events

     Returns an array with one or more log events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        events (Union[Unset, list[LogEventType]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetLogEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['LogEvent']]]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        events=events,
        username=username,
        ip=ip,
        protocols=protocols,
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
    events: Union[Unset, list[LogEventType]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetLogEventsOrder] = UNSET,
) -> Optional[Union[Any, list["LogEvent"]]]:
    r"""Get log events

     Returns an array with one or more log events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        events (Union[Unset, list[LogEventType]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetLogEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['LogEvent']]
    """

    return sync_detailed(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        events=events,
        username=username,
        ip=ip,
        protocols=protocols,
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
    events: Union[Unset, list[LogEventType]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetLogEventsOrder] = UNSET,
) -> Response[Union[Any, list["LogEvent"]]]:
    r"""Get log events

     Returns an array with one or more log events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        events (Union[Unset, list[LogEventType]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetLogEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['LogEvent']]]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        events=events,
        username=username,
        ip=ip,
        protocols=protocols,
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
    events: Union[Unset, list[LogEventType]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    protocols: Union[Unset, list[EventProtocols]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetLogEventsOrder] = UNSET,
) -> Optional[Union[Any, list["LogEvent"]]]:
    r"""Get log events

     Returns an array with one or more log events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        events (Union[Unset, list[LogEventType]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        protocols (Union[Unset, list[EventProtocols]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetLogEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['LogEvent']]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            events=events,
            username=username,
            ip=ip,
            protocols=protocols,
            instance_ids=instance_ids,
            from_id=from_id,
            role=role,
            csv_export=csv_export,
            limit=limit,
            order=order,
        )
    ).parsed
