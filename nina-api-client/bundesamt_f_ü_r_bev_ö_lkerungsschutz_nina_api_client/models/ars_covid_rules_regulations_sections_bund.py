from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_covid_rules_regulations_sections_bund_icon import ARSCovidRulesRegulationsSectionsBUNDIcon


T = TypeVar("T", bound="ARSCovidRulesRegulationsSectionsBUND")


@_attrs_define
class ARSCovidRulesRegulationsSectionsBUND:
    """
    Attributes:
        caption (Union[Unset, str]):  Example: Bundesverordnung.
        url (Union[Unset, str]):  Example: https://www.bundesregierung.de/breg-de/themen/coronavirus/.
        icon (Union[Unset, ARSCovidRulesRegulationsSectionsBUNDIcon]):
    """

    caption: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    icon: Union[Unset, "ARSCovidRulesRegulationsSectionsBUNDIcon"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caption = self.caption

        url = self.url

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
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_covid_rules_regulations_sections_bund_icon import ARSCovidRulesRegulationsSectionsBUNDIcon

        d = dict(src_dict)
        caption = d.pop("caption", UNSET)

        url = d.pop("url", UNSET)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, ARSCovidRulesRegulationsSectionsBUNDIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = ARSCovidRulesRegulationsSectionsBUNDIcon.from_dict(_icon)

        ars_covid_rules_regulations_sections_bund = cls(
            caption=caption,
            url=url,
            icon=icon,
        )

        ars_covid_rules_regulations_sections_bund.additional_properties = d
        return ars_covid_rules_regulations_sections_bund

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
