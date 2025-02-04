from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.transfer_quota_usage import TransferQuotaUsage
from ...models.user_transfer_quota_update_usage_mode import UserTransferQuotaUpdateUsageMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    body: TransferQuotaUsage,
    mode: Union[Unset, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_mode: Union[Unset, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/quotas/users/{username}/transfer-usage",
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
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
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
    body: TransferQuotaUsage,
    mode: Union[Unset, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        body (TransferQuotaUsage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TransferQuotaUsage,
    mode: Union[Unset, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        body (TransferQuotaUsage):

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
        mode=mode,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TransferQuotaUsage,
    mode: Union[Unset, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        body (TransferQuotaUsage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TransferQuotaUsage,
    mode: Union[Unset, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        body (TransferQuotaUsage):

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
            mode=mode,
        )
    ).parsed
