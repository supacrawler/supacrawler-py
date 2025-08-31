from enum import Enum


class GetV1ScrapeFormat(str, Enum):
    LINKS = "links"
    MARKDOWN = "markdown"

    def __str__(self) -> str:
        return str(self.value)
