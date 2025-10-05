from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_v1_scrape_format import GetV1ScrapeFormat
from ...models.get_v1_scrape_proxy_mode import GetV1ScrapeProxyMode
from ...models.scrape_response import ScrapeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    url_query: str,
    format_: Union[Unset, GetV1ScrapeFormat] = UNSET,
    depth: Union[Unset, int] = UNSET,
    max_links: Union[Unset, int] = UNSET,
    render_js: Union[Unset, bool] = UNSET,
    include_html: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
    proxy_mode: Union[Unset, GetV1ScrapeProxyMode] = GetV1ScrapeProxyMode.OFF,
    proxy_region: Union[Unset, str] = UNSET,
    proxy_session: Union[Unset, str] = UNSET,
    rotate_user_agent: Union[Unset, bool] = True,
    enable_bot_protection: Union[Unset, bool] = True,
    max_consecutive_errors: Union[Unset, int] = 5,
    user_agent: Union[Unset, str] = UNSET,
    wait_for_selectors: Union[Unset, list[str]] = UNSET,
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

    params["include_html"] = include_html

    params["fresh"] = fresh

    json_proxy_mode: Union[Unset, str] = UNSET
    if not isinstance(proxy_mode, Unset):
        json_proxy_mode = proxy_mode.value

    params["proxy_mode"] = json_proxy_mode

    params["proxy_region"] = proxy_region

    params["proxy_session"] = proxy_session

    params["rotate_user_agent"] = rotate_user_agent

    params["enable_bot_protection"] = enable_bot_protection

    params["max_consecutive_errors"] = max_consecutive_errors

    params["user_agent"] = user_agent

    json_wait_for_selectors: Union[Unset, list[str]] = UNSET
    if not isinstance(wait_for_selectors, Unset):
        json_wait_for_selectors = wait_for_selectors

    params["wait_for_selectors"] = json_wait_for_selectors

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
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 408:
        response_408 = Error.from_dict(response.json())

        return response_408
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
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
    include_html: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
    proxy_mode: Union[Unset, GetV1ScrapeProxyMode] = GetV1ScrapeProxyMode.OFF,
    proxy_region: Union[Unset, str] = UNSET,
    proxy_session: Union[Unset, str] = UNSET,
    rotate_user_agent: Union[Unset, bool] = True,
    enable_bot_protection: Union[Unset, bool] = True,
    max_consecutive_errors: Union[Unset, int] = 5,
    user_agent: Union[Unset, str] = UNSET,
    wait_for_selectors: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        include_html (Union[Unset, bool]):
        fresh (Union[Unset, bool]):
        proxy_mode (Union[Unset, GetV1ScrapeProxyMode]):  Default: GetV1ScrapeProxyMode.OFF.
        proxy_region (Union[Unset, str]): ISO country code (e.g., "us", "eu", "gb")
        proxy_session (Union[Unset, str]): Sticky session key for proxy consistency
        rotate_user_agent (Union[Unset, bool]):  Default: True.
        enable_bot_protection (Union[Unset, bool]):  Default: True.
        max_consecutive_errors (Union[Unset, int]):  Default: 5.
        user_agent (Union[Unset, str]): Specific user agent to use (selected by backend)
        wait_for_selectors (Union[Unset, list[str]]): CSS selectors to wait for before considering
            page loaded (for dynamic content)

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
        include_html=include_html,
        fresh=fresh,
        proxy_mode=proxy_mode,
        proxy_region=proxy_region,
        proxy_session=proxy_session,
        rotate_user_agent=rotate_user_agent,
        enable_bot_protection=enable_bot_protection,
        max_consecutive_errors=max_consecutive_errors,
        user_agent=user_agent,
        wait_for_selectors=wait_for_selectors,
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
    include_html: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
    proxy_mode: Union[Unset, GetV1ScrapeProxyMode] = GetV1ScrapeProxyMode.OFF,
    proxy_region: Union[Unset, str] = UNSET,
    proxy_session: Union[Unset, str] = UNSET,
    rotate_user_agent: Union[Unset, bool] = True,
    enable_bot_protection: Union[Unset, bool] = True,
    max_consecutive_errors: Union[Unset, int] = 5,
    user_agent: Union[Unset, str] = UNSET,
    wait_for_selectors: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        include_html (Union[Unset, bool]):
        fresh (Union[Unset, bool]):
        proxy_mode (Union[Unset, GetV1ScrapeProxyMode]):  Default: GetV1ScrapeProxyMode.OFF.
        proxy_region (Union[Unset, str]): ISO country code (e.g., "us", "eu", "gb")
        proxy_session (Union[Unset, str]): Sticky session key for proxy consistency
        rotate_user_agent (Union[Unset, bool]):  Default: True.
        enable_bot_protection (Union[Unset, bool]):  Default: True.
        max_consecutive_errors (Union[Unset, int]):  Default: 5.
        user_agent (Union[Unset, str]): Specific user agent to use (selected by backend)
        wait_for_selectors (Union[Unset, list[str]]): CSS selectors to wait for before considering
            page loaded (for dynamic content)

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
        include_html=include_html,
        fresh=fresh,
        proxy_mode=proxy_mode,
        proxy_region=proxy_region,
        proxy_session=proxy_session,
        rotate_user_agent=rotate_user_agent,
        enable_bot_protection=enable_bot_protection,
        max_consecutive_errors=max_consecutive_errors,
        user_agent=user_agent,
        wait_for_selectors=wait_for_selectors,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    url_query: str,
    format_: Union[Unset, GetV1ScrapeFormat] = UNSET,
    depth: Union[Unset, int] = UNSET,
    max_links: Union[Unset, int] = UNSET,
    render_js: Union[Unset, bool] = UNSET,
    include_html: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
    proxy_mode: Union[Unset, GetV1ScrapeProxyMode] = GetV1ScrapeProxyMode.OFF,
    proxy_region: Union[Unset, str] = UNSET,
    proxy_session: Union[Unset, str] = UNSET,
    rotate_user_agent: Union[Unset, bool] = True,
    enable_bot_protection: Union[Unset, bool] = True,
    max_consecutive_errors: Union[Unset, int] = 5,
    user_agent: Union[Unset, str] = UNSET,
    wait_for_selectors: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        include_html (Union[Unset, bool]):
        fresh (Union[Unset, bool]):
        proxy_mode (Union[Unset, GetV1ScrapeProxyMode]):  Default: GetV1ScrapeProxyMode.OFF.
        proxy_region (Union[Unset, str]): ISO country code (e.g., "us", "eu", "gb")
        proxy_session (Union[Unset, str]): Sticky session key for proxy consistency
        rotate_user_agent (Union[Unset, bool]):  Default: True.
        enable_bot_protection (Union[Unset, bool]):  Default: True.
        max_consecutive_errors (Union[Unset, int]):  Default: 5.
        user_agent (Union[Unset, str]): Specific user agent to use (selected by backend)
        wait_for_selectors (Union[Unset, list[str]]): CSS selectors to wait for before considering
            page loaded (for dynamic content)

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
        include_html=include_html,
        fresh=fresh,
        proxy_mode=proxy_mode,
        proxy_region=proxy_region,
        proxy_session=proxy_session,
        rotate_user_agent=rotate_user_agent,
        enable_bot_protection=enable_bot_protection,
        max_consecutive_errors=max_consecutive_errors,
        user_agent=user_agent,
        wait_for_selectors=wait_for_selectors,
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
    include_html: Union[Unset, bool] = UNSET,
    fresh: Union[Unset, bool] = UNSET,
    proxy_mode: Union[Unset, GetV1ScrapeProxyMode] = GetV1ScrapeProxyMode.OFF,
    proxy_region: Union[Unset, str] = UNSET,
    proxy_session: Union[Unset, str] = UNSET,
    rotate_user_agent: Union[Unset, bool] = True,
    enable_bot_protection: Union[Unset, bool] = True,
    max_consecutive_errors: Union[Unset, int] = 5,
    user_agent: Union[Unset, str] = UNSET,
    wait_for_selectors: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Error, ScrapeResponse]]:
    """Scrape a single URL

    Args:
        url_query (str):
        format_ (Union[Unset, GetV1ScrapeFormat]):
        depth (Union[Unset, int]):
        max_links (Union[Unset, int]):
        render_js (Union[Unset, bool]):
        include_html (Union[Unset, bool]):
        fresh (Union[Unset, bool]):
        proxy_mode (Union[Unset, GetV1ScrapeProxyMode]):  Default: GetV1ScrapeProxyMode.OFF.
        proxy_region (Union[Unset, str]): ISO country code (e.g., "us", "eu", "gb")
        proxy_session (Union[Unset, str]): Sticky session key for proxy consistency
        rotate_user_agent (Union[Unset, bool]):  Default: True.
        enable_bot_protection (Union[Unset, bool]):  Default: True.
        max_consecutive_errors (Union[Unset, int]):  Default: 5.
        user_agent (Union[Unset, str]): Specific user agent to use (selected by backend)
        wait_for_selectors (Union[Unset, list[str]]): CSS selectors to wait for before considering
            page loaded (for dynamic content)

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
            include_html=include_html,
            fresh=fresh,
            proxy_mode=proxy_mode,
            proxy_region=proxy_region,
            proxy_session=proxy_session,
            rotate_user_agent=rotate_user_agent,
            enable_bot_protection=enable_bot_protection,
            max_consecutive_errors=max_consecutive_errors,
            user_agent=user_agent,
            wait_for_selectors=wait_for_selectors,
        )
    ).parsed
