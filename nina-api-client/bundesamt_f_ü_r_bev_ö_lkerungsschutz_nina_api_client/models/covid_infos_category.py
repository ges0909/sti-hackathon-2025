import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.covid_infos_image import CovidInfosImage
    from ..models.covid_infos_tip import CovidInfosTip


T = TypeVar("T", bound="CovidInfosCategory")


@_attrs_define
class CovidInfosCategory:
    """
    Attributes:
        title (str):  Example: Corona-Grundwissen.
        tips (list['CovidInfosTip']):
        image (CovidInfosImage):
        last_modification_date (datetime.datetime): Unix-Zeitstempel der letzten Änderung Example: 2021-06-09
            10:36:53+02:00.
    """

    title: str
    tips: list["CovidInfosTip"]
    image: "CovidInfosImage"
    last_modification_date: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        tips = []
        for tips_item_data in self.tips:
            tips_item = tips_item_data.to_dict()
            tips.append(tips_item)

        image = self.image.to_dict()

        last_modification_date = self.last_modification_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "tips": tips,
                "image": image,
                "lastModificationDate": last_modification_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covid_infos_image import CovidInfosImage
        from ..models.covid_infos_tip import CovidInfosTip

        d = dict(src_dict)
        title = d.pop("title")

        tips = []
        _tips = d.pop("tips")
        for tips_item_data in _tips:
            tips_item = CovidInfosTip.from_dict(tips_item_data)

            tips.append(tips_item)

        image = CovidInfosImage.from_dict(d.pop("image"))

        last_modification_date = isoparse(d.pop("lastModificationDate"))

        covid_infos_category = cls(
            title=title,
            tips=tips,
            image=image,
            last_modification_date=last_modification_date,
        )

        covid_infos_category.additional_properties = d
        return covid_infos_category

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
