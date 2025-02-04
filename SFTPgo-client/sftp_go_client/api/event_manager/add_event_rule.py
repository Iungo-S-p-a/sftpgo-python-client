from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_rule import EventRule
from ...models.event_rule_minimal import EventRuleMinimal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EventRuleMinimal,
    confidential_data: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["confidential_data"] = confidential_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/eventrules",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventRule]]:
    if response.status_code == 201:
        response_201 = EventRule.from_dict(response.json())

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
) -> Response[Union[Any, EventRule]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRuleMinimal,
    confidential_data: Union[Unset, int] = UNSET,
) -> Response[Union[Any, EventRule]]:
    """Add event rule

     Adds a new event rule

    Args:
        confidential_data (Union[Unset, int]):
        body (EventRuleMinimal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRule]]
    """

    kwargs = _get_kwargs(
        body=body,
        confidential_data=confidential_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRuleMinimal,
    confidential_data: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, EventRule]]:
    """Add event rule

     Adds a new event rule

    Args:
        confidential_data (Union[Unset, int]):
        body (EventRuleMinimal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventRule]
    """

    return sync_detailed(
        client=client,
        body=body,
        confidential_data=confidential_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRuleMinimal,
    confidential_data: Union[Unset, int] = UNSET,
) -> Response[Union[Any, EventRule]]:
    """Add event rule

     Adds a new event rule

    Args:
        confidential_data (Union[Unset, int]):
        body (EventRuleMinimal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRule]]
    """

    kwargs = _get_kwargs(
        body=body,
        confidential_data=confidential_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRuleMinimal,
    confidential_data: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, EventRule]]:
    """Add event rule

     Adds a new event rule

    Args:
        confidential_data (Union[Unset, int]):
        body (EventRuleMinimal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventRule]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            confidential_data=confidential_data,
        )
    ).parsed
