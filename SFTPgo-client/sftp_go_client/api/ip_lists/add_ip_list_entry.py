from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.ip_list_entry import IPListEntry
from ...models.ip_list_type import IPListType
from ...types import Response


def _get_kwargs(
    type_: IPListType,
    *,
    body: IPListEntry,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/iplists/{type_}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == 201:
        response_201 = ApiResponse.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, ApiResponse]]:
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
    body: IPListEntry,
) -> Response[Union[Any, ApiResponse]]:
    """Add a new IP list entry

     Add an IP address or a CIDR network to a supported list

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        body (IPListEntry):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: IPListType,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IPListEntry,
) -> Optional[Union[Any, ApiResponse]]:
    """Add a new IP list entry

     Add an IP address or a CIDR network to a supported list

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        body (IPListEntry):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return sync_detailed(
        type_=type_,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    type_: IPListType,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IPListEntry,
) -> Response[Union[Any, ApiResponse]]:
    """Add a new IP list entry

     Add an IP address or a CIDR network to a supported list

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        body (IPListEntry):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: IPListType,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IPListEntry,
) -> Optional[Union[Any, ApiResponse]]:
    """Add a new IP list entry

     Add an IP address or a CIDR network to a supported list

    Args:
        type_ (IPListType): IP List types:
              * `1` - allow list
              * `2` - defender
              * `3` - rate limiter safe list
        body (IPListEntry):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            body=body,
        )
    ).parsed
