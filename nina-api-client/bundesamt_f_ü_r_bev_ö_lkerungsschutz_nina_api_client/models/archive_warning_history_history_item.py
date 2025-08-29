import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveWarningHistoryHistoryItem")


@_attrs_define
class ArchiveWarningHistoryHistoryItem:
    """
    Attributes:
        identifier (Union[Unset, str]):  Example: mow.DE-NI-OL-W015-20230121-001_20230121112659.json.
        msg_type (Union[Unset, str]):  Example: ALERT.
        sent (Union[Unset, datetime.datetime]):  Example: 2023-01-21 11:26:59+01:00.
        headline (Union[Unset, str]):  Example: Rauchentwicklung und Geruchsbelästigung nach Großbrand - Westerstede,
            Halsbek.
    """

    identifier: Union[Unset, str] = UNSET
    msg_type: Union[Unset, str] = UNSET
    sent: Union[Unset, datetime.datetime] = UNSET
    headline: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        msg_type = self.msg_type

        sent: Union[Unset, str] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat()

        headline = self.headline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if msg_type is not UNSET:
            field_dict["msgType"] = msg_type
        if sent is not UNSET:
            field_dict["sent"] = sent
        if headline is not UNSET:
            field_dict["headline"] = headline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        msg_type = d.pop("msgType", UNSET)

        _sent = d.pop("sent", UNSET)
        sent: Union[Unset, datetime.datetime]
        if isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = isoparse(_sent)

        headline = d.pop("headline", UNSET)

        archive_warning_history_history_item = cls(
            identifier=identifier,
            msg_type=msg_type,
            sent=sent,
            headline=headline,
        )

        archive_warning_history_history_item.additional_properties = d
        return archive_warning_history_history_item

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
