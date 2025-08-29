import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_warnings_item_i18n_title import MapWarningsItemI18NTitle


T = TypeVar("T", bound="MapWarningsItem")


@_attrs_define
class MapWarningsItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: kat.60e96f0b62aefd198d9c0956_public_topics.
        version (Union[Unset, int]):  Example: 9.
        start_date (Union[Unset, datetime.datetime]):  Example: 2021-07-10 11:57:33+02:00.
        severity (Union[Unset, str]):  Example: Severe.
        type_ (Union[Unset, str]):  Example: Alert.
        i_18_n_title (Union[Unset, MapWarningsItemI18NTitle]):
    """

    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    severity: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    i_18_n_title: Union[Unset, "MapWarningsItemI18NTitle"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version = self.version

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        severity = self.severity

        type_ = self.type_

        i_18_n_title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.i_18_n_title, Unset):
            i_18_n_title = self.i_18_n_title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if severity is not UNSET:
            field_dict["severity"] = severity
        if type_ is not UNSET:
            field_dict["type"] = type_
        if i_18_n_title is not UNSET:
            field_dict["i18nTitle"] = i_18_n_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_warnings_item_i18n_title import MapWarningsItemI18NTitle

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        severity = d.pop("severity", UNSET)

        type_ = d.pop("type", UNSET)

        _i_18_n_title = d.pop("i18nTitle", UNSET)
        i_18_n_title: Union[Unset, MapWarningsItemI18NTitle]
        if isinstance(_i_18_n_title, Unset):
            i_18_n_title = UNSET
        else:
            i_18_n_title = MapWarningsItemI18NTitle.from_dict(_i_18_n_title)

        map_warnings_item = cls(
            id=id,
            version=version,
            start_date=start_date,
            severity=severity,
            type_=type_,
            i_18_n_title=i_18_n_title,
        )

        map_warnings_item.additional_properties = d
        return map_warnings_item

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
