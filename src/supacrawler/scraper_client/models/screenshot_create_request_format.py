from enum import Enum


class ScreenshotCreateRequestFormat(str, Enum):
    JPEG = "jpeg"
    PNG = "png"

    def __str__(self) -> str:
        return str(self.value)
