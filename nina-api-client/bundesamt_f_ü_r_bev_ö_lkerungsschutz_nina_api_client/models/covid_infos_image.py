import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CovidInfosImage")


@_attrs_define
class CovidInfosImage:
    """
    Attributes:
        id (str):  Example: 7b995a3b-cec7-4354-833b-3be57710076e.
        src (str):  Example:
            https://warnung.bund.de/api31/appdata/covid/covidinfos/DE/images/7b995a3b-cec7-4354-833b-3be57710076e.png.
        title (str):  Example: Aktuelle Fallzahlen.
        alt (str):  Example: Aktuelle Fallzahlen.
        source_text (str):  Example: Materna.
        last_modification_date (datetime.datetime):  Example: 2021-06-09 10:36:53+02:00.
        hash_ (str):  Example: 2b83ba3d16288caf879640b67774560629b85af74804cec7eb5120faa7eb060a.
    """

    id: str
    src: str
    title: str
    alt: str
    source_text: str
    last_modification_date: datetime.datetime
    hash_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        src = self.src

        title = self.title

        alt = self.alt

        source_text = self.source_text

        last_modification_date = self.last_modification_date.isoformat()

        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "src": src,
                "title": title,
                "alt": alt,
                "sourceText": source_text,
                "lastModificationDate": last_modification_date,
                "hash": hash_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        src = d.pop("src")

        title = d.pop("title")

        alt = d.pop("alt")

        source_text = d.pop("sourceText")

        last_modification_date = isoparse(d.pop("lastModificationDate"))

        hash_ = d.pop("hash")

        covid_infos_image = cls(
            id=id,
            src=src,
            title=title,
            alt=alt,
            source_text=source_text,
            last_modification_date=last_modification_date,
            hash_=hash_,
        )

        covid_infos_image.additional_properties = d
        return covid_infos_image

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
