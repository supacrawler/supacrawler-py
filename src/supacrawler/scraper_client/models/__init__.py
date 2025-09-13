"""Contains all the data models used in inputs/outputs"""

from .crawl_create_request import CrawlCreateRequest
from .crawl_create_request_format import CrawlCreateRequestFormat
from .crawl_create_response import CrawlCreateResponse
from .crawl_job_data import CrawlJobData
from .crawl_job_data_crawl_data import CrawlJobDataCrawlData
from .crawl_job_data_error_data import CrawlJobDataErrorData
from .crawl_statistics import CrawlStatistics
from .crawl_status_response import CrawlStatusResponse
from .crawl_status_response_status import CrawlStatusResponseStatus
from .error import Error
from .get_v1_scrape_format import GetV1ScrapeFormat
from .page_content import PageContent
from .page_metadata import PageMetadata
from .parse_create_request import ParseCreateRequest
from .parse_create_request_output_format import ParseCreateRequestOutputFormat
from .parse_create_request_schema import ParseCreateRequestSchema
from .parse_examples_response import ParseExamplesResponse
from .parse_examples_response_examples import ParseExamplesResponseExamples
from .parse_examples_response_examples_additional_property import ParseExamplesResponseExamplesAdditionalProperty
from .parse_response import ParseResponse
from .parse_response_partial_results_item import ParseResponsePartialResultsItem
from .parse_response_workflow_status import ParseResponseWorkflowStatus
from .parse_templates_response import ParseTemplatesResponse
from .parse_templates_response_templates import ParseTemplatesResponseTemplates
from .parse_validation_result import ParseValidationResult
from .parse_validation_result_format import ParseValidationResultFormat
from .scrape_metadata import ScrapeMetadata
from .scrape_response import ScrapeResponse
from .screenshot_create_request import ScreenshotCreateRequest
from .screenshot_create_request_block_resources_item import ScreenshotCreateRequestBlockResourcesItem
from .screenshot_create_request_cookies_item import ScreenshotCreateRequestCookiesItem
from .screenshot_create_request_device import ScreenshotCreateRequestDevice
from .screenshot_create_request_format import ScreenshotCreateRequestFormat
from .screenshot_create_request_headers import ScreenshotCreateRequestHeaders
from .screenshot_create_request_wait_until import ScreenshotCreateRequestWaitUntil
from .screenshot_get_response import ScreenshotGetResponse
from .screenshot_get_response_status import ScreenshotGetResponseStatus
from .screenshot_job_response import ScreenshotJobResponse
from .screenshot_job_response_status import ScreenshotJobResponseStatus
from .screenshot_job_response_type import ScreenshotJobResponseType
from .screenshot_metadata import ScreenshotMetadata

__all__ = (
    "CrawlCreateRequest",
    "CrawlCreateRequestFormat",
    "CrawlCreateResponse",
    "CrawlJobData",
    "CrawlJobDataCrawlData",
    "CrawlJobDataErrorData",
    "CrawlStatistics",
    "CrawlStatusResponse",
    "CrawlStatusResponseStatus",
    "Error",
    "GetV1ScrapeFormat",
    "PageContent",
    "PageMetadata",
    "ParseCreateRequest",
    "ParseCreateRequestOutputFormat",
    "ParseCreateRequestSchema",
    "ParseExamplesResponse",
    "ParseExamplesResponseExamples",
    "ParseExamplesResponseExamplesAdditionalProperty",
    "ParseResponse",
    "ParseResponsePartialResultsItem",
    "ParseResponseWorkflowStatus",
    "ParseTemplatesResponse",
    "ParseTemplatesResponseTemplates",
    "ParseValidationResult",
    "ParseValidationResultFormat",
    "ScrapeMetadata",
    "ScrapeResponse",
    "ScreenshotCreateRequest",
    "ScreenshotCreateRequestBlockResourcesItem",
    "ScreenshotCreateRequestCookiesItem",
    "ScreenshotCreateRequestDevice",
    "ScreenshotCreateRequestFormat",
    "ScreenshotCreateRequestHeaders",
    "ScreenshotCreateRequestWaitUntil",
    "ScreenshotGetResponse",
    "ScreenshotGetResponseStatus",
    "ScreenshotJobResponse",
    "ScreenshotJobResponseStatus",
    "ScreenshotJobResponseType",
    "ScreenshotMetadata",
)
