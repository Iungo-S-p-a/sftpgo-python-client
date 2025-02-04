from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.loaddata_from_file_mode import LoaddataFromFileMode
from ...models.loaddata_from_file_scan_quota import LoaddataFromFileScanQuota
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    input_file: str,
    scan_quota: Union[Unset, LoaddataFromFileScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromFileMode] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["input-file"] = input_file

    json_scan_quota: Union[Unset, int] = UNSET
    if not isinstance(scan_quota, Unset):
        json_scan_quota = scan_quota.value

    params["scan-quota"] = json_scan_quota

    json_mode: Union[Unset, int] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/loaddata",
        "params": params,
    }

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
    input_file: str,
    scan_quota: Union[Unset, LoaddataFromFileScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromFileMode] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Load data from path

     Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and
    the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

    Args:
        input_file (str):
        scan_quota (Union[Unset, LoaddataFromFileScanQuota]):
        mode (Union[Unset, LoaddataFromFileMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        input_file=input_file,
        scan_quota=scan_quota,
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    input_file: str,
    scan_quota: Union[Unset, LoaddataFromFileScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromFileMode] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Load data from path

     Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and
    the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

    Args:
        input_file (str):
        scan_quota (Union[Unset, LoaddataFromFileScanQuota]):
        mode (Union[Unset, LoaddataFromFileMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return sync_detailed(
        client=client,
        input_file=input_file,
        scan_quota=scan_quota,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    input_file: str,
    scan_quota: Union[Unset, LoaddataFromFileScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromFileMode] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Load data from path

     Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and
    the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

    Args:
        input_file (str):
        scan_quota (Union[Unset, LoaddataFromFileScanQuota]):
        mode (Union[Unset, LoaddataFromFileMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        input_file=input_file,
        scan_quota=scan_quota,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    input_file: str,
    scan_quota: Union[Unset, LoaddataFromFileScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromFileMode] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Load data from path

     Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and
    the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

    Args:
        input_file (str):
        scan_quota (Union[Unset, LoaddataFromFileScanQuota]):
        mode (Union[Unset, LoaddataFromFileMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            input_file=input_file,
            scan_quota=scan_quota,
            mode=mode,
        )
    ).parsed
