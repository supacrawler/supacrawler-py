from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crawl_create_request_format import CrawlCreateRequestFormat
from ..types import UNSET, Unset

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
    """

    url: str
    format_: Union[Unset, CrawlCreateRequestFormat] = UNSET
    depth: Union[Unset, int] = UNSET
    link_limit: Union[Unset, int] = UNSET
    include_subdomains: Union[Unset, bool] = UNSET
    render_js: Union[Unset, bool] = UNSET
    include_html: Union[Unset, bool] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        crawl_create_request = cls(
            url=url,
            format_=format_,
            depth=depth,
            link_limit=link_limit,
            include_subdomains=include_subdomains,
            render_js=render_js,
            include_html=include_html,
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
