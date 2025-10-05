from enum import Enum


class CrawlCreateRequestProxyMode(str, Enum):
    OFF = "off"
    RESIDENTIAL = "residential"
    SHARED_POOL = "shared_pool"

    def __str__(self) -> str:
        return str(self.value)
