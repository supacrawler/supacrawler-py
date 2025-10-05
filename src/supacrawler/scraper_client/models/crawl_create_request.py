from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crawl_create_request_format import CrawlCreateRequestFormat
from ..models.crawl_create_request_proxy_mode import CrawlCreateRequestProxyMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crawl_create_request_webhook_headers import CrawlCreateRequestWebhookHeaders


T = TypeVar("T", bound="CrawlCreateRequest")


@_attrs_define
class CrawlCreateRequest:
    """
    Attributes:
        url (str):
        format_ (Union[Unset, CrawlCreateRequestFormat]):
        depth (Union[Unset, int]):
        link_limit (Union[Unset, int]):
        include_subdomains (Union[Unset, bool]):
        render_js (Union[Unset, bool]):
        include_html (Union[Unset, bool]):
        fresh (Union[Unset, bool]): Bypass cache and fetch fresh content
        patterns (Union[Unset, list[str]]): URL patterns to match (e.g., ["/blog/*", "/docs/*"])
        proxy_mode (Union[Unset, CrawlCreateRequestProxyMode]): Proxy rotation mode Default:
            CrawlCreateRequestProxyMode.OFF.
        proxy_region (Union[Unset, str]): ISO country code (e.g., "us", "eu", "gb")
        proxy_session (Union[Unset, str]): Sticky session key for proxy consistency
        rotate_user_agent (Union[Unset, bool]): Enable user agent rotation Default: True.
        enable_bot_protection (Union[Unset, bool]): Enable anti-bot detection and pivoting Default: True.
        max_consecutive_errors (Union[Unset, int]): Max consecutive errors before pivoting strategy Default: 5.
        user_agent (Union[Unset, str]): Specific user agent to use (selected by backend)
        wait_for_selectors (Union[Unset, list[str]]): CSS selectors to wait for before considering page loaded (for
            dynamic content)
        webhook_url (Union[Unset, str]): Optional webhook URL to notify when job completes
        webhook_headers (Union[Unset, CrawlCreateRequestWebhookHeaders]): Optional HTTP headers to include in webhook
            requests
    """

    url: str
    format_: Union[Unset, CrawlCreateRequestFormat] = UNSET
    depth: Union[Unset, int] = UNSET
    link_limit: Union[Unset, int] = UNSET
    include_subdomains: Union[Unset, bool] = UNSET
    render_js: Union[Unset, bool] = UNSET
    include_html: Union[Unset, bool] = UNSET
    fresh: Union[Unset, bool] = UNSET
    patterns: Union[Unset, list[str]] = UNSET
    proxy_mode: Union[Unset, CrawlCreateRequestProxyMode] = CrawlCreateRequestProxyMode.OFF
    proxy_region: Union[Unset, str] = UNSET
    proxy_session: Union[Unset, str] = UNSET
    rotate_user_agent: Union[Unset, bool] = True
    enable_bot_protection: Union[Unset, bool] = True
    max_consecutive_errors: Union[Unset, int] = 5
    user_agent: Union[Unset, str] = UNSET
    wait_for_selectors: Union[Unset, list[str]] = UNSET
    webhook_url: Union[Unset, str] = UNSET
    webhook_headers: Union[Unset, "CrawlCreateRequestWebhookHeaders"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        depth = self.depth

        link_limit = self.link_limit

        include_subdomains = self.include_subdomains

        render_js = self.render_js

        include_html = self.include_html

        fresh = self.fresh

        patterns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.patterns, Unset):
            patterns = self.patterns

        proxy_mode: Union[Unset, str] = UNSET
        if not isinstance(self.proxy_mode, Unset):
            proxy_mode = self.proxy_mode.value

        proxy_region = self.proxy_region

        proxy_session = self.proxy_session

        rotate_user_agent = self.rotate_user_agent

        enable_bot_protection = self.enable_bot_protection

        max_consecutive_errors = self.max_consecutive_errors

        user_agent = self.user_agent

        wait_for_selectors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.wait_for_selectors, Unset):
            wait_for_selectors = self.wait_for_selectors

        webhook_url = self.webhook_url

        webhook_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.webhook_headers, Unset):
            webhook_headers = self.webhook_headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if depth is not UNSET:
            field_dict["depth"] = depth
        if link_limit is not UNSET:
            field_dict["link_limit"] = link_limit
        if include_subdomains is not UNSET:
            field_dict["include_subdomains"] = include_subdomains
        if render_js is not UNSET:
            field_dict["render_js"] = render_js
        if include_html is not UNSET:
            field_dict["include_html"] = include_html
        if fresh is not UNSET:
            field_dict["fresh"] = fresh
        if patterns is not UNSET:
            field_dict["patterns"] = patterns
        if proxy_mode is not UNSET:
            field_dict["proxy_mode"] = proxy_mode
        if proxy_region is not UNSET:
            field_dict["proxy_region"] = proxy_region
        if proxy_session is not UNSET:
            field_dict["proxy_session"] = proxy_session
        if rotate_user_agent is not UNSET:
            field_dict["rotate_user_agent"] = rotate_user_agent
        if enable_bot_protection is not UNSET:
            field_dict["enable_bot_protection"] = enable_bot_protection
        if max_consecutive_errors is not UNSET:
            field_dict["max_consecutive_errors"] = max_consecutive_errors
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if wait_for_selectors is not UNSET:
            field_dict["wait_for_selectors"] = wait_for_selectors
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if webhook_headers is not UNSET:
            field_dict["webhook_headers"] = webhook_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crawl_create_request_webhook_headers import CrawlCreateRequestWebhookHeaders

        d = dict(src_dict)
        url = d.pop("url")

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, CrawlCreateRequestFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CrawlCreateRequestFormat(_format_)

        depth = d.pop("depth", UNSET)

        link_limit = d.pop("link_limit", UNSET)

        include_subdomains = d.pop("include_subdomains", UNSET)

        render_js = d.pop("render_js", UNSET)

        include_html = d.pop("include_html", UNSET)

        fresh = d.pop("fresh", UNSET)

        patterns = cast(list[str], d.pop("patterns", UNSET))

        _proxy_mode = d.pop("proxy_mode", UNSET)
        proxy_mode: Union[Unset, CrawlCreateRequestProxyMode]
        if isinstance(_proxy_mode, Unset):
            proxy_mode = UNSET
        else:
            proxy_mode = CrawlCreateRequestProxyMode(_proxy_mode)

        proxy_region = d.pop("proxy_region", UNSET)

        proxy_session = d.pop("proxy_session", UNSET)

        rotate_user_agent = d.pop("rotate_user_agent", UNSET)

        enable_bot_protection = d.pop("enable_bot_protection", UNSET)

        max_consecutive_errors = d.pop("max_consecutive_errors", UNSET)

        user_agent = d.pop("user_agent", UNSET)

        wait_for_selectors = cast(list[str], d.pop("wait_for_selectors", UNSET))

        webhook_url = d.pop("webhook_url", UNSET)

        _webhook_headers = d.pop("webhook_headers", UNSET)
        webhook_headers: Union[Unset, CrawlCreateRequestWebhookHeaders]
        if isinstance(_webhook_headers, Unset):
            webhook_headers = UNSET
        else:
            webhook_headers = CrawlCreateRequestWebhookHeaders.from_dict(_webhook_headers)

        crawl_create_request = cls(
            url=url,
            format_=format_,
            depth=depth,
            link_limit=link_limit,
            include_subdomains=include_subdomains,
            render_js=render_js,
            include_html=include_html,
            fresh=fresh,
            patterns=patterns,
            proxy_mode=proxy_mode,
            proxy_region=proxy_region,
            proxy_session=proxy_session,
            rotate_user_agent=rotate_user_agent,
            enable_bot_protection=enable_bot_protection,
            max_consecutive_errors=max_consecutive_errors,
            user_agent=user_agent,
            wait_for_selectors=wait_for_selectors,
            webhook_url=webhook_url,
            webhook_headers=webhook_headers,
        )

        crawl_create_request.additional_properties = d
        return crawl_create_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
