from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ARSCovidRulesRegulationsSectionsLANDIcon")


@_attrs_define
class ARSCovidRulesRegulationsSectionsLANDIcon:
    """
    Attributes:
        src (Union[Unset, str]):  Example: https://warnung.bund.de/api31/appdata/covid/covidrules/assets/1f65c785497bbdf
            ddcb9de3a39c4b2ed1aee58d41afd4a3f9a62cfb9f2942748.png.
        hash_ (Union[Unset, str]):  Example: 1f65c785497bbdfddcb9de3a39c4b2ed1aee58d41afd4a3f9a62cfb9f2942748.
    """

    src: Union[Unset, str] = UNSET
    hash_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src

        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if src is not UNSET:
            field_dict["src"] = src
        if hash_ is not UNSET:
            field_dict["hash"] = hash_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = d.pop("src", UNSET)

        hash_ = d.pop("hash", UNSET)

        ars_covid_rules_regulations_sections_land_icon = cls(
            src=src,
            hash_=hash_,
        )

        ars_covid_rules_regulations_sections_land_icon.additional_properties = d
        return ars_covid_rules_regulations_sections_land_icon

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
