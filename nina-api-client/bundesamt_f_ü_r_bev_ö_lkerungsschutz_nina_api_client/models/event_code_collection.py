from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_code import EventCode


T = TypeVar("T", bound="EventCodeCollection")


@_attrs_define
class EventCodeCollection:
    """
    Attributes:
        event_codes (list['EventCode']):
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
    """

    event_codes: list["EventCode"]
    last_modification_date: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_codes = []
        for event_codes_item_data in self.event_codes:
            event_codes_item = event_codes_item_data.to_dict()
            event_codes.append(event_codes_item)

        last_modification_date = self.last_modification_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventCodes": event_codes,
                "lastModificationDate": last_modification_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_code import EventCode

        d = dict(src_dict)
        event_codes = []
        _event_codes = d.pop("eventCodes")
        for event_codes_item_data in _event_codes:
            event_codes_item = EventCode.from_dict(event_codes_item_data)

            event_codes.append(event_codes_item)

        last_modification_date = d.pop("lastModificationDate")

        event_code_collection = cls(
            event_codes=event_codes,
            last_modification_date=last_modification_date,
        )

        event_code_collection.additional_properties = d
        return event_code_collection

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
