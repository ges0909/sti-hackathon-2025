from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RssChannelImage")


@_attrs_define
class RssChannelImage:
    """
    Attributes:
        title (Union[Unset, str]):  Example: Aktuelle Bevölkerungsschutz-Warnungen (StÃ¤dteregion Aachen).
        link (Union[Unset, str]):  Example: https://warnung.bund.de.
        url (Union[Unset, str]):  Example: https://warnung.bund.de/assets/images/icons/ic_mowa.png.
    """

    title: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        link = self.link

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if link is not UNSET:
            field_dict["link"] = link
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        link = d.pop("link", UNSET)

        url = d.pop("url", UNSET)

        rss_channel_image = cls(
            title=title,
            link=link,
            url=url,
        )

        rss_channel_image.additional_properties = d
        return rss_channel_image

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
