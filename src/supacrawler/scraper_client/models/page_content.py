from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_metadata import PageMetadata


T = TypeVar("T", bound="PageContent")


@_attrs_define
class PageContent:
    """
    Attributes:
        markdown (str):
        links (list[str]): All discovered links on the page
        metadata (PageMetadata):
        html (Union[Unset, str]):
    """

    markdown: str
    links: list[str]
    metadata: "PageMetadata"
    html: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        markdown = self.markdown

        links = self.links

        metadata = self.metadata.to_dict()

        html = self.html

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "markdown": markdown,
                "links": links,
                "metadata": metadata,
            }
        )
        if html is not UNSET:
            field_dict["html"] = html

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_metadata import PageMetadata

        d = dict(src_dict)
        markdown = d.pop("markdown")

        links = cast(list[str], d.pop("links"))

        metadata = PageMetadata.from_dict(d.pop("metadata"))

        html = d.pop("html", UNSET)

        page_content = cls(
            markdown=markdown,
            links=links,
            metadata=metadata,
            html=html,
        )

        page_content.additional_properties = d
        return page_content

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
