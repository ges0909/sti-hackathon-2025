import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CovidTickerEntry")


@_attrs_define
class CovidTickerEntry:
    """
    Attributes:
        id (UUID): Tickermeldungs-ID, details können über /appdata/covid/covidticker/DE/tickermeldungen/{id}.json
            abgerufen werden. Example: 06ad3d65-d9f8-4ace-bb5a-cf2ac599a097.
        last_modification_date (datetime.datetime):  Example: 2021-06-09 10:36:53+02:00.
    """

    id: UUID
    last_modification_date: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        last_modification_date = self.last_modification_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "lastModificationDate": last_modification_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        last_modification_date = isoparse(d.pop("lastModificationDate"))

        covid_ticker_entry = cls(
            id=id,
            last_modification_date=last_modification_date,
        )

        covid_ticker_entry.additional_properties = d
        return covid_ticker_entry

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
