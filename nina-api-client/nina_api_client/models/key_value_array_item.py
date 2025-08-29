from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyValueArrayItem")


@_attrs_define
class KeyValueArrayItem:
    """
    Attributes:
        value_name (Union[Unset, str]):  Example: instructionCode.
        value (Union[Unset, str]):  Example: BBK-ISC-132.
    """

    value_name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_name = self.value_name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_name is not UNSET:
            field_dict["valueName"] = value_name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value_name = d.pop("valueName", UNSET)

        value = d.pop("value", UNSET)

        key_value_array_item = cls(
            value_name=value_name,
            value=value,
        )

        key_value_array_item.additional_properties = d
        return key_value_array_item

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
