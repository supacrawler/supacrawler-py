from enum import Enum


class ScreenshotCreateRequestBlockResourcesItem(str, Enum):
    FONT = "font"
    IMAGE = "image"
    SCRIPT = "script"
    STYLESHEET = "stylesheet"

    def __str__(self) -> str:
        return str(self.value)
