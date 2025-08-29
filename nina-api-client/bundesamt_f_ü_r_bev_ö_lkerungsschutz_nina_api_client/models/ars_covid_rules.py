from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_covid_rules_common_item import ARSCovidRulesCommonItem
    from ..models.ars_covid_rules_level import ARSCovidRulesLevel
    from ..models.ars_covid_rules_regulations import ARSCovidRulesRegulations
    from ..models.ars_covid_rules_rules_item import ARSCovidRulesRulesItem


T = TypeVar("T", bound="ARSCovidRules")


@_attrs_define
class ARSCovidRules:
    """
    Attributes:
        key (Union[Unset, str]):  Example: 091620000000.
        level (Union[Unset, ARSCovidRulesLevel]):
        general_info (Union[Unset, str]):  Example: <p><span>GrundsÃ¤tzlich gilt: </span></p><p><span>Abstand + Hygiene
            + Maske im Alltag + Corona-Warn-App + Lüften</span></p><p><span data-stringify-type=paragraph-break/><span>Keine
            Testpflicht + keine AusgangsbeschrÃ¤nkungen + keine KontaktbeschrÃ¤nkungen für Geimpfte und Genesene</span></p>.
        rules (Union[Unset, list['ARSCovidRulesRulesItem']]):
        regulations (Union[Unset, ARSCovidRulesRegulations]):
        common (Union[Unset, list['ARSCovidRulesCommonItem']]):
    """

    key: Union[Unset, str] = UNSET
    level: Union[Unset, "ARSCovidRulesLevel"] = UNSET
    general_info: Union[Unset, str] = UNSET
    rules: Union[Unset, list["ARSCovidRulesRulesItem"]] = UNSET
    regulations: Union[Unset, "ARSCovidRulesRegulations"] = UNSET
    common: Union[Unset, list["ARSCovidRulesCommonItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.to_dict()

        general_info = self.general_info

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        regulations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.regulations, Unset):
            regulations = self.regulations.to_dict()

        common: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.common, Unset):
            common = []
            for common_item_data in self.common:
                common_item = common_item_data.to_dict()
                common.append(common_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if level is not UNSET:
            field_dict["level"] = level
        if general_info is not UNSET:
            field_dict["generalInfo"] = general_info
        if rules is not UNSET:
            field_dict["rules"] = rules
        if regulations is not UNSET:
            field_dict["regulations"] = regulations
        if common is not UNSET:
            field_dict["common"] = common

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_covid_rules_common_item import ARSCovidRulesCommonItem
        from ..models.ars_covid_rules_level import ARSCovidRulesLevel
        from ..models.ars_covid_rules_regulations import ARSCovidRulesRegulations
        from ..models.ars_covid_rules_rules_item import ARSCovidRulesRulesItem

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, ARSCovidRulesLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = ARSCovidRulesLevel.from_dict(_level)

        general_info = d.pop("generalInfo", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = ARSCovidRulesRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        _regulations = d.pop("regulations", UNSET)
        regulations: Union[Unset, ARSCovidRulesRegulations]
        if isinstance(_regulations, Unset):
            regulations = UNSET
        else:
            regulations = ARSCovidRulesRegulations.from_dict(_regulations)

        common = []
        _common = d.pop("common", UNSET)
        for common_item_data in _common or []:
            common_item = ARSCovidRulesCommonItem.from_dict(common_item_data)

            common.append(common_item)

        ars_covid_rules = cls(
            key=key,
            level=level,
            general_info=general_info,
            rules=rules,
            regulations=regulations,
            common=common,
        )

        ars_covid_rules.additional_properties = d
        return ars_covid_rules

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
