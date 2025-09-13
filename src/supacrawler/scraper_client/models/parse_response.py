from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parse_response_workflow_status import ParseResponseWorkflowStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parse_response_partial_results_item import ParseResponsePartialResultsItem


T = TypeVar("T", bound="ParseResponse")


@_attrs_define
class ParseResponse:
    """
    Attributes:
        success (bool): Whether the parsing operation succeeded
        data (Union[Unset, Any]): Extracted data as JSON object, CSV string, or markdown
        workflow_status (Union[Unset, ParseResponseWorkflowStatus]): Current workflow stage
        pages_processed (Union[Unset, int]): Number of pages processed so far
        total_pages (Union[Unset, int]): Total pages discovered (if known)
        partial_results (Union[Unset, list['ParseResponsePartialResultsItem']]): Incremental results for streaming
            responses
        execution_time (Union[Unset, int]): Total execution time in milliseconds
        error (Union[Unset, str]): Error message if parsing failed
    """

    success: bool
    data: Union[Unset, Any] = UNSET
    workflow_status: Union[Unset, ParseResponseWorkflowStatus] = UNSET
    pages_processed: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    partial_results: Union[Unset, list["ParseResponsePartialResultsItem"]] = UNSET
    execution_time: Union[Unset, int] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = self.data

        workflow_status: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_status, Unset):
            workflow_status = self.workflow_status.value

        pages_processed = self.pages_processed

        total_pages = self.total_pages

        partial_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.partial_results, Unset):
            partial_results = []
            for partial_results_item_data in self.partial_results:
                partial_results_item = partial_results_item_data.to_dict()
                partial_results.append(partial_results_item)

        execution_time = self.execution_time

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if workflow_status is not UNSET:
            field_dict["workflow_status"] = workflow_status
        if pages_processed is not UNSET:
            field_dict["pages_processed"] = pages_processed
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if partial_results is not UNSET:
            field_dict["partial_results"] = partial_results
        if execution_time is not UNSET:
            field_dict["execution_time"] = execution_time
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parse_response_partial_results_item import ParseResponsePartialResultsItem

        d = dict(src_dict)
        success = d.pop("success")

        data = d.pop("data", UNSET)

        _workflow_status = d.pop("workflow_status", UNSET)
        workflow_status: Union[Unset, ParseResponseWorkflowStatus]
        if isinstance(_workflow_status, Unset):
            workflow_status = UNSET
        else:
            workflow_status = ParseResponseWorkflowStatus(_workflow_status)

        pages_processed = d.pop("pages_processed", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        partial_results = []
        _partial_results = d.pop("partial_results", UNSET)
        for partial_results_item_data in _partial_results or []:
            partial_results_item = ParseResponsePartialResultsItem.from_dict(partial_results_item_data)

            partial_results.append(partial_results_item)

        execution_time = d.pop("execution_time", UNSET)

        error = d.pop("error", UNSET)

        parse_response = cls(
            success=success,
            data=data,
            workflow_status=workflow_status,
            pages_processed=pages_processed,
            total_pages=total_pages,
            partial_results=partial_results,
            execution_time=execution_time,
            error=error,
        )

        parse_response.additional_properties = d
        return parse_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
