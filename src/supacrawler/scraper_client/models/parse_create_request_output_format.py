from enum import Enum


class ParseCreateRequestOutputFormat(str, Enum):
    CSV = "csv"
    JSON = "json"
    MARKDOWN = "markdown"
    XML = "xml"
    YAML = "yaml"

    def __str__(self) -> str:
        return str(self.value)
