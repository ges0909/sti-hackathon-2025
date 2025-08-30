import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CovidInfosArticle")


@_attrs_define
class CovidInfosArticle:
    """
    Attributes:
        title (str):  Example: COVID-19: Die aktuellen Fallzahlen für Deutschland.
        body_text (str):  Example: <html><head></head><body><p>Das <strong>Robert-Koch-Institut (RKI)</strong> bereitet
            ...</p></body></html>.
        date_of_issue (datetime.datetime):  Example: 2021-06-09 10:36:53+02:00.
        last_modification_date (datetime.datetime):  Example: 2021-06-09 10:36:53+02:00.
        function (Union[Unset, str]):  Example: KARTE.
    """

    title: str
    body_text: str
    date_of_issue: datetime.datetime
    last_modification_date: datetime.datetime
    function: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body_text = self.body_text

        date_of_issue = self.date_of_issue.isoformat()

        last_modification_date = self.last_modification_date.isoformat()

        function = self.function

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "bodyText": body_text,
                "dateOfIssue": date_of_issue,
                "lastModificationDate": last_modification_date,
            }
        )
        if function is not UNSET:
            field_dict["function"] = function

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        body_text = d.pop("bodyText")

        date_of_issue = isoparse(d.pop("dateOfIssue"))

        last_modification_date = isoparse(d.pop("lastModificationDate"))

        function = d.pop("function", UNSET)

        covid_infos_article = cls(
            title=title,
            body_text=body_text,
            date_of_issue=date_of_issue,
            last_modification_date=last_modification_date,
            function=function,
        )

        covid_infos_article.additional_properties = d
        return covid_infos_article

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
