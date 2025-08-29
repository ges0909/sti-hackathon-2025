from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Logo")


@_attrs_define
class Logo:
    """
    Attributes:
        sender_id (str):  Example: opendata@dwd.de.
        name (str):  Example: Deutscher Wetterdienst.
        orientation (str): Orientierung des Logos, 0 oder 1 Example: 1.
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
        image (Union[Unset, str]): Dateiname, relativ zu https://warnung.bund.de/api31/appdata/gsb/logos/ (z.B.:
            https://warnung.bund.de/api31/appdata/gsb/logos/dwd_logo.png). Bei machen Logos nicht definiert. Example:
            dwd_logo.png.
    """

    sender_id: str
    name: str
    orientation: str
    last_modification_date: int
    image: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_id = self.sender_id

        name = self.name

        orientation = self.orientation

        last_modification_date = self.last_modification_date

        image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "senderId": sender_id,
                "name": name,
                "orientation": orientation,
                "lastModificationDate": last_modification_date,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_id = d.pop("senderId")

        name = d.pop("name")

        orientation = d.pop("orientation")

        last_modification_date = d.pop("lastModificationDate")

        image = d.pop("image", UNSET)

        logo = cls(
            sender_id=sender_id,
            name=name,
            orientation=orientation,
            last_modification_date=last_modification_date,
            image=image,
        )

        logo.additional_properties = d
        return logo

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
