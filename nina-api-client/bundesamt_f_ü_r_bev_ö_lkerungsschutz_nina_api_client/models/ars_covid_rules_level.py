from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ARSCovidRulesLevel")


@_attrs_define
class ARSCovidRulesLevel:
    """
    Attributes:
        headline (Union[Unset, str]):  Example: Infektionsgefahr Stufe 2.
        range_ (Union[Unset, str]):  Example: Sieben-Tage-Inzidenz Kreis: 204 Sieben-Tage-Inzidenz Bundesland: 109.
        background_color (Union[Unset, str]):  Example: #FFF280.
        text_color (Union[Unset, str]):  Example: #000000.
    """

    headline: Union[Unset, str] = UNSET
    range_: Union[Unset, str] = UNSET
    background_color: Union[Unset, str] = UNSET
    text_color: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headline = self.headline

        range_ = self.range_

        background_color = self.background_color

        text_color = self.text_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headline is not UNSET:
            field_dict["headline"] = headline
        if range_ is not UNSET:
            field_dict["range"] = range_
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if text_color is not UNSET:
            field_dict["textColor"] = text_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        headline = d.pop("headline", UNSET)

        range_ = d.pop("range", UNSET)

        background_color = d.pop("backgroundColor", UNSET)

        text_color = d.pop("textColor", UNSET)

        ars_covid_rules_level = cls(
            headline=headline,
            range_=range_,
            background_color=background_color,
            text_color=text_color,
        )

        ars_covid_rules_level.additional_properties = d
        return ars_covid_rules_level

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
