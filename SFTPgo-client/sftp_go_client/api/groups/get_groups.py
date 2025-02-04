from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_order import GetGroupsOrder
from ...models.group import Group
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetGroupsOrder] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["Group"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Group.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["Group"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetGroupsOrder] = UNSET,
) -> Response[Union[Any, list["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['Group']]]
    """

    kwargs = _get_kwargs(
        offset=offset,
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
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetGroupsOrder] = UNSET,
) -> Optional[Union[Any, list["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['Group']]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetGroupsOrder] = UNSET,
) -> Response[Union[Any, list["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['Group']]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetGroupsOrder] = UNSET,
) -> Optional[Union[Any, list["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['Group']]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            order=order,
        )
    ).parsed
