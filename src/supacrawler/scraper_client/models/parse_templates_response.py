from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parse_templates_response_templates import ParseTemplatesResponseTemplates


T = TypeVar("T", bound="ParseTemplatesResponse")


@_attrs_define
class ParseTemplatesResponse:
    """
    Attributes:
        success (bool):
        templates (ParseTemplatesResponseTemplates): Available templates with descriptions
        content_types (list[str]): Supported content types
        output_formats (list[str]): Supported output formats
    """

    success: bool
    templates: "ParseTemplatesResponseTemplates"
    content_types: list[str]
    output_formats: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        templates = self.templates.to_dict()

        content_types = self.content_types

        output_formats = self.output_formats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "templates": templates,
                "content_types": content_types,
                "output_formats": output_formats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parse_templates_response_templates import ParseTemplatesResponseTemplates

        d = dict(src_dict)
        success = d.pop("success")

        templates = ParseTemplatesResponseTemplates.from_dict(d.pop("templates"))

        content_types = cast(list[str], d.pop("content_types"))

        output_formats = cast(list[str], d.pop("output_formats"))

        parse_templates_response = cls(
            success=success,
            templates=templates,
            content_types=content_types,
            output_formats=output_formats,
        )

        parse_templates_response.additional_properties = d
        return parse_templates_response

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
