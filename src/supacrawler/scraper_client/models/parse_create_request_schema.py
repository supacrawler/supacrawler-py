from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ParseCreateRequestSchema")


@_attrs_define
class ParseCreateRequestSchema:
    """Optional JSON schema for structured output

    Example:
        {'type': 'object', 'properties': {'posts': {'type': 'array', 'items': {'type': 'object', 'properties': {'title':
            {'type': 'string'}, 'date': {'type': 'string'}, 'url': {'type': 'string'}}, 'required': ['title', 'date',
            'url']}}}, 'required': ['posts']}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parse_create_request_schema = cls()

        parse_create_request_schema.additional_properties = d
        return parse_create_request_schema

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
