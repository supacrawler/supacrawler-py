from enum import Enum


class ParseResponseWorkflowStatus(str, Enum):
    ANALYZING = "analyzing"
    COMPLETED = "completed"
    CRAWLING = "crawling"
    EXTRACTING = "extracting"
    FAILED = "failed"
    FORMATTING = "formatting"
    SCRAPING = "scraping"

    def __str__(self) -> str:
        return str(self.value)
