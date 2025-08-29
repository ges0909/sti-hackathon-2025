import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value_array_item import KeyValueArrayItem
    from ..models.warning_info_item_area_item import WarningInfoItemAreaItem


T = TypeVar("T", bound="WarningInfoItem")


@_attrs_define
class WarningInfoItem:
    """
    Attributes:
        category (Union[Unset, list[str]]):  Example: ['Other'].
        event (Union[Unset, str]):  Example: Sonderfall.
        urgency (Union[Unset, str]):  Example: Unknown.
        severity (Union[Unset, str]):  Example: Severe.
        certainty (Union[Unset, str]):  Example: Unknown.
        event_code (Union[Unset, list['KeyValueArrayItem']]):
        effective (Union[Unset, datetime.datetime]):  Example: 2021-09-24 13:38:00+02:00.
        sender_name (Union[Unset, str]):  Example: Feuerwehrleitstelle Musterstadt.
        headline (Union[Unset, str]):  Example: Feuerwehrleitstelle Musterstadt meldet: Warnung Sonderfall.  Gültig ab
            01.09.2021, 11:11..
        description (Union[Unset, str]):  Example: Es ist etwas passiert<br/>Belastung durch Beispiele
            Nachgewiesen<br/>Weitere informationen über....
        web (Union[Unset, str]):  Example: https://bund.dev.
        parameter (Union[Unset, list['KeyValueArrayItem']]):
        area (Union[Unset, list['WarningInfoItemAreaItem']]):
    """

    category: Union[Unset, list[str]] = UNSET
    event: Union[Unset, str] = UNSET
    urgency: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    certainty: Union[Unset, str] = UNSET
    event_code: Union[Unset, list["KeyValueArrayItem"]] = UNSET
    effective: Union[Unset, datetime.datetime] = UNSET
    sender_name: Union[Unset, str] = UNSET
    headline: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    web: Union[Unset, str] = UNSET
    parameter: Union[Unset, list["KeyValueArrayItem"]] = UNSET
    area: Union[Unset, list["WarningInfoItemAreaItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, list[str]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        event = self.event

        urgency = self.urgency

        severity = self.severity

        certainty = self.certainty

        event_code: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_code, Unset):
            event_code = []
            for componentsschemas_key_value_array_item_data in self.event_code:
                componentsschemas_key_value_array_item = componentsschemas_key_value_array_item_data.to_dict()
                event_code.append(componentsschemas_key_value_array_item)

        effective: Union[Unset, str] = UNSET
        if not isinstance(self.effective, Unset):
            effective = self.effective.isoformat()

        sender_name = self.sender_name

        headline = self.headline

        description = self.description

        web = self.web

        parameter: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parameter, Unset):
            parameter = []
            for componentsschemas_key_value_array_item_data in self.parameter:
                componentsschemas_key_value_array_item = componentsschemas_key_value_array_item_data.to_dict()
                parameter.append(componentsschemas_key_value_array_item)

        area: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.area, Unset):
            area = []
            for area_item_data in self.area:
                area_item = area_item_data.to_dict()
                area.append(area_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if event is not UNSET:
            field_dict["event"] = event
        if urgency is not UNSET:
            field_dict["urgency"] = urgency
        if severity is not UNSET:
            field_dict["severity"] = severity
        if certainty is not UNSET:
            field_dict["certainty"] = certainty
        if event_code is not UNSET:
            field_dict["eventCode"] = event_code
        if effective is not UNSET:
            field_dict["effective"] = effective
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description
        if web is not UNSET:
            field_dict["web"] = web
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_value_array_item import KeyValueArrayItem
        from ..models.warning_info_item_area_item import WarningInfoItemAreaItem

        d = dict(src_dict)
        category = cast(list[str], d.pop("category", UNSET))

        event = d.pop("event", UNSET)

        urgency = d.pop("urgency", UNSET)

        severity = d.pop("severity", UNSET)

        certainty = d.pop("certainty", UNSET)

        event_code = []
        _event_code = d.pop("eventCode", UNSET)
        for componentsschemas_key_value_array_item_data in _event_code or []:
            componentsschemas_key_value_array_item = KeyValueArrayItem.from_dict(
                componentsschemas_key_value_array_item_data
            )

            event_code.append(componentsschemas_key_value_array_item)

        _effective = d.pop("effective", UNSET)
        effective: Union[Unset, datetime.datetime]
        if isinstance(_effective, Unset):
            effective = UNSET
        else:
            effective = isoparse(_effective)

        sender_name = d.pop("senderName", UNSET)

        headline = d.pop("headline", UNSET)

        description = d.pop("description", UNSET)

        web = d.pop("web", UNSET)

        parameter = []
        _parameter = d.pop("parameter", UNSET)
        for componentsschemas_key_value_array_item_data in _parameter or []:
            componentsschemas_key_value_array_item = KeyValueArrayItem.from_dict(
                componentsschemas_key_value_array_item_data
            )

            parameter.append(componentsschemas_key_value_array_item)

        area = []
        _area = d.pop("area", UNSET)
        for area_item_data in _area or []:
            area_item = WarningInfoItemAreaItem.from_dict(area_item_data)

            area.append(area_item)

        warning_info_item = cls(
            category=category,
            event=event,
            urgency=urgency,
            severity=severity,
            certainty=certainty,
            event_code=event_code,
            effective=effective,
            sender_name=sender_name,
            headline=headline,
            description=description,
            web=web,
            parameter=parameter,
            area=area,
        )

        warning_info_item.additional_properties = d
        return warning_info_item

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
