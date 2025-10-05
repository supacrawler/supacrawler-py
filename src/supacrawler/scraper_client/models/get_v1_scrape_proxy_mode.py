from enum import Enum


class GetV1ScrapeProxyMode(str, Enum):
    OFF = "off"
    RESIDENTIAL = "residential"
    SHARED_POOL = "shared_pool"

    def __str__(self) -> str:
        return str(self.value)
