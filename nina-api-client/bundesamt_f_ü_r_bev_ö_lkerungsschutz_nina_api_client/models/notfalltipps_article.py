from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notfalltipps_image import NotfalltippsImage


T = TypeVar("T", bound="NotfalltippsArticle")


@_attrs_define
class NotfalltippsArticle:
    """
    Attributes:
        title (str):  Example: Allgemeine Hinweise.
        body_text (str):  Example: <p>In NotfÃ¤llen und größâ€¦tastrophenhilfe</a>.</p>.
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
        image (Union[Unset, NotfalltippsImage]):
    """

    title: str
    body_text: str
    last_modification_date: int
    image: Union[Unset, "NotfalltippsImage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body_text = self.body_text

        last_modification_date = self.last_modification_date

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "bodyText": body_text,
                "lastModificationDate": last_modification_date,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notfalltipps_image import NotfalltippsImage

        d = dict(src_dict)
        title = d.pop("title")

        body_text = d.pop("bodyText")

        last_modification_date = d.pop("lastModificationDate")

        _image = d.pop("image", UNSET)
        image: Union[Unset, NotfalltippsImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = NotfalltippsImage.from_dict(_image)

        notfalltipps_article = cls(
            title=title,
            body_text=body_text,
            last_modification_date=last_modification_date,
            image=image,
        )

        notfalltipps_article.additional_properties = d
        return notfalltipps_article

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
