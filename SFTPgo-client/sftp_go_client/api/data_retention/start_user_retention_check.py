from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.folder_retention import FolderRetention
from ...models.retention_check_notification import RetentionCheckNotification
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    body: list["FolderRetention"],
    notifications: Union[Unset, list[RetentionCheckNotification]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_notifications: Union[Unset, list[str]] = UNSET
    if not isinstance(notifications, Unset):
        json_notifications = []
        for notifications_item_data in notifications:
            notifications_item = notifications_item_data.value
            json_notifications.append(notifications_item)

    params["notifications"] = json_notifications

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/retention/users/{username}/check",
        "params": params,
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == 202:
        response_202 = ApiResponse.from_dict(response.json())

        return response_202
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
    body: list["FolderRetention"],
    notifications: Union[Unset, list[RetentionCheckNotification]] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, list[RetentionCheckNotification]]):
        body (list['FolderRetention']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        notifications=notifications,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["FolderRetention"],
    notifications: Union[Unset, list[RetentionCheckNotification]] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, list[RetentionCheckNotification]]):
        body (list['FolderRetention']):

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
        notifications=notifications,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["FolderRetention"],
    notifications: Union[Unset, list[RetentionCheckNotification]] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, list[RetentionCheckNotification]]):
        body (list['FolderRetention']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        notifications=notifications,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["FolderRetention"],
    notifications: Union[Unset, list[RetentionCheckNotification]] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, list[RetentionCheckNotification]]):
        body (list['FolderRetention']):

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
            notifications=notifications,
        )
    ).parsed
