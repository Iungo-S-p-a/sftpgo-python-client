from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.update_user_disconnect import UpdateUserDisconnect
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_disconnect: Union[Unset, int] = UNSET
    if not isinstance(disconnect, Unset):
        json_disconnect = disconnect.value

    params["disconnect"] = json_disconnect

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/users/{username}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == 200:
        response_200 = ApiResponse.from_dict(response.json())

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
) -> Response[Union[Any, ApiResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings. The
    current password will be preserved if the password field is omitted in the request body. Recovery
    codes and TOTP configuration cannot be set/updated using this API: each user must use the specific
    APIs

    Args:
        username (str):
        disconnect (Union[Unset, UpdateUserDisconnect]):
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        disconnect=disconnect,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings. The
    current password will be preserved if the password field is omitted in the request body. Recovery
    codes and TOTP configuration cannot be set/updated using this API: each user must use the specific
    APIs

    Args:
        username (str):
        disconnect (Union[Unset, UpdateUserDisconnect]):
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
        disconnect=disconnect,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings. The
    current password will be preserved if the password field is omitted in the request body. Recovery
    codes and TOTP configuration cannot be set/updated using this API: each user must use the specific
    APIs

    Args:
        username (str):
        disconnect (Union[Unset, UpdateUserDisconnect]):
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        disconnect=disconnect,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings. The
    current password will be preserved if the password field is omitted in the request body. Recovery
    codes and TOTP configuration cannot be set/updated using this API: each user must use the specific
    APIs

    Args:
        username (str):
        disconnect (Union[Unset, UpdateUserDisconnect]):
        body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
            disconnect=disconnect,
        )
    ).parsed
