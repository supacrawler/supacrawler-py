from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScreenshotMetadata")


@_attrs_define
class ScreenshotMetadata:
    """
    Attributes:
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        format_ (Union[Unset, str]):
        quality (Union[Unset, int]):
        file_size (Union[Unset, int]):
        load_time (Union[Unset, int]):
        device (Union[Unset, str]):
        device_scale (Union[Unset, float]):
    """

    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    format_: Union[Unset, str] = UNSET
    quality: Union[Unset, int] = UNSET
    file_size: Union[Unset, int] = UNSET
    load_time: Union[Unset, int] = UNSET
    device: Union[Unset, str] = UNSET
    device_scale: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        format_ = self.format_

        quality = self.quality

        file_size = self.file_size

        load_time = self.load_time

        device = self.device

        device_scale = self.device_scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if format_ is not UNSET:
            field_dict["format"] = format_
        if quality is not UNSET:
            field_dict["quality"] = quality
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if load_time is not UNSET:
            field_dict["load_time"] = load_time
        if device is not UNSET:
            field_dict["device"] = device
        if device_scale is not UNSET:
            field_dict["device_scale"] = device_scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        format_ = d.pop("format", UNSET)

        quality = d.pop("quality", UNSET)

        file_size = d.pop("file_size", UNSET)

        load_time = d.pop("load_time", UNSET)

        device = d.pop("device", UNSET)

        device_scale = d.pop("device_scale", UNSET)

        screenshot_metadata = cls(
            width=width,
            height=height,
            format_=format_,
            quality=quality,
            file_size=file_size,
            load_time=load_time,
            device=device,
            device_scale=device_scale,
        )

        screenshot_metadata.additional_properties = d
        return screenshot_metadata

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
