from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.screenshot_get_response_status import ScreenshotGetResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.screenshot_metadata import ScreenshotMetadata


T = TypeVar("T", bound="ScreenshotGetResponse")


@_attrs_define
class ScreenshotGetResponse:
    """
    Attributes:
        success (bool):
        job_id (Union[Unset, str]):
        url (Union[Unset, str]): Source URL of the page
        screenshot (Union[Unset, str]): Signed or public URL to the image
        status (Union[Unset, ScreenshotGetResponseStatus]):
        metadata (Union[Unset, ScreenshotMetadata]):
    """

    success: bool
    job_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    screenshot: Union[Unset, str] = UNSET
    status: Union[Unset, ScreenshotGetResponseStatus] = UNSET
    metadata: Union[Unset, "ScreenshotMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        job_id = self.job_id

        url = self.url

        screenshot = self.screenshot

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if url is not UNSET:
            field_dict["url"] = url
        if screenshot is not UNSET:
            field_dict["screenshot"] = screenshot
        if status is not UNSET:
            field_dict["status"] = status
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.screenshot_metadata import ScreenshotMetadata

        d = dict(src_dict)
        success = d.pop("success")

        job_id = d.pop("job_id", UNSET)

        url = d.pop("url", UNSET)

        screenshot = d.pop("screenshot", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScreenshotGetResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScreenshotGetResponseStatus(_status)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ScreenshotMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ScreenshotMetadata.from_dict(_metadata)

        screenshot_get_response = cls(
            success=success,
            job_id=job_id,
            url=url,
            screenshot=screenshot,
            status=status,
            metadata=metadata,
        )

        screenshot_get_response.additional_properties = d
        return screenshot_get_response

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
