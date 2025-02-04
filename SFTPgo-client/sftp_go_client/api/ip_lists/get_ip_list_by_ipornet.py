from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ip_list_entry import IPListEntry
from ...models.ip_list_type import IPListType
from ...types import Response


def _get_kwargs(
    type_: IPListType,
    ipornet: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/iplists/{type_}/{ipornet}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, IPListEntry]]:
    if response.status_code == 200:
        response_200 = IPListEntry.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, IPListEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: IPListType,
    ipornet: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, IPListEntry]]:
    """Find entry by ipornet

     Returns the entry with the given ipornet if it exists.

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        ipornet (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IPListEntry]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        ipornet=ipornet,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: IPListType,
    ipornet: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, IPListEntry]]:
    """Find entry by ipornet

     Returns the entry with the given ipornet if it exists.

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        ipornet (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, IPListEntry]
    """

    return sync_detailed(
        type_=type_,
        ipornet=ipornet,
        client=client,
    ).parsed


async def asyncio_detailed(
    type_: IPListType,
    ipornet: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, IPListEntry]]:
    """Find entry by ipornet

     Returns the entry with the given ipornet if it exists.

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        ipornet (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IPListEntry]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        ipornet=ipornet,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: IPListType,
    ipornet: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, IPListEntry]]:
    """Find entry by ipornet

     Returns the entry with the given ipornet if it exists.

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        ipornet (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, IPListEntry]
    """

    return (
        await asyncio_detailed(
            type_=type_,
            ipornet=ipornet,
            client=client,
        )
    ).parsed
