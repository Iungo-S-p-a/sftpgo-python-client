from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.setprops_user_file_body import SetpropsUserFileBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: SetpropsUserFileBody,
    path: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/user/files/metadata",
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
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetpropsUserFileBody,
    path: str,
) -> Response[Union[Any, ApiResponse]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        body (SetpropsUserFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetpropsUserFileBody,
    path: str,
) -> Optional[Union[Any, ApiResponse]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        body (SetpropsUserFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        path=path,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetpropsUserFileBody,
    path: str,
) -> Response[Union[Any, ApiResponse]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        body (SetpropsUserFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetpropsUserFileBody,
    path: str,
) -> Optional[Union[Any, ApiResponse]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        body (SetpropsUserFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            path=path,
        )
    ).parsed
