from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crawl_status_response_status import CrawlStatusResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crawl_job_data import CrawlJobData


T = TypeVar("T", bound="CrawlStatusResponse")


@_attrs_define
class CrawlStatusResponse:
    """
    Attributes:
        success (bool):
        status (CrawlStatusResponseStatus):
        job_id (Union[Unset, str]):
        data (Union[Unset, CrawlJobData]):
        error (Union[Unset, str]):
    """

    success: bool
    status: CrawlStatusResponseStatus
    job_id: Union[Unset, str] = UNSET
    data: Union[Unset, "CrawlJobData"] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status.value

        job_id = self.job_id

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
            }
        )
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crawl_job_data import CrawlJobData

        d = dict(src_dict)
        success = d.pop("success")

        status = CrawlStatusResponseStatus(d.pop("status"))

        job_id = d.pop("job_id", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, CrawlJobData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CrawlJobData.from_dict(_data)

        error = d.pop("error", UNSET)

        crawl_status_response = cls(
            success=success,
            status=status,
            job_id=job_id,
            data=data,
            error=error,
        )

        crawl_status_response.additional_properties = d
        return crawl_status_response

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
