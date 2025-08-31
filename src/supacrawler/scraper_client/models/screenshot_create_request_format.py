from enum import Enum


class ScreenshotCreateRequestFormat(str, Enum):
    JPEG = "jpeg"
    JPG = "jpg"
    PNG = "png"
    WEBP = "webp"

    def __str__(self) -> str:
        return str(self.value)
