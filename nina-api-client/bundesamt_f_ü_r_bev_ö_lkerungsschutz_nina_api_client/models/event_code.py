from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventCode")


@_attrs_define
class EventCode:
    """
    Attributes:
        event_code (str):  Example: BBK-EVC-001.
        image (Union[Unset, str]): Dateiname, relativ zu https://warnung.bund.de/api31/appdata/gsb/eventCodes/ (z.B.:
            https://warnung.bund.de/api31/appdata/gsb/eventCodes/BBK-EVC-001.png). Example: dwd_logo.png.
    """

    event_code: str
    image: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_code = self.event_code

        image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventCode": event_code,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_code = d.pop("eventCode")

        image = d.pop("image", UNSET)

        event_code = cls(
            event_code=event_code,
            image=image,
        )

        event_code.additional_properties = d
        return event_code

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
