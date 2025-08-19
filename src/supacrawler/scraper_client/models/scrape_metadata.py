from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScrapeMetadata")


@_attrs_define
class ScrapeMetadata:
    """
    Attributes:
        status_code (Union[Unset, int]):
        depth (Union[Unset, int]):
        source_url (Union[Unset, str]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        language (Union[Unset, str]):
        canonical (Union[Unset, str]):
        favicon (Union[Unset, str]):
        og_title (Union[Unset, str]):
        og_description (Union[Unset, str]):
        og_image (Union[Unset, str]):
        og_site_name (Union[Unset, str]):
        twitter_title (Union[Unset, str]):
        twitter_description (Union[Unset, str]):
        twitter_image (Union[Unset, str]):
    """

    status_code: Union[Unset, int] = UNSET
    depth: Union[Unset, int] = UNSET
    source_url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    canonical: Union[Unset, str] = UNSET
    favicon: Union[Unset, str] = UNSET
    og_title: Union[Unset, str] = UNSET
    og_description: Union[Unset, str] = UNSET
    og_image: Union[Unset, str] = UNSET
    og_site_name: Union[Unset, str] = UNSET
    twitter_title: Union[Unset, str] = UNSET
    twitter_description: Union[Unset, str] = UNSET
    twitter_image: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        depth = self.depth

        source_url = self.source_url

        title = self.title

        description = self.description

        language = self.language

        canonical = self.canonical

        favicon = self.favicon

        og_title = self.og_title

        og_description = self.og_description

        og_image = self.og_image

        og_site_name = self.og_site_name

        twitter_title = self.twitter_title

        twitter_description = self.twitter_description

        twitter_image = self.twitter_image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if depth is not UNSET:
            field_dict["depth"] = depth
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if language is not UNSET:
            field_dict["language"] = language
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if favicon is not UNSET:
            field_dict["favicon"] = favicon
        if og_title is not UNSET:
            field_dict["og_title"] = og_title
        if og_description is not UNSET:
            field_dict["og_description"] = og_description
        if og_image is not UNSET:
            field_dict["og_image"] = og_image
        if og_site_name is not UNSET:
            field_dict["og_site_name"] = og_site_name
        if twitter_title is not UNSET:
            field_dict["twitter_title"] = twitter_title
        if twitter_description is not UNSET:
            field_dict["twitter_description"] = twitter_description
        if twitter_image is not UNSET:
            field_dict["twitter_image"] = twitter_image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_code = d.pop("status_code", UNSET)

        depth = d.pop("depth", UNSET)

        source_url = d.pop("source_url", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        language = d.pop("language", UNSET)

        canonical = d.pop("canonical", UNSET)

        favicon = d.pop("favicon", UNSET)

        og_title = d.pop("og_title", UNSET)

        og_description = d.pop("og_description", UNSET)

        og_image = d.pop("og_image", UNSET)

        og_site_name = d.pop("og_site_name", UNSET)

        twitter_title = d.pop("twitter_title", UNSET)

        twitter_description = d.pop("twitter_description", UNSET)

        twitter_image = d.pop("twitter_image", UNSET)

        scrape_metadata = cls(
            status_code=status_code,
            depth=depth,
            source_url=source_url,
            title=title,
            description=description,
            language=language,
            canonical=canonical,
            favicon=favicon,
            og_title=og_title,
            og_description=og_description,
            og_image=og_image,
            og_site_name=og_site_name,
            twitter_title=twitter_title,
            twitter_description=twitter_description,
            twitter_image=twitter_image,
        )

        scrape_metadata.additional_properties = d
        return scrape_metadata

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
