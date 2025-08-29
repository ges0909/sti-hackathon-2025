from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_covid_rules_regulations_sections_bund import ARSCovidRulesRegulationsSectionsBUND
    from ..models.ars_covid_rules_regulations_sections_kreis import ARSCovidRulesRegulationsSectionsKREIS
    from ..models.ars_covid_rules_regulations_sections_land import ARSCovidRulesRegulationsSectionsLAND


T = TypeVar("T", bound="ARSCovidRulesRegulationsSections")


@_attrs_define
class ARSCovidRulesRegulationsSections:
    """
    Attributes:
        bund (Union[Unset, ARSCovidRulesRegulationsSectionsBUND]):
        land (Union[Unset, ARSCovidRulesRegulationsSectionsLAND]):
        kreis (Union[Unset, ARSCovidRulesRegulationsSectionsKREIS]):
    """

    bund: Union[Unset, "ARSCovidRulesRegulationsSectionsBUND"] = UNSET
    land: Union[Unset, "ARSCovidRulesRegulationsSectionsLAND"] = UNSET
    kreis: Union[Unset, "ARSCovidRulesRegulationsSectionsKREIS"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bund, Unset):
            bund = self.bund.to_dict()

        land: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.land, Unset):
            land = self.land.to_dict()

        kreis: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.kreis, Unset):
            kreis = self.kreis.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bund is not UNSET:
            field_dict["BUND"] = bund
        if land is not UNSET:
            field_dict["LAND"] = land
        if kreis is not UNSET:
            field_dict["KREIS"] = kreis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_covid_rules_regulations_sections_bund import ARSCovidRulesRegulationsSectionsBUND
        from ..models.ars_covid_rules_regulations_sections_kreis import ARSCovidRulesRegulationsSectionsKREIS
        from ..models.ars_covid_rules_regulations_sections_land import ARSCovidRulesRegulationsSectionsLAND

        d = dict(src_dict)
        _bund = d.pop("BUND", UNSET)
        bund: Union[Unset, ARSCovidRulesRegulationsSectionsBUND]
        if isinstance(_bund, Unset):
            bund = UNSET
        else:
            bund = ARSCovidRulesRegulationsSectionsBUND.from_dict(_bund)

        _land = d.pop("LAND", UNSET)
        land: Union[Unset, ARSCovidRulesRegulationsSectionsLAND]
        if isinstance(_land, Unset):
            land = UNSET
        else:
            land = ARSCovidRulesRegulationsSectionsLAND.from_dict(_land)

        _kreis = d.pop("KREIS", UNSET)
        kreis: Union[Unset, ARSCovidRulesRegulationsSectionsKREIS]
        if isinstance(_kreis, Unset):
            kreis = UNSET
        else:
            kreis = ARSCovidRulesRegulationsSectionsKREIS.from_dict(_kreis)

        ars_covid_rules_regulations_sections = cls(
            bund=bund,
            land=land,
            kreis=kreis,
        )

        ars_covid_rules_regulations_sections.additional_properties = d
        return ars_covid_rules_regulations_sections

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
