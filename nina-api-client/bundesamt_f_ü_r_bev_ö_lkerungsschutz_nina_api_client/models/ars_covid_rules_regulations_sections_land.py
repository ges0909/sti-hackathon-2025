import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_covid_rules_regulations_sections_land_icon import ARSCovidRulesRegulationsSectionsLANDIcon


T = TypeVar("T", bound="ARSCovidRulesRegulationsSectionsLAND")


@_attrs_define
class ARSCovidRulesRegulationsSectionsLAND:
    """
    Attributes:
        caption (Union[Unset, str]):  Example: Landesverordnung.
        url (Union[Unset, str]):  Example: https://www.stmgp.bayern.de/coronavirus/rechtsgrundlagen.
        valid_from (Union[Unset, datetime.datetime]):  Example: 2021-07-01 00:00:00+02:00.
        valid_until (Union[Unset, datetime.datetime]):  Example: 2021-07-28 23:59:59+02:00.
        icon (Union[Unset, ARSCovidRulesRegulationsSectionsLANDIcon]):
    """

    caption: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    valid_from: Union[Unset, datetime.datetime] = UNSET
    valid_until: Union[Unset, datetime.datetime] = UNSET
    icon: Union[Unset, "ARSCovidRulesRegulationsSectionsLANDIcon"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caption = self.caption

        url = self.url

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_until: Union[Unset, str] = UNSET
        if not isinstance(self.valid_until, Unset):
            valid_until = self.valid_until.isoformat()

        icon: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caption is not UNSET:
            field_dict["caption"] = caption
        if url is not UNSET:
            field_dict["url"] = url
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_covid_rules_regulations_sections_land_icon import ARSCovidRulesRegulationsSectionsLANDIcon

        d = dict(src_dict)
        caption = d.pop("caption", UNSET)

        url = d.pop("url", UNSET)

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: Union[Unset, datetime.datetime]
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        _valid_until = d.pop("validUntil", UNSET)
        valid_until: Union[Unset, datetime.datetime]
        if isinstance(_valid_until, Unset):
            valid_until = UNSET
        else:
            valid_until = isoparse(_valid_until)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, ARSCovidRulesRegulationsSectionsLANDIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = ARSCovidRulesRegulationsSectionsLANDIcon.from_dict(_icon)

        ars_covid_rules_regulations_sections_land = cls(
            caption=caption,
            url=url,
            valid_from=valid_from,
            valid_until=valid_until,
            icon=icon,
        )

        ars_covid_rules_regulations_sections_land.additional_properties = d
        return ars_covid_rules_regulations_sections_land

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
