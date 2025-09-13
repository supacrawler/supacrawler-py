from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parse_validation_result_format import ParseValidationResultFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParseValidationResult")


@_attrs_define
class ParseValidationResult:
    """
    Attributes:
        is_valid (bool): Whether the response is valid
        format_ (ParseValidationResultFormat): Format of the response
        errors (list[str]): Validation errors
        fields_found (Union[Unset, list[str]]): JSON fields discovered
        row_count (Union[Unset, int]): CSV row count
        column_count (Union[Unset, int]): CSV column count
    """

    is_valid: bool
    format_: ParseValidationResultFormat
    errors: list[str]
    fields_found: Union[Unset, list[str]] = UNSET
    row_count: Union[Unset, int] = UNSET
    column_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        format_ = self.format_.value

        errors = self.errors

        fields_found: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields_found, Unset):
            fields_found = self.fields_found

        row_count = self.row_count

        column_count = self.column_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_valid": is_valid,
                "format": format_,
                "errors": errors,
            }
        )
        if fields_found is not UNSET:
            field_dict["fields_found"] = fields_found
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if column_count is not UNSET:
            field_dict["column_count"] = column_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_valid = d.pop("is_valid")

        format_ = ParseValidationResultFormat(d.pop("format"))

        errors = cast(list[str], d.pop("errors"))

        fields_found = cast(list[str], d.pop("fields_found", UNSET))

        row_count = d.pop("row_count", UNSET)

        column_count = d.pop("column_count", UNSET)

        parse_validation_result = cls(
            is_valid=is_valid,
            format_=format_,
            errors=errors,
            fields_found=fields_found,
            row_count=row_count,
            column_count=column_count,
        )

        parse_validation_result.additional_properties = d
        return parse_validation_result

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
