import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.warning_info_item import WarningInfoItem


T = TypeVar("T", bound="Warning_")


@_attrs_define
class Warning_:
    """
    Attributes:
        identifier (Union[Unset, str]):  Example: kat.1234567890abcdef12345678_public_topics.
        sender (Union[Unset, str]): Sender-ID, passende logos können über /appdata/gsb/logos/logos.json abgerufen werden
            Example: CAP@katwarn.de.
        sent (Union[Unset, datetime.datetime]):  Example: 2021-09-24 13:37:35+02:00.
        status (Union[Unset, str]):  Example: Actual.
        msg_type (Union[Unset, str]):  Example: Alert.
        scope (Union[Unset, str]):  Example: Public.
        code (Union[Unset, list[str]]):  Example: ['DVN:9'].
        incidents (Union[Unset, str]):  Example: 1234567890abcdef12345678.
        info (Union[Unset, list['WarningInfoItem']]):
    """

    identifier: Union[Unset, str] = UNSET
    sender: Union[Unset, str] = UNSET
    sent: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    msg_type: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    code: Union[Unset, list[str]] = UNSET
    incidents: Union[Unset, str] = UNSET
    info: Union[Unset, list["WarningInfoItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        sender = self.sender

        sent: Union[Unset, str] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat()

        status = self.status

        msg_type = self.msg_type

        scope = self.scope

        code: Union[Unset, list[str]] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        incidents = self.incidents

        info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.info, Unset):
            info = []
            for info_item_data in self.info:
                info_item = info_item_data.to_dict()
                info.append(info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sent is not UNSET:
            field_dict["sent"] = sent
        if status is not UNSET:
            field_dict["status"] = status
        if msg_type is not UNSET:
            field_dict["msgType"] = msg_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if code is not UNSET:
            field_dict["code"] = code
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.warning_info_item import WarningInfoItem

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        sender = d.pop("sender", UNSET)

        _sent = d.pop("sent", UNSET)
        sent: Union[Unset, datetime.datetime]
        if isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = isoparse(_sent)

        status = d.pop("status", UNSET)

        msg_type = d.pop("msgType", UNSET)

        scope = d.pop("scope", UNSET)

        code = cast(list[str], d.pop("code", UNSET))

        incidents = d.pop("incidents", UNSET)

        info = []
        _info = d.pop("info", UNSET)
        for info_item_data in _info or []:
            info_item = WarningInfoItem.from_dict(info_item_data)

            info.append(info_item)

        warning = cls(
            identifier=identifier,
            sender=sender,
            sent=sent,
            status=status,
            msg_type=msg_type,
            scope=scope,
            code=code,
            incidents=incidents,
            info=info,
        )

        warning.additional_properties = d
        return warning

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
