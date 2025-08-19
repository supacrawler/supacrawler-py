from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_v1_scrape_format import GetV1ScrapeFormat
from ...models.scrape_response import ScrapeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    url_query: str,
    format_: Union[Unset, GetV1ScrapeFormat] = UNSET,
    depth: Union[Unset, int] = UNSET,
    max_links: Union[Unset, int] = UNSET,
    render_js: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["url"] = url_query

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["depth"] = depth

    params["max_links"] = max_links

    params["render_js"] = render_js

    params["fresh"] = fresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/scrape",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ScrapeResponse]]:
    if response.status_code == 200:
        response_200 = ScrapeResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, ScrapeResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    url_query: str,
    format_: Union[Unset, GetV1ScrapeFormat] = UNSET,
    depth: Union[Unset, int] = UNSET,
    max_links: Union[Unset, int] = UNSET,
    render_js: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        fresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ScrapeResponse]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        format_=format_,
        depth=depth,
        max_links=max_links,
        render_js=render_js,
        fresh=fresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    url_query: str,
    format_: Union[Unset, GetV1ScrapeFormat] = UNSET,
    depth: Union[Unset, int] = UNSET,
    max_links: Union[Unset, int] = UNSET,
    render_js: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        fresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ScrapeResponse]
    """

    return sync_detailed(
        client=client,
        url_query=url_query,
        format_=format_,
        depth=depth,
        max_links=max_links,
        render_js=render_js,
        fresh=fresh,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    url_query: str,
    format_: Union[Unset, GetV1ScrapeFormat] = UNSET,
    depth: Union[Unset, int] = UNSET,
    max_links: Union[Unset, int] = UNSET,
    render_js: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        fresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ScrapeResponse]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        format_=format_,
        depth=depth,
        max_links=max_links,
        render_js=render_js,
        fresh=fresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    url_query: str,
    format_: Union[Unset, GetV1ScrapeFormat] = UNSET,
    depth: Union[Unset, int] = UNSET,
    max_links: Union[Unset, int] = UNSET,
    render_js: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        fresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ScrapeResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            url_query=url_query,
            format_=format_,
            depth=depth,
            max_links=max_links,
            render_js=render_js,
            fresh=fresh,
        )
    ).parsed
