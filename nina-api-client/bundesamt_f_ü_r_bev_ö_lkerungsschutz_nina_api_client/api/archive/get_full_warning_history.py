from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_warning_history import ArchiveWarningHistory
from ...types import Response


def _get_kwargs(
    identifier: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/archive.mowas/{identifier}-mapping.json",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ArchiveWarningHistory]:
    if response.status_code == 200:
        response_200 = ArchiveWarningHistory.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ArchiveWarningHistory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArchiveWarningHistory]:
    """Gesammelter Verlauf einer MOWAS Warnung

     Gesammelter Verlauf einer MOWAS Warnung

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveWarningHistory]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArchiveWarningHistory]:
    """Gesammelter Verlauf einer MOWAS Warnung

     Gesammelter Verlauf einer MOWAS Warnung

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveWarningHistory
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ArchiveWarningHistory]:
    """Gesammelter Verlauf einer MOWAS Warnung

     Gesammelter Verlauf einer MOWAS Warnung

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveWarningHistory]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ArchiveWarningHistory]:
    """Gesammelter Verlauf einer MOWAS Warnung

     Gesammelter Verlauf einer MOWAS Warnung

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveWarningHistory
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
        )
    ).parsed
