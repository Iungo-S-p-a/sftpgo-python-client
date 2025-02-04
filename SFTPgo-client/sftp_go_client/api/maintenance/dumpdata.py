from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.backup_data import BackupData
from ...models.dump_data_scopes import DumpDataScopes
from ...models.dumpdata_indent import DumpdataIndent
from ...models.dumpdata_output_data import DumpdataOutputData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    output_file: Union[Unset, str] = UNSET,
    output_data: Union[Unset, DumpdataOutputData] = UNSET,
    indent: Union[Unset, DumpdataIndent] = UNSET,
    scopes: Union[Unset, list[DumpDataScopes]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["output-file"] = output_file

    json_output_data: Union[Unset, int] = UNSET
    if not isinstance(output_data, Unset):
        json_output_data = output_data.value

    params["output-data"] = json_output_data

    json_indent: Union[Unset, int] = UNSET
    if not isinstance(indent, Unset):
        json_indent = indent.value

    params["indent"] = json_indent

    json_scopes: Union[Unset, list[str]] = UNSET
    if not isinstance(scopes, Unset):
        json_scopes = []
        for scopes_item_data in scopes:
            scopes_item = scopes_item_data.value
            json_scopes.append(scopes_item)

    params["scopes"] = json_scopes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dumpdata",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["ApiResponse", "BackupData"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["ApiResponse", "BackupData"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ApiResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = BackupData.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[Any, Union["ApiResponse", "BackupData"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    output_file: Union[Unset, str] = UNSET,
    output_data: Union[Unset, DumpdataOutputData] = UNSET,
    indent: Union[Unset, DumpdataIndent] = UNSET,
    scopes: Union[Unset, list[DumpDataScopes]] = UNSET,
) -> Response[Union[Any, Union["ApiResponse", "BackupData"]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, str]):
        output_data (Union[Unset, DumpdataOutputData]):
        indent (Union[Unset, DumpdataIndent]):
        scopes (Union[Unset, list[DumpDataScopes]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['ApiResponse', 'BackupData']]]
    """

    kwargs = _get_kwargs(
        output_file=output_file,
        output_data=output_data,
        indent=indent,
        scopes=scopes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    output_file: Union[Unset, str] = UNSET,
    output_data: Union[Unset, DumpdataOutputData] = UNSET,
    indent: Union[Unset, DumpdataIndent] = UNSET,
    scopes: Union[Unset, list[DumpDataScopes]] = UNSET,
) -> Optional[Union[Any, Union["ApiResponse", "BackupData"]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, str]):
        output_data (Union[Unset, DumpdataOutputData]):
        indent (Union[Unset, DumpdataIndent]):
        scopes (Union[Unset, list[DumpDataScopes]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['ApiResponse', 'BackupData']]
    """

    return sync_detailed(
        client=client,
        output_file=output_file,
        output_data=output_data,
        indent=indent,
        scopes=scopes,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    output_file: Union[Unset, str] = UNSET,
    output_data: Union[Unset, DumpdataOutputData] = UNSET,
    indent: Union[Unset, DumpdataIndent] = UNSET,
    scopes: Union[Unset, list[DumpDataScopes]] = UNSET,
) -> Response[Union[Any, Union["ApiResponse", "BackupData"]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, str]):
        output_data (Union[Unset, DumpdataOutputData]):
        indent (Union[Unset, DumpdataIndent]):
        scopes (Union[Unset, list[DumpDataScopes]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['ApiResponse', 'BackupData']]]
    """

    kwargs = _get_kwargs(
        output_file=output_file,
        output_data=output_data,
        indent=indent,
        scopes=scopes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    output_file: Union[Unset, str] = UNSET,
    output_data: Union[Unset, DumpdataOutputData] = UNSET,
    indent: Union[Unset, DumpdataIndent] = UNSET,
    scopes: Union[Unset, list[DumpDataScopes]] = UNSET,
) -> Optional[Union[Any, Union["ApiResponse", "BackupData"]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, str]):
        output_data (Union[Unset, DumpdataOutputData]):
        indent (Union[Unset, DumpdataIndent]):
        scopes (Union[Unset, list[DumpDataScopes]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['ApiResponse', 'BackupData']]
    """

    return (
        await asyncio_detailed(
            client=client,
            output_file=output_file,
            output_data=output_data,
            indent=indent,
            scopes=scopes,
        )
    ).parsed
