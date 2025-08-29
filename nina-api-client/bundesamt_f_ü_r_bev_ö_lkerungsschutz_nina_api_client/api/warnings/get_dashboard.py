from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ars_overview_result_item import ARSOverviewResultItem
from ...types import Response


def _get_kwargs(
    ars: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dashboard/{ars}.json",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ARSOverviewResultItem"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_ars_overview_result_item_data in _response_200:
            componentsschemas_ars_overview_result_item = ARSOverviewResultItem.from_dict(
                componentsschemas_ars_overview_result_item_data
            )

            response_200.append(componentsschemas_ars_overview_result_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ARSOverviewResultItem"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ars: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["ARSOverviewResultItem"]]:
    """Meldungsübersicht nach ARS

     Erhalten Sie die aktuellen Warnmeldungen für eine bestimmte Region.

    Args:
        ars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ARSOverviewResultItem']]
    """

    kwargs = _get_kwargs(
        ars=ars,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ars: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["ARSOverviewResultItem"]]:
    """Meldungsübersicht nach ARS

     Erhalten Sie die aktuellen Warnmeldungen für eine bestimmte Region.

    Args:
        ars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ARSOverviewResultItem']
    """

    return sync_detailed(
        ars=ars,
        client=client,
    ).parsed


async def asyncio_detailed(
    ars: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["ARSOverviewResultItem"]]:
    """Meldungsübersicht nach ARS

     Erhalten Sie die aktuellen Warnmeldungen für eine bestimmte Region.

    Args:
        ars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ARSOverviewResultItem']]
    """

    kwargs = _get_kwargs(
        ars=ars,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ars: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["ARSOverviewResultItem"]]:
    """Meldungsübersicht nach ARS

     Erhalten Sie die aktuellen Warnmeldungen für eine bestimmte Region.

    Args:
        ars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ARSOverviewResultItem']
    """

    return (
        await asyncio_detailed(
            ars=ars,
            client=client,
        )
    ).parsed
