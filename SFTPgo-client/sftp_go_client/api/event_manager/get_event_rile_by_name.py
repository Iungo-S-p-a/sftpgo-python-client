from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_rule import EventRule
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    confidential_data: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["confidential_data"] = confidential_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/eventrules/{name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventRule]]:
    if response.status_code == 200:
        response_200 = EventRule.from_dict(response.json())

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
) -> Response[Union[Any, EventRule]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    confidential_data: Union[Unset, int] = UNSET,
) -> Response[Union[Any, EventRule]]:
    """Find event rules by name

     Returns the event rule with the given name if it exists.

    Args:
        name (str):
        confidential_data (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRule]]
    """

    kwargs = _get_kwargs(
        name=name,
        confidential_data=confidential_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    confidential_data: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, EventRule]]:
    """Find event rules by name

     Returns the event rule with the given name if it exists.

    Args:
        name (str):
        confidential_data (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventRule]
    """

    return sync_detailed(
        name=name,
        client=client,
        confidential_data=confidential_data,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    confidential_data: Union[Unset, int] = UNSET,
) -> Response[Union[Any, EventRule]]:
    """Find event rules by name

     Returns the event rule with the given name if it exists.

    Args:
        name (str):
        confidential_data (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRule]]
    """

    kwargs = _get_kwargs(
        name=name,
        confidential_data=confidential_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    confidential_data: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, EventRule]]:
    """Find event rules by name

     Returns the event rule with the given name if it exists.

    Args:
        name (str):
        confidential_data (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventRule]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            confidential_data=confidential_data,
        )
    ).parsed
