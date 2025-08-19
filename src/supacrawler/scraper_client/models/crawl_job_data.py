from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crawl_job_data_crawl_data import CrawlJobDataCrawlData
    from ..models.crawl_job_data_error_data import CrawlJobDataErrorData
    from ..models.crawl_statistics import CrawlStatistics


T = TypeVar("T", bound="CrawlJobData")


@_attrs_define
class CrawlJobData:
    """
    Attributes:
        url (Union[Unset, str]):
        crawl_data (Union[Unset, CrawlJobDataCrawlData]):
        error_data (Union[Unset, CrawlJobDataErrorData]):
        statistics (Union[Unset, CrawlStatistics]):
        render_js (Union[Unset, bool]):
    """

    url: Union[Unset, str] = UNSET
    crawl_data: Union[Unset, "CrawlJobDataCrawlData"] = UNSET
    error_data: Union[Unset, "CrawlJobDataErrorData"] = UNSET
    statistics: Union[Unset, "CrawlStatistics"] = UNSET
    render_js: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        crawl_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.crawl_data, Unset):
            crawl_data = self.crawl_data.to_dict()

        error_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error_data, Unset):
            error_data = self.error_data.to_dict()

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        render_js = self.render_js

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if crawl_data is not UNSET:
            field_dict["crawl_data"] = crawl_data
        if error_data is not UNSET:
            field_dict["error_data"] = error_data
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if render_js is not UNSET:
            field_dict["render_js"] = render_js

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crawl_job_data_crawl_data import CrawlJobDataCrawlData
        from ..models.crawl_job_data_error_data import CrawlJobDataErrorData
        from ..models.crawl_statistics import CrawlStatistics

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _crawl_data = d.pop("crawl_data", UNSET)
        crawl_data: Union[Unset, CrawlJobDataCrawlData]
        if isinstance(_crawl_data, Unset):
            crawl_data = UNSET
        else:
            crawl_data = CrawlJobDataCrawlData.from_dict(_crawl_data)

        _error_data = d.pop("error_data", UNSET)
        error_data: Union[Unset, CrawlJobDataErrorData]
        if isinstance(_error_data, Unset):
            error_data = UNSET
        else:
            error_data = CrawlJobDataErrorData.from_dict(_error_data)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CrawlStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CrawlStatistics.from_dict(_statistics)

        render_js = d.pop("render_js", UNSET)

        crawl_job_data = cls(
            url=url,
            crawl_data=crawl_data,
            error_data=error_data,
            statistics=statistics,
            render_js=render_js,
        )

        crawl_job_data.additional_properties = d
        return crawl_job_data

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
