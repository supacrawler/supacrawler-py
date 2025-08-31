from enum import Enum


class ScreenshotCreateRequestDevice(str, Enum):
    CUSTOM = "custom"
    DESKTOP = "desktop"
    MOBILE = "mobile"
    TABLET = "tablet"

    def __str__(self) -> str:
        return str(self.value)
