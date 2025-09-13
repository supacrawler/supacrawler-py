from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parse_create_request_output_format import ParseCreateRequestOutputFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parse_create_request_schema import ParseCreateRequestSchema


T = TypeVar("T", bound="ParseCreateRequest")


@_attrs_define
class ParseCreateRequest:
    """
    Attributes:
        prompt (str): Natural language prompt that may include URLs and extraction instructions Example: Crawl
            https://example.com/blog and give me the 5 most recent posts in CSV..
        schema (Union[Unset, ParseCreateRequestSchema]): Optional JSON schema for structured output Example: {'type':
            'object', 'properties': {'posts': {'type': 'array', 'items': {'type': 'object', 'properties': {'title': {'type':
            'string'}, 'date': {'type': 'string'}, 'url': {'type': 'string'}}, 'required': ['title', 'date', 'url']}}},
            'required': ['posts']}.
        output_format (Union[Unset, ParseCreateRequestOutputFormat]): Preferred output format Default:
            ParseCreateRequestOutputFormat.JSON.
        stream (Union[Unset, bool]): Enable streaming responses for real-time results Default: False.
        max_depth (Union[Unset, int]): Maximum crawl depth (if crawling is needed) Default: 1.
        max_pages (Union[Unset, int]): Maximum pages to process Default: 10.
    """

    prompt: str
    schema: Union[Unset, "ParseCreateRequestSchema"] = UNSET
    output_format: Union[Unset, ParseCreateRequestOutputFormat] = ParseCreateRequestOutputFormat.JSON
    stream: Union[Unset, bool] = False
    max_depth: Union[Unset, int] = 1
    max_pages: Union[Unset, int] = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        output_format: Union[Unset, str] = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value

        stream = self.stream

        max_depth = self.max_depth

        max_pages = self.max_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if stream is not UNSET:
            field_dict["stream"] = stream
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth
        if max_pages is not UNSET:
            field_dict["max_pages"] = max_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parse_create_request_schema import ParseCreateRequestSchema

        d = dict(src_dict)
        prompt = d.pop("prompt")

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, ParseCreateRequestSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = ParseCreateRequestSchema.from_dict(_schema)

        _output_format = d.pop("output_format", UNSET)
        output_format: Union[Unset, ParseCreateRequestOutputFormat]
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = ParseCreateRequestOutputFormat(_output_format)

        stream = d.pop("stream", UNSET)

        max_depth = d.pop("max_depth", UNSET)

        max_pages = d.pop("max_pages", UNSET)

        parse_create_request = cls(
            prompt=prompt,
            schema=schema,
            output_format=output_format,
            stream=stream,
            max_depth=max_depth,
            max_pages=max_pages,
        )

        parse_create_request.additional_properties = d
        return parse_create_request

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
