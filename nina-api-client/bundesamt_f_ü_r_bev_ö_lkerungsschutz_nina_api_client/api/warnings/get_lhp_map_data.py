from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.map_warnings_item import MapWarningsItem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lhp/mapData.json",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["MapWarningsItem"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_map_warnings_item_data in _response_200:
            componentsschemas_map_warnings_item = MapWarningsItem.from_dict(componentsschemas_map_warnings_item_data)

            response_200.append(componentsschemas_map_warnings_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["MapWarningsItem"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["MapWarningsItem"]]:
    """Meldungen des LÃ¤nderübergreifenden Hochwasserportals

     Liefert die Meldungen des LÃ¤nderübergreifenden Hochwasserportals für die Kartenansicht.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['MapWarningsItem']]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["MapWarningsItem"]]:
    """Meldungen des LÃ¤nderübergreifenden Hochwasserportals

     Liefert die Meldungen des LÃ¤nderübergreifenden Hochwasserportals für die Kartenansicht.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['MapWarningsItem']
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["MapWarningsItem"]]:
    """Meldungen des LÃ¤nderübergreifenden Hochwasserportals

     Liefert die Meldungen des LÃ¤nderübergreifenden Hochwasserportals für die Kartenansicht.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['MapWarningsItem']]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["MapWarningsItem"]]:
    """Meldungen des LÃ¤nderübergreifenden Hochwasserportals

     Liefert die Meldungen des LÃ¤nderübergreifenden Hochwasserportals für die Kartenansicht.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['MapWarningsItem']
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
