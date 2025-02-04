from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ip_list_entries_order import GetIpListEntriesOrder
from ...models.ip_list_entry import IPListEntry
from ...models.ip_list_type import IPListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: IPListType,
    *,
    filter_: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetIpListEntriesOrder] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["from"] = from_

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/iplists/{type_}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["IPListEntry"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IPListEntry.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["IPListEntry"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: IPListType,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetIpListEntriesOrder] = UNSET,
) -> Response[Union[Any, list["IPListEntry"]]]:
    """Get IP list entries

     Returns an array with one or more IP list entry

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        filter_ (Union[Unset, str]):
        from_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetIpListEntriesOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['IPListEntry']]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        filter_=filter_,
        from_=from_,
        limit=limit,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: IPListType,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetIpListEntriesOrder] = UNSET,
) -> Optional[Union[Any, list["IPListEntry"]]]:
    """Get IP list entries

     Returns an array with one or more IP list entry

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        filter_ (Union[Unset, str]):
        from_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetIpListEntriesOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['IPListEntry']]
    """

    return sync_detailed(
        type_=type_,
        client=client,
        filter_=filter_,
        from_=from_,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    type_: IPListType,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetIpListEntriesOrder] = UNSET,
) -> Response[Union[Any, list["IPListEntry"]]]:
    """Get IP list entries

     Returns an array with one or more IP list entry

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        filter_ (Union[Unset, str]):
        from_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetIpListEntriesOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['IPListEntry']]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        filter_=filter_,
        from_=from_,
        limit=limit,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: IPListType,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetIpListEntriesOrder] = UNSET,
) -> Optional[Union[Any, list["IPListEntry"]]]:
    """Get IP list entries

     Returns an array with one or more IP list entry

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        filter_ (Union[Unset, str]):
        from_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        order (Union[Unset, GetIpListEntriesOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['IPListEntry']]
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            filter_=filter_,
            from_=from_,
            limit=limit,
            order=order,
        )
    ).parsed
