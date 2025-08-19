from enum import Enum


class ScreenshotGetResponseStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
