from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.screenshot_create_request_format import ScreenshotCreateRequestFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScreenshotCreateRequest")


@_attrs_define
class ScreenshotCreateRequest:
    """
    Attributes:
        url (str):
        full_page (Union[Unset, bool]):
        format_ (Union[Unset, ScreenshotCreateRequestFormat]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        stream (Union[Unset, bool]):
    """

    url: str
    full_page: Union[Unset, bool] = UNSET
    format_: Union[Unset, ScreenshotCreateRequestFormat] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    stream: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        full_page = self.full_page

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        width = self.width

        height = self.height

        stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if full_page is not UNSET:
            field_dict["full_page"] = full_page
        if format_ is not UNSET:
            field_dict["format"] = format_
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        full_page = d.pop("full_page", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ScreenshotCreateRequestFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ScreenshotCreateRequestFormat(_format_)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        stream = d.pop("stream", UNSET)

        screenshot_create_request = cls(
            url=url,
            full_page=full_page,
            format_=format_,
            width=width,
            height=height,
            stream=stream,
        )

        screenshot_create_request.additional_properties = d
        return screenshot_create_request

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
