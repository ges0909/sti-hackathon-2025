from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notfalltipps_tip import NotfalltippsTip


T = TypeVar("T", bound="NotfalltippsCategory")


@_attrs_define
class NotfalltippsCategory:
    """
    Attributes:
        title (str):  Example: Corona-Grundwissen.
        tips (list['NotfalltippsTip']):
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
        event_codes (Union[Unset, list[str]]): Event Codes, zugehörige Logos können über
            /appdata/gsb/eventCodes/eventCodes.json abgerufen werden.
    """

    title: str
    tips: list["NotfalltippsTip"]
    last_modification_date: int
    event_codes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        tips = []
        for tips_item_data in self.tips:
            tips_item = tips_item_data.to_dict()
            tips.append(tips_item)

        last_modification_date = self.last_modification_date

        event_codes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.event_codes, Unset):
            event_codes = self.event_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "tips": tips,
                "lastModificationDate": last_modification_date,
            }
        )
        if event_codes is not UNSET:
            field_dict["eventCodes"] = event_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notfalltipps_tip import NotfalltippsTip

        d = dict(src_dict)
        title = d.pop("title")

        tips = []
        _tips = d.pop("tips")
        for tips_item_data in _tips:
            tips_item = NotfalltippsTip.from_dict(tips_item_data)

            tips.append(tips_item)

        last_modification_date = d.pop("lastModificationDate")

        event_codes = cast(list[str], d.pop("eventCodes", UNSET))

        notfalltipps_category = cls(
            title=title,
            tips=tips,
            last_modification_date=last_modification_date,
            event_codes=event_codes,
        )

        notfalltipps_category.additional_properties = d
        return notfalltipps_category

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
