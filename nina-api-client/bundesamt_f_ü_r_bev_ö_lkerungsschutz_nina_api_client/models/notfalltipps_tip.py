from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notfalltipps_article import NotfalltippsArticle


T = TypeVar("T", bound="NotfalltippsTip")


@_attrs_define
class NotfalltippsTip:
    """
    Attributes:
        title (str):  Example: Corona-Grundwissen.
        articles (Union[Unset, list['NotfalltippsArticle']]):
    """

    title: str
    articles: Union[Unset, list["NotfalltippsArticle"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        articles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.articles, Unset):
            articles = []
            for articles_item_data in self.articles:
                articles_item = articles_item_data.to_dict()
                articles.append(articles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if articles is not UNSET:
            field_dict["articles"] = articles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notfalltipps_article import NotfalltippsArticle

        d = dict(src_dict)
        title = d.pop("title")

        articles = []
        _articles = d.pop("articles", UNSET)
        for articles_item_data in _articles or []:
            articles_item = NotfalltippsArticle.from_dict(articles_item_data)

            articles.append(articles_item)

        notfalltipps_tip = cls(
            title=title,
            articles=articles,
        )

        notfalltipps_tip.additional_properties = d
        return notfalltipps_tip

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
