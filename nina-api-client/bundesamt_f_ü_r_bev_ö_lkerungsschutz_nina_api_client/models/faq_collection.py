from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.faq import FAQ


T = TypeVar("T", bound="FAQCollection")


@_attrs_define
class FAQCollection:
    """
    Attributes:
        faq (list['FAQ']):
        last_modification_date (Union[Unset, int]): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
    """

    faq: list["FAQ"]
    last_modification_date: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        faq = []
        for faq_item_data in self.faq:
            faq_item = faq_item_data.to_dict()
            faq.append(faq_item)

        last_modification_date = self.last_modification_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FAQ": faq,
            }
        )
        if last_modification_date is not UNSET:
            field_dict["lastModificationDate"] = last_modification_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.faq import FAQ

        d = dict(src_dict)
        faq = []
        _faq = d.pop("FAQ")
        for faq_item_data in _faq:
            faq_item = FAQ.from_dict(faq_item_data)

            faq.append(faq_item)

        last_modification_date = d.pop("lastModificationDate", UNSET)

        faq_collection = cls(
            faq=faq,
            last_modification_date=last_modification_date,
        )

        faq_collection.additional_properties = d
        return faq_collection

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
