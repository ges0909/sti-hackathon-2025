from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rss_channel_image import RssChannelImage
    from ..models.rss_channel_item_item import RssChannelItemItem


T = TypeVar("T", bound="RssChannel")


@_attrs_define
class RssChannel:
    """
    Attributes:
        title (Union[Unset, str]):  Example: Aktuelle Bevölkerungsschutz-Warnungen (Städteregion Aachen).
        link (Union[Unset, str]):  Example: https://warnung.bund.de.
        description (Union[Unset, str]):  Example: Aktuell vorliegende Warnmeldungen - MoWaS.
        pub_date (Union[Unset, str]):  Example: Tue, 04 Apr 2023 20:38:30 +0200.
        image (Union[Unset, RssChannelImage]):
        item (Union[Unset, list['RssChannelItemItem']]):
    """

    title: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    pub_date: Union[Unset, str] = UNSET
    image: Union[Unset, "RssChannelImage"] = UNSET
    item: Union[Unset, list["RssChannelItemItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        link = self.link

        description = self.description

        pub_date = self.pub_date

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        item: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.item, Unset):
            item = []
            for item_item_data in self.item:
                item_item = item_item_data.to_dict()
                item.append(item_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if link is not UNSET:
            field_dict["link"] = link
        if description is not UNSET:
            field_dict["description"] = description
        if pub_date is not UNSET:
            field_dict["pubDate"] = pub_date
        if image is not UNSET:
            field_dict["image"] = image
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rss_channel_image import RssChannelImage
        from ..models.rss_channel_item_item import RssChannelItemItem

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        link = d.pop("link", UNSET)

        description = d.pop("description", UNSET)

        pub_date = d.pop("pubDate", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, RssChannelImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = RssChannelImage.from_dict(_image)

        item = []
        _item = d.pop("item", UNSET)
        for item_item_data in _item or []:
            item_item = RssChannelItemItem.from_dict(item_item_data)

            item.append(item_item)

        rss_channel = cls(
            title=title,
            link=link,
            description=description,
            pub_date=pub_date,
            image=image,
            item=item,
        )

        rss_channel.additional_properties = d
        return rss_channel

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
