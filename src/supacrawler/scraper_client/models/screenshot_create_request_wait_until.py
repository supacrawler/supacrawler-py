from enum import Enum


class ScreenshotCreateRequestWaitUntil(str, Enum):
    DOMCONTENTLOADED = "domcontentloaded"
    LOAD = "load"
    NETWORKIDLE = "networkidle"

    def __str__(self) -> str:
        return str(self.value)
