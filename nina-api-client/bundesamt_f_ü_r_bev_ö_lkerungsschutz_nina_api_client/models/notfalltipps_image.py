from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NotfalltippsImage")


@_attrs_define
class NotfalltippsImage:
    """
    Attributes:
        src (str):  Example: https://warnung.bund.de/api31/appdata/gsb/notfalltipps/DE/images/0_1_0_src.jpg.
        title (str):  Example: Richtig handeln im Notfall.
        alt (str):  Example: Icon Richtig handeln im Notfall.
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
        hash_ (str):  Example: 2b83ba3d16288caf879640b67774560629b85af74804cec7eb5120faa7eb060a.
    """

    src: str
    title: str
    alt: str
    last_modification_date: int
    hash_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src

        title = self.title

        alt = self.alt

        last_modification_date = self.last_modification_date

        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src": src,
                "title": title,
                "alt": alt,
                "lastModificationDate": last_modification_date,
                "hash": hash_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = d.pop("src")

        title = d.pop("title")

        alt = d.pop("alt")

        last_modification_date = d.pop("lastModificationDate")

        hash_ = d.pop("hash")

        notfalltipps_image = cls(
            src=src,
            title=title,
            alt=alt,
            last_modification_date=last_modification_date,
            hash_=hash_,
        )

        notfalltipps_image.additional_properties = d
        return notfalltipps_image

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
