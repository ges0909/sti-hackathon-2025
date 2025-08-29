import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_overview_result_item_i18n_title import ARSOverviewResultItemI18NTitle
    from ..models.ars_overview_result_item_payload import ARSOverviewResultItemPayload


T = TypeVar("T", bound="ARSOverviewResultItem")


@_attrs_define
class ARSOverviewResultItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: mow.DE-NW-BN-SE030-20201014-30-000.
        payload (Union[Unset, ARSOverviewResultItemPayload]):
        i_18_n_title (Union[Unset, ARSOverviewResultItemI18NTitle]):
        sent (Union[Unset, datetime.datetime]):  Example: 2020-10-14 16:35:21+02:00.
    """

    id: Union[Unset, str] = UNSET
    payload: Union[Unset, "ARSOverviewResultItemPayload"] = UNSET
    i_18_n_title: Union[Unset, "ARSOverviewResultItemI18NTitle"] = UNSET
    sent: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        i_18_n_title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.i_18_n_title, Unset):
            i_18_n_title = self.i_18_n_title.to_dict()

        sent: Union[Unset, str] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if i_18_n_title is not UNSET:
            field_dict["i18nTitle"] = i_18_n_title
        if sent is not UNSET:
            field_dict["sent"] = sent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_overview_result_item_i18n_title import ARSOverviewResultItemI18NTitle
        from ..models.ars_overview_result_item_payload import ARSOverviewResultItemPayload

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ARSOverviewResultItemPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ARSOverviewResultItemPayload.from_dict(_payload)

        _i_18_n_title = d.pop("i18nTitle", UNSET)
        i_18_n_title: Union[Unset, ARSOverviewResultItemI18NTitle]
        if isinstance(_i_18_n_title, Unset):
            i_18_n_title = UNSET
        else:
            i_18_n_title = ARSOverviewResultItemI18NTitle.from_dict(_i_18_n_title)

        _sent = d.pop("sent", UNSET)
        sent: Union[Unset, datetime.datetime]
        if isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = isoparse(_sent)

        ars_overview_result_item = cls(
            id=id,
            payload=payload,
            i_18_n_title=i_18_n_title,
            sent=sent,
        )

        ars_overview_result_item.additional_properties = d
        return ars_overview_result_item

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
