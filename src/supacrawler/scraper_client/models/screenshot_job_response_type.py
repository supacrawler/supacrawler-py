from enum import Enum


class ScreenshotJobResponseType(str, Enum):
    SCREENSHOT = "screenshot"

    def __str__(self) -> str:
        return str(self.value)
