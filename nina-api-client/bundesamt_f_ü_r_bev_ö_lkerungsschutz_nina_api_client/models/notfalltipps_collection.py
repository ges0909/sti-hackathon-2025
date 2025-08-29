from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notfalltipps_category import NotfalltippsCategory


T = TypeVar("T", bound="NotfalltippsCollection")


@_attrs_define
class NotfalltippsCollection:
    """
    Attributes:
        category (list['NotfalltippsCategory']):
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
    """

    category: list["NotfalltippsCategory"]
    last_modification_date: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = []
        for category_item_data in self.category:
            category_item = category_item_data.to_dict()
            category.append(category_item)

        last_modification_date = self.last_modification_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "lastModificationDate": last_modification_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notfalltipps_category import NotfalltippsCategory

        d = dict(src_dict)
        category = []
        _category = d.pop("category")
        for category_item_data in _category:
            category_item = NotfalltippsCategory.from_dict(category_item_data)

            category.append(category_item)

        last_modification_date = d.pop("lastModificationDate")

        notfalltipps_collection = cls(
            category=category,
            last_modification_date=last_modification_date,
        )

        notfalltipps_collection.additional_properties = d
        return notfalltipps_collection

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
