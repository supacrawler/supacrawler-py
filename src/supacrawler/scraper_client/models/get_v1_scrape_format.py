from enum import Enum


class GetV1ScrapeFormat(str, Enum):
    HTML = "html"
    LINKS = "links"
    MARKDOWN = "markdown"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
