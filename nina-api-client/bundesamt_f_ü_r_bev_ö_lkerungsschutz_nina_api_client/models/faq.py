from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FAQ")


@_attrs_define
class FAQ:
    r"""
    Attributes:
        question (str):  Example: <p>Wofür steht die Warn-App <abbr title=\"Notfall-Informations- und Nachrichten-
            App\">NINA</abbr>?</p>.
        answer (str):  Example: <p><abbr title=\"Notfall-Informations- und Nachrichten-App\">NINA</abbr> steht für
            Notfall-Informations- und Nachrichten-App.</p>.
        last_modification_date (int): Unix-Zeitstempel der letzten Änderung Example: 1620819849000.
    """

    question: str
    answer: str
    last_modification_date: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        question = self.question

        answer = self.answer

        last_modification_date = self.last_modification_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question": question,
                "answer": answer,
                "lastModificationDate": last_modification_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        question = d.pop("question")

        answer = d.pop("answer")

        last_modification_date = d.pop("lastModificationDate")

        faq = cls(
            question=question,
            answer=answer,
            last_modification_date=last_modification_date,
        )

        faq.additional_properties = d
        return faq

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
