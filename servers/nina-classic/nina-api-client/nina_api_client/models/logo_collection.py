from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.logo import Logo


T = TypeVar("T", bound="LogoCollection")


@_attrs_define
class LogoCollection:
    """
    Attributes:
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
        logos (list['Logo']):
    """

    last_modification_date: int
    logos: list["Logo"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modification_date = self.last_modification_date

        logos = []
        for logos_item_data in self.logos:
            logos_item = logos_item_data.to_dict()
            logos.append(logos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastModificationDate": last_modification_date,
                "logos": logos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logo import Logo

        d = dict(src_dict)
        last_modification_date = d.pop("lastModificationDate")

        logos = []
        _logos = d.pop("logos")
        for logos_item_data in _logos:
            logos_item = Logo.from_dict(logos_item_data)

            logos.append(logos_item)

        logo_collection = cls(
            last_modification_date=last_modification_date,
            logos=logos,
        )

        logo_collection.additional_properties = d
        return logo_collection

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
