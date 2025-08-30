from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_covid_rules_regulations_sections import ARSCovidRulesRegulationsSections


T = TypeVar("T", bound="ARSCovidRulesRegulations")


@_attrs_define
class ARSCovidRulesRegulations:
    """
    Attributes:
        valid_from_until (Union[Unset, str]):  Example: Gültig von $validFrom bis $validUntil.
        sections (Union[Unset, ARSCovidRulesRegulationsSections]):
    """

    valid_from_until: Union[Unset, str] = UNSET
    sections: Union[Unset, "ARSCovidRulesRegulationsSections"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid_from_until = self.valid_from_until

        sections: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid_from_until is not UNSET:
            field_dict["validFromUntil"] = valid_from_until
        if sections is not UNSET:
            field_dict["sections"] = sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_covid_rules_regulations_sections import ARSCovidRulesRegulationsSections

        d = dict(src_dict)
        valid_from_until = d.pop("validFromUntil", UNSET)

        _sections = d.pop("sections", UNSET)
        sections: Union[Unset, ARSCovidRulesRegulationsSections]
        if isinstance(_sections, Unset):
            sections = UNSET
        else:
            sections = ARSCovidRulesRegulationsSections.from_dict(_sections)

        ars_covid_rules_regulations = cls(
            valid_from_until=valid_from_until,
            sections=sections,
        )

        ars_covid_rules_regulations.additional_properties = d
        return ars_covid_rules_regulations

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
