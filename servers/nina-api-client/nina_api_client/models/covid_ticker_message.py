import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CovidTickerMessage")


@_attrs_define
class CovidTickerMessage:
    """
    Attributes:
        id (str):  Example: 7eb928fc-4496-4a71-8154-1c64be10ce0a.
        date_of_issue (datetime.datetime):  Example: 2021-06-09 10:36:53+02:00.
        title (str):  Example: Bund-Länder-Beschluss vom 5. Januar: Neue Corona-Maßnahmen gelten ab heute bundesweit.
        body_text (str):  Example: <html><head></head><body><p>Private Zusammenkünfte mit maximal...</p></body></html>.
        teaser_text (str):  Example: <p>Private Zusammenkünfte mit maximal...</p>.
        push (bool):
        last_modification_date (datetime.datetime):  Example: 2021-06-09 10:36:53+02:00.
        version (int):  Example: 2.
    """

    id: str
    date_of_issue: datetime.datetime
    title: str
    body_text: str
    teaser_text: str
    push: bool
    last_modification_date: datetime.datetime
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date_of_issue = self.date_of_issue.isoformat()

        title = self.title

        body_text = self.body_text

        teaser_text = self.teaser_text

        push = self.push

        last_modification_date = self.last_modification_date.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dateOfIssue": date_of_issue,
                "title": title,
                "bodyText": body_text,
                "teaserText": teaser_text,
                "push": push,
                "lastModificationDate": last_modification_date,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        date_of_issue = isoparse(d.pop("dateOfIssue"))

        title = d.pop("title")

        body_text = d.pop("bodyText")

        teaser_text = d.pop("teaserText")

        push = d.pop("push")

        last_modification_date = isoparse(d.pop("lastModificationDate"))

        version = d.pop("version")

        covid_ticker_message = cls(
            id=id,
            date_of_issue=date_of_issue,
            title=title,
            body_text=body_text,
            teaser_text=teaser_text,
            push=push,
            last_modification_date=last_modification_date,
            version=version,
        )

        covid_ticker_message.additional_properties = d
        return covid_ticker_message

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
