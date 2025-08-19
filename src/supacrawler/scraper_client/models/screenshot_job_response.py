from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.screenshot_job_response_status import ScreenshotJobResponseStatus
from ..models.screenshot_job_response_type import ScreenshotJobResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.screenshot_metadata import ScreenshotMetadata


T = TypeVar("T", bound="ScreenshotJobResponse")


@_attrs_define
class ScreenshotJobResponse:
    """
    Attributes:
        success (bool):
        job_id (str):
        type_ (Union[Unset, ScreenshotJobResponseType]):
        status (Union[Unset, ScreenshotJobResponseStatus]):
        url (Union[Unset, str]):
        metadata (Union[Unset, ScreenshotMetadata]):
    """

    success: bool
    job_id: str
    type_: Union[Unset, ScreenshotJobResponseType] = UNSET
    status: Union[Unset, ScreenshotJobResponseStatus] = UNSET
    url: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ScreenshotMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        job_id = self.job_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        url = self.url

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "job_id": job_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.screenshot_metadata import ScreenshotMetadata

        d = dict(src_dict)
        success = d.pop("success")

        job_id = d.pop("job_id")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ScreenshotJobResponseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ScreenshotJobResponseType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScreenshotJobResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScreenshotJobResponseStatus(_status)

        url = d.pop("url", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ScreenshotMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ScreenshotMetadata.from_dict(_metadata)

        screenshot_job_response = cls(
            success=success,
            job_id=job_id,
            type_=type_,
            status=status,
            url=url,
            metadata=metadata,
        )

        screenshot_job_response.additional_properties = d
        return screenshot_job_response

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
