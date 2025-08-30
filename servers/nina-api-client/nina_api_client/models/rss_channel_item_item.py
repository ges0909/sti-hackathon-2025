from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RssChannelItemItem")


@_attrs_define
class RssChannelItemItem:
    """
    Attributes:
        title (Union[Unset, str]):  Example: Entwarnung: Rauchgase - Eschweiler-Röthgen.
        link (Union[Unset, str]):  Example: https://warnung.bund.de/meldung/mow.DE-NW-AC-
            SE090-20230404-90-001/Entwarnung:_Rauchgase_-_Eschweiler-R%C3%B6thgen.
        pub_date (Union[Unset, str]):  Example: Tue, 04 Apr 2023 20:38:30 +0200.
        guid (Union[Unset, str]):  Example: b2c4bf09f14192dce01f7364c0845b81daf815fca5967f015c880932c1480b56.
        description (Union[Unset, str]):  Example: Dies ist die Entwarnung zur Warnung "Rauchgase - Eschweiler-Röthgen"
            vom 04.04.2023 18:56:51 gesendet durch LS Aachen, Städteregion (DEU, NW, Aachen). (Hier kommen Beschreibung und
            Handlungsanweisungen)
            --- Diese Warnmeldung stammt aus dem Modularen Warnsystem (MoWaS) des Bundesamtes für Bevölkerungsschutz und
            Katastrophenhilfe. Sie darf nur inhaltlich unverändert und nicht zu gewerblichen Zwecken verwendet werden. Um
            die Authentizität der Warnmeldung zu überprüfen gehen Sie auf https://warnung.bund.de. Eine Einschränkung oder
            (zeitweise) Einstellung des RSS-Feeds ist z.B. für technische Wartungen jederzeit und ohne vorherige Ankündigung
            möglich..
    """

    title: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    pub_date: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        link = self.link

        pub_date = self.pub_date

        guid = self.guid

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if link is not UNSET:
            field_dict["link"] = link
        if pub_date is not UNSET:
            field_dict["pubDate"] = pub_date
        if guid is not UNSET:
            field_dict["guid"] = guid
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        link = d.pop("link", UNSET)

        pub_date = d.pop("pubDate", UNSET)

        guid = d.pop("guid", UNSET)

        description = d.pop("description", UNSET)

        rss_channel_item_item = cls(
            title=title,
            link=link,
            pub_date=pub_date,
            guid=guid,
            description=description,
        )

        rss_channel_item_item.additional_properties = d
        return rss_channel_item_item

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
