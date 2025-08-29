from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value_array_item import KeyValueArrayItem


T = TypeVar("T", bound="WarningInfoItemAreaItem")


@_attrs_define
class WarningInfoItemAreaItem:
    """
    Attributes:
        area_desc (Union[Unset, str]):  Example: Musterstadt.
        geocode (Union[Unset, list['KeyValueArrayItem']]):
    """

    area_desc: Union[Unset, str] = UNSET
    geocode: Union[Unset, list["KeyValueArrayItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area_desc = self.area_desc

        geocode: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.geocode, Unset):
            geocode = []
            for componentsschemas_key_value_array_item_data in self.geocode:
                componentsschemas_key_value_array_item = componentsschemas_key_value_array_item_data.to_dict()
                geocode.append(componentsschemas_key_value_array_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area_desc is not UNSET:
            field_dict["areaDesc"] = area_desc
        if geocode is not UNSET:
            field_dict["geocode"] = geocode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_value_array_item import KeyValueArrayItem

        d = dict(src_dict)
        area_desc = d.pop("areaDesc", UNSET)

        geocode = []
        _geocode = d.pop("geocode", UNSET)
        for componentsschemas_key_value_array_item_data in _geocode or []:
            componentsschemas_key_value_array_item = KeyValueArrayItem.from_dict(
                componentsschemas_key_value_array_item_data
            )

            geocode.append(componentsschemas_key_value_array_item)

        warning_info_item_area_item = cls(
            area_desc=area_desc,
            geocode=geocode,
        )

        warning_info_item_area_item.additional_properties = d
        return warning_info_item_area_item

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
