import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.covid_infos_category import CovidInfosCategory


T = TypeVar("T", bound="CovidInfos")


@_attrs_define
class CovidInfos:
    """Allgemeine Informationen zu Corona

    Attributes:
        last_modification_date (datetime.datetime): Unix-Zeitstempel der letzten Änderung Example: 2021-06-09
            10:36:53+02:00.
        categories (list['CovidInfosCategory']):
    """

    last_modification_date: datetime.datetime
    categories: list["CovidInfosCategory"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modification_date = self.last_modification_date.isoformat()

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastModificationDate": last_modification_date,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covid_infos_category import CovidInfosCategory

        d = dict(src_dict)
        last_modification_date = isoparse(d.pop("lastModificationDate"))

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = CovidInfosCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        covid_infos = cls(
            last_modification_date=last_modification_date,
            categories=categories,
        )

        covid_infos.additional_properties = d
        return covid_infos

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
