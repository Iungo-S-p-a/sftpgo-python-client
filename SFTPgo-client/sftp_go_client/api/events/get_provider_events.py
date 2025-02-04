from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_provider_events_order import GetProviderEventsOrder
from ...models.provider_event import ProviderEvent
from ...models.provider_event_action import ProviderEventAction
from ...models.provider_event_object_type import ProviderEventObjectType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    actions: Union[Unset, list[ProviderEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    object_types: Union[Unset, list[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    omit_object_data: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetProviderEventsOrder] = UNSET,
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

    params["object_name"] = object_name

    json_object_types: Union[Unset, list[str]] = UNSET
    if not isinstance(object_types, Unset):
        json_object_types = []
        for object_types_item_data in object_types:
            object_types_item = object_types_item_data.value
            json_object_types.append(object_types_item)

    params["object_types"] = json_object_types

    json_instance_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(instance_ids, Unset):
        json_instance_ids = instance_ids

    params["instance_ids"] = json_instance_ids

    params["from_id"] = from_id

    params["role"] = role

    params["csv_export"] = csv_export

    params["omit_object_data"] = omit_object_data

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/provider",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ProviderEvent"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProviderEvent.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["ProviderEvent"]]]:
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
    actions: Union[Unset, list[ProviderEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    object_types: Union[Unset, list[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    omit_object_data: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetProviderEventsOrder] = UNSET,
) -> Response[Union[Any, list["ProviderEvent"]]]:
    r"""Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[ProviderEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        object_name (Union[Unset, str]):
        object_types (Union[Unset, list[ProviderEventObjectType]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        omit_object_data (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ProviderEvent']]]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        object_name=object_name,
        object_types=object_types,
        instance_ids=instance_ids,
        from_id=from_id,
        role=role,
        csv_export=csv_export,
        omit_object_data=omit_object_data,
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
    actions: Union[Unset, list[ProviderEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    object_types: Union[Unset, list[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    omit_object_data: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetProviderEventsOrder] = UNSET,
) -> Optional[Union[Any, list["ProviderEvent"]]]:
    r"""Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[ProviderEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        object_name (Union[Unset, str]):
        object_types (Union[Unset, list[ProviderEventObjectType]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        omit_object_data (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ProviderEvent']]
    """

    return sync_detailed(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        object_name=object_name,
        object_types=object_types,
        instance_ids=instance_ids,
        from_id=from_id,
        role=role,
        csv_export=csv_export,
        omit_object_data=omit_object_data,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_timestamp: Union[Unset, int] = 0,
    end_timestamp: Union[Unset, int] = 0,
    actions: Union[Unset, list[ProviderEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    object_types: Union[Unset, list[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    omit_object_data: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetProviderEventsOrder] = UNSET,
) -> Response[Union[Any, list["ProviderEvent"]]]:
    r"""Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[ProviderEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        object_name (Union[Unset, str]):
        object_types (Union[Unset, list[ProviderEventObjectType]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        omit_object_data (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ProviderEvent']]]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        object_name=object_name,
        object_types=object_types,
        instance_ids=instance_ids,
        from_id=from_id,
        role=role,
        csv_export=csv_export,
        omit_object_data=omit_object_data,
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
    actions: Union[Unset, list[ProviderEventAction]] = UNSET,
    username: Union[Unset, str] = UNSET,
    ip: Union[Unset, str] = UNSET,
    object_name: Union[Unset, str] = UNSET,
    object_types: Union[Unset, list[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, list[str]] = UNSET,
    from_id: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    csv_export: Union[Unset, bool] = False,
    omit_object_data: Union[Unset, bool] = False,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetProviderEventsOrder] = UNSET,
) -> Optional[Union[Any, list["ProviderEvent"]]]:
    r"""Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, int]):  Default: 0.
        end_timestamp (Union[Unset, int]):  Default: 0.
        actions (Union[Unset, list[ProviderEventAction]]):
        username (Union[Unset, str]):
        ip (Union[Unset, str]):
        object_name (Union[Unset, str]):
        object_types (Union[Unset, list[ProviderEventObjectType]]):
        instance_ids (Union[Unset, list[str]]):
        from_id (Union[Unset, str]):
        role (Union[Unset, str]):
        csv_export (Union[Unset, bool]):  Default: False.
        omit_object_data (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ProviderEvent']]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            actions=actions,
            username=username,
            ip=ip,
            object_name=object_name,
            object_types=object_types,
            instance_ids=instance_ids,
            from_id=from_id,
            role=role,
            csv_export=csv_export,
            omit_object_data=omit_object_data,
            limit=limit,
            order=order,
        )
    ).parsed
