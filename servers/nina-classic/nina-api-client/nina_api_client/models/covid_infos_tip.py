from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.covid_infos_article import CovidInfosArticle
    from ..models.covid_infos_image import CovidInfosImage


T = TypeVar("T", bound="CovidInfosTip")


@_attrs_define
class CovidInfosTip:
    """
    Attributes:
        image (CovidInfosImage):
        title (str):  Example: Corona-Grundwissen.
        article (CovidInfosArticle):
    """

    image: "CovidInfosImage"
    title: str
    article: "CovidInfosArticle"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_dict()

        title = self.title

        article = self.article.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "title": title,
                "article": article,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covid_infos_article import CovidInfosArticle
        from ..models.covid_infos_image import CovidInfosImage

        d = dict(src_dict)
        image = CovidInfosImage.from_dict(d.pop("image"))

        title = d.pop("title")

        article = CovidInfosArticle.from_dict(d.pop("article"))

        covid_infos_tip = cls(
            image=image,
            title=title,
            article=article,
        )

        covid_infos_tip.additional_properties = d
        return covid_infos_tip

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
