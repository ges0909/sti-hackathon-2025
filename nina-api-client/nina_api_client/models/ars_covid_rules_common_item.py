from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ARSCovidRulesCommonItem")


@_attrs_define
class ARSCovidRulesCommonItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: contact.
        caption (Union[Unset, str]):  Example: Ansprechpartner.
        text (Union[Unset, str]):  Example: <p>Quellen sind jeweils die Landesregierungen bzw. die örtlichen Behörden
            auf Kreisebene oder in den Stadtkreisen. Sollten Sie zu den Verordnungen oder Verfügungen Fragen haben
            informieren Sie sich bitte auf den Webseiten Ihrer jeweiligen Kreis- oder Stadtverwaltung oder wenden Sie sich
            bitte an die entsprechenden Bürgerkontakte.</p>.
    """

    id: Union[Unset, str] = UNSET
    caption: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        caption = self.caption

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if caption is not UNSET:
            field_dict["caption"] = caption
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        caption = d.pop("caption", UNSET)

        text = d.pop("text", UNSET)

        ars_covid_rules_common_item = cls(
            id=id,
            caption=caption,
            text=text,
        )

        ars_covid_rules_common_item.additional_properties = d
        return ars_covid_rules_common_item

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
