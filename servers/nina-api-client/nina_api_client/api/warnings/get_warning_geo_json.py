from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.geo_json_object import GeoJSONObject
from ...types import Response


def _get_kwargs(
    identifier: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/warnings/{identifier}.geojson",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GeoJSONObject]:
    if response.status_code == 200:
        response_200 = GeoJSONObject.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GeoJSONObject]:
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
) -> Response[GeoJSONObject]:
    """GeoJSON informationen zu einer Warnung.

     Datenformat entspricht [https://datatracker.ietf.org/doc/html/rfc7946#section-
    3](https://datatracker.ietf.org/doc/html/rfc7946#section-3)

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeoJSONObject]
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
) -> Optional[GeoJSONObject]:
    """GeoJSON informationen zu einer Warnung.

     Datenformat entspricht [https://datatracker.ietf.org/doc/html/rfc7946#section-
    3](https://datatracker.ietf.org/doc/html/rfc7946#section-3)

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeoJSONObject
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GeoJSONObject]:
    """GeoJSON informationen zu einer Warnung.

     Datenformat entspricht [https://datatracker.ietf.org/doc/html/rfc7946#section-
    3](https://datatracker.ietf.org/doc/html/rfc7946#section-3)

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeoJSONObject]
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
) -> Optional[GeoJSONObject]:
    """GeoJSON informationen zu einer Warnung.

     Datenformat entspricht [https://datatracker.ietf.org/doc/html/rfc7946#section-
    3](https://datatracker.ietf.org/doc/html/rfc7946#section-3)

    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeoJSONObject
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
        )
    ).parsed
