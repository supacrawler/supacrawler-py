from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scrape_metadata import ScrapeMetadata


T = TypeVar("T", bound="ScrapeResponse")


@_attrs_define
class ScrapeResponse:
    """
    Attributes:
        success (bool):
        url (str):
        metadata (ScrapeMetadata):
        title (Union[Unset, str]):
        content (Union[Unset, str]): Markdown or HTML depending on format
        links (Union[Unset, list[str]]):
        discovered (Union[Unset, int]):
    """

    success: bool
    url: str
    metadata: "ScrapeMetadata"
    title: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    links: Union[Unset, list[str]] = UNSET
    discovered: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        url = self.url

        metadata = self.metadata.to_dict()

        title = self.title

        content = self.content

        links: Union[Unset, list[str]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        discovered = self.discovered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "url": url,
                "metadata": metadata,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if content is not UNSET:
            field_dict["content"] = content
        if links is not UNSET:
            field_dict["links"] = links
        if discovered is not UNSET:
            field_dict["discovered"] = discovered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scrape_metadata import ScrapeMetadata

        d = dict(src_dict)
        success = d.pop("success")

        url = d.pop("url")

        metadata = ScrapeMetadata.from_dict(d.pop("metadata"))

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        links = cast(list[str], d.pop("links", UNSET))

        discovered = d.pop("discovered", UNSET)

        scrape_response = cls(
            success=success,
            url=url,
            metadata=metadata,
            title=title,
            content=content,
            links=links,
            discovered=discovered,
        )

        scrape_response.additional_properties = d
        return scrape_response

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
