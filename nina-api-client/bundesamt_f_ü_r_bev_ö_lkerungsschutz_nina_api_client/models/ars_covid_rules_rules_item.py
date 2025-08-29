from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_covid_rules_rules_item_icon import ARSCovidRulesRulesItemIcon


T = TypeVar("T", bound="ARSCovidRulesRulesItem")


@_attrs_define
class ARSCovidRulesRulesItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: vaccinations.
        caption (Union[Unset, str]):  Example: Impfen.
        text (Union[Unset, str]):  Example: <p><span>Keine Priorisierung bei der Corona-Schutzimpfung in Arztpraxen und
            Impfzentren. NÃ¤here Informationen zur Schutzimpfung gegen das Corona-Virus erhalten Sie über die bundesweite
            Hotline 116117.</span></p><p><span><a class=RichTextExtLink ExternalLink data-gsb-doc-
            origin=36a6263b-25b9-40c2-8b51-8cfc1eb76506 href=https://www.stmgp.bayern.de/coronavirus/impfung/>Hier finden
            Sie Informationen aus Ihrem Bundesland.</a></span></p>.
        source (Union[Unset, str]):  Example: LAND.
        icon (Union[Unset, ARSCovidRulesRulesItemIcon]):
    """

    id: Union[Unset, str] = UNSET
    caption: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    icon: Union[Unset, "ARSCovidRulesRulesItemIcon"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        caption = self.caption

        text = self.text

        source = self.source

        icon: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if caption is not UNSET:
            field_dict["caption"] = caption
        if text is not UNSET:
            field_dict["text"] = text
        if source is not UNSET:
            field_dict["source"] = source
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_covid_rules_rules_item_icon import ARSCovidRulesRulesItemIcon

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        caption = d.pop("caption", UNSET)

        text = d.pop("text", UNSET)

        source = d.pop("source", UNSET)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, ARSCovidRulesRulesItemIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = ARSCovidRulesRulesItemIcon.from_dict(_icon)

        ars_covid_rules_rules_item = cls(
            id=id,
            caption=caption,
            text=text,
            source=source,
            icon=icon,
        )

        ars_covid_rules_rules_item.additional_properties = d
        return ars_covid_rules_rules_item

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
