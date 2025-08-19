from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.page_content import PageContent


T = TypeVar("T", bound="CrawlJobDataCrawlData")


@_attrs_define
class CrawlJobDataCrawlData:
    """ """

    additional_properties: dict[str, "PageContent"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_content import PageContent

        d = dict(src_dict)
        crawl_job_data_crawl_data = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PageContent.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        crawl_job_data_crawl_data.additional_properties = additional_properties
        return crawl_job_data_crawl_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "PageContent":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "PageContent") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
