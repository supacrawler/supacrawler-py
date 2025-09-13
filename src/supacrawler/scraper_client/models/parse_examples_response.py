from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parse_examples_response_examples import ParseExamplesResponseExamples


T = TypeVar("T", bound="ParseExamplesResponse")


@_attrs_define
class ParseExamplesResponse:
    """
    Attributes:
        success (bool):
        examples (ParseExamplesResponseExamples): Example output specifications
    """

    success: bool
    examples: "ParseExamplesResponseExamples"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        examples = self.examples.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "examples": examples,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parse_examples_response_examples import ParseExamplesResponseExamples

        d = dict(src_dict)
        success = d.pop("success")

        examples = ParseExamplesResponseExamples.from_dict(d.pop("examples"))

        parse_examples_response = cls(
            success=success,
            examples=examples,
        )

        parse_examples_response.additional_properties = d
        return parse_examples_response

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
