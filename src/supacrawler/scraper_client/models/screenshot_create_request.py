from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.screenshot_create_request_block_resources_item import ScreenshotCreateRequestBlockResourcesItem
from ..models.screenshot_create_request_device import ScreenshotCreateRequestDevice
from ..models.screenshot_create_request_format import ScreenshotCreateRequestFormat
from ..models.screenshot_create_request_wait_until import ScreenshotCreateRequestWaitUntil
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.screenshot_create_request_cookies_item import ScreenshotCreateRequestCookiesItem
    from ..models.screenshot_create_request_headers import ScreenshotCreateRequestHeaders


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
        quality (Union[Unset, int]):
        device (Union[Unset, ScreenshotCreateRequestDevice]):
        wait_until (Union[Unset, ScreenshotCreateRequestWaitUntil]):
        timeout (Union[Unset, int]):
        dark_mode (Union[Unset, bool]):
        delay (Union[Unset, int]):
        wait_for_selector (Union[Unset, str]):
        click_selector (Union[Unset, str]):
        hide_selectors (Union[Unset, list[str]]):
        block_ads (Union[Unset, bool]):
        block_cookies (Union[Unset, bool]):
        block_chats (Union[Unset, bool]):
        block_trackers (Union[Unset, bool]):
        block_resources (Union[Unset, list[ScreenshotCreateRequestBlockResourcesItem]]):
        user_agent (Union[Unset, str]):
        headers (Union[Unset, ScreenshotCreateRequestHeaders]):
        cookies (Union[Unset, list['ScreenshotCreateRequestCookiesItem']]):
        reduced_motion (Union[Unset, bool]):
        high_contrast (Union[Unset, bool]):
        disable_js (Union[Unset, bool]):
        print_mode (Union[Unset, bool]):
        ignore_https (Union[Unset, bool]):
        device_scale (Union[Unset, float]):
        is_mobile (Union[Unset, bool]):
        has_touch (Union[Unset, bool]):
        is_landscape (Union[Unset, bool]):
        stream (Union[Unset, bool]):
    """

    url: str
    full_page: Union[Unset, bool] = UNSET
    format_: Union[Unset, ScreenshotCreateRequestFormat] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    quality: Union[Unset, int] = UNSET
    device: Union[Unset, ScreenshotCreateRequestDevice] = UNSET
    wait_until: Union[Unset, ScreenshotCreateRequestWaitUntil] = UNSET
    timeout: Union[Unset, int] = UNSET
    dark_mode: Union[Unset, bool] = UNSET
    delay: Union[Unset, int] = UNSET
    wait_for_selector: Union[Unset, str] = UNSET
    click_selector: Union[Unset, str] = UNSET
    hide_selectors: Union[Unset, list[str]] = UNSET
    block_ads: Union[Unset, bool] = UNSET
    block_cookies: Union[Unset, bool] = UNSET
    block_chats: Union[Unset, bool] = UNSET
    block_trackers: Union[Unset, bool] = UNSET
    block_resources: Union[Unset, list[ScreenshotCreateRequestBlockResourcesItem]] = UNSET
    user_agent: Union[Unset, str] = UNSET
    headers: Union[Unset, "ScreenshotCreateRequestHeaders"] = UNSET
    cookies: Union[Unset, list["ScreenshotCreateRequestCookiesItem"]] = UNSET
    reduced_motion: Union[Unset, bool] = UNSET
    high_contrast: Union[Unset, bool] = UNSET
    disable_js: Union[Unset, bool] = UNSET
    print_mode: Union[Unset, bool] = UNSET
    ignore_https: Union[Unset, bool] = UNSET
    device_scale: Union[Unset, float] = UNSET
    is_mobile: Union[Unset, bool] = UNSET
    has_touch: Union[Unset, bool] = UNSET
    is_landscape: Union[Unset, bool] = UNSET
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

        quality = self.quality

        device: Union[Unset, str] = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.value

        wait_until: Union[Unset, str] = UNSET
        if not isinstance(self.wait_until, Unset):
            wait_until = self.wait_until.value

        timeout = self.timeout

        dark_mode = self.dark_mode

        delay = self.delay

        wait_for_selector = self.wait_for_selector

        click_selector = self.click_selector

        hide_selectors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.hide_selectors, Unset):
            hide_selectors = self.hide_selectors

        block_ads = self.block_ads

        block_cookies = self.block_cookies

        block_chats = self.block_chats

        block_trackers = self.block_trackers

        block_resources: Union[Unset, list[str]] = UNSET
        if not isinstance(self.block_resources, Unset):
            block_resources = []
            for block_resources_item_data in self.block_resources:
                block_resources_item = block_resources_item_data.value
                block_resources.append(block_resources_item)

        user_agent = self.user_agent

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        cookies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cookies, Unset):
            cookies = []
            for cookies_item_data in self.cookies:
                cookies_item = cookies_item_data.to_dict()
                cookies.append(cookies_item)

        reduced_motion = self.reduced_motion

        high_contrast = self.high_contrast

        disable_js = self.disable_js

        print_mode = self.print_mode

        ignore_https = self.ignore_https

        device_scale = self.device_scale

        is_mobile = self.is_mobile

        has_touch = self.has_touch

        is_landscape = self.is_landscape

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
        if quality is not UNSET:
            field_dict["quality"] = quality
        if device is not UNSET:
            field_dict["device"] = device
        if wait_until is not UNSET:
            field_dict["wait_until"] = wait_until
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if dark_mode is not UNSET:
            field_dict["dark_mode"] = dark_mode
        if delay is not UNSET:
            field_dict["delay"] = delay
        if wait_for_selector is not UNSET:
            field_dict["wait_for_selector"] = wait_for_selector
        if click_selector is not UNSET:
            field_dict["click_selector"] = click_selector
        if hide_selectors is not UNSET:
            field_dict["hide_selectors"] = hide_selectors
        if block_ads is not UNSET:
            field_dict["block_ads"] = block_ads
        if block_cookies is not UNSET:
            field_dict["block_cookies"] = block_cookies
        if block_chats is not UNSET:
            field_dict["block_chats"] = block_chats
        if block_trackers is not UNSET:
            field_dict["block_trackers"] = block_trackers
        if block_resources is not UNSET:
            field_dict["block_resources"] = block_resources
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if headers is not UNSET:
            field_dict["headers"] = headers
        if cookies is not UNSET:
            field_dict["cookies"] = cookies
        if reduced_motion is not UNSET:
            field_dict["reduced_motion"] = reduced_motion
        if high_contrast is not UNSET:
            field_dict["high_contrast"] = high_contrast
        if disable_js is not UNSET:
            field_dict["disable_js"] = disable_js
        if print_mode is not UNSET:
            field_dict["print_mode"] = print_mode
        if ignore_https is not UNSET:
            field_dict["ignore_https"] = ignore_https
        if device_scale is not UNSET:
            field_dict["device_scale"] = device_scale
        if is_mobile is not UNSET:
            field_dict["is_mobile"] = is_mobile
        if has_touch is not UNSET:
            field_dict["has_touch"] = has_touch
        if is_landscape is not UNSET:
            field_dict["is_landscape"] = is_landscape
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.screenshot_create_request_cookies_item import ScreenshotCreateRequestCookiesItem
        from ..models.screenshot_create_request_headers import ScreenshotCreateRequestHeaders

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

        quality = d.pop("quality", UNSET)

        _device = d.pop("device", UNSET)
        device: Union[Unset, ScreenshotCreateRequestDevice]
        if isinstance(_device, Unset):
            device = UNSET
        else:
            device = ScreenshotCreateRequestDevice(_device)

        _wait_until = d.pop("wait_until", UNSET)
        wait_until: Union[Unset, ScreenshotCreateRequestWaitUntil]
        if isinstance(_wait_until, Unset):
            wait_until = UNSET
        else:
            wait_until = ScreenshotCreateRequestWaitUntil(_wait_until)

        timeout = d.pop("timeout", UNSET)

        dark_mode = d.pop("dark_mode", UNSET)

        delay = d.pop("delay", UNSET)

        wait_for_selector = d.pop("wait_for_selector", UNSET)

        click_selector = d.pop("click_selector", UNSET)

        hide_selectors = cast(list[str], d.pop("hide_selectors", UNSET))

        block_ads = d.pop("block_ads", UNSET)

        block_cookies = d.pop("block_cookies", UNSET)

        block_chats = d.pop("block_chats", UNSET)

        block_trackers = d.pop("block_trackers", UNSET)

        block_resources = []
        _block_resources = d.pop("block_resources", UNSET)
        for block_resources_item_data in _block_resources or []:
            block_resources_item = ScreenshotCreateRequestBlockResourcesItem(block_resources_item_data)

            block_resources.append(block_resources_item)

        user_agent = d.pop("user_agent", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, ScreenshotCreateRequestHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ScreenshotCreateRequestHeaders.from_dict(_headers)

        cookies = []
        _cookies = d.pop("cookies", UNSET)
        for cookies_item_data in _cookies or []:
            cookies_item = ScreenshotCreateRequestCookiesItem.from_dict(cookies_item_data)

            cookies.append(cookies_item)

        reduced_motion = d.pop("reduced_motion", UNSET)

        high_contrast = d.pop("high_contrast", UNSET)

        disable_js = d.pop("disable_js", UNSET)

        print_mode = d.pop("print_mode", UNSET)

        ignore_https = d.pop("ignore_https", UNSET)

        device_scale = d.pop("device_scale", UNSET)

        is_mobile = d.pop("is_mobile", UNSET)

        has_touch = d.pop("has_touch", UNSET)

        is_landscape = d.pop("is_landscape", UNSET)

        stream = d.pop("stream", UNSET)

        screenshot_create_request = cls(
            url=url,
            full_page=full_page,
            format_=format_,
            width=width,
            height=height,
            quality=quality,
            device=device,
            wait_until=wait_until,
            timeout=timeout,
            dark_mode=dark_mode,
            delay=delay,
            wait_for_selector=wait_for_selector,
            click_selector=click_selector,
            hide_selectors=hide_selectors,
            block_ads=block_ads,
            block_cookies=block_cookies,
            block_chats=block_chats,
            block_trackers=block_trackers,
            block_resources=block_resources,
            user_agent=user_agent,
            headers=headers,
            cookies=cookies,
            reduced_motion=reduced_motion,
            high_contrast=high_contrast,
            disable_js=disable_js,
            print_mode=print_mode,
            ignore_https=ignore_https,
            device_scale=device_scale,
            is_mobile=is_mobile,
            has_touch=has_touch,
            is_landscape=is_landscape,
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
