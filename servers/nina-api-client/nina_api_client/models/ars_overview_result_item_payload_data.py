from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_overview_result_item_payload_data_area import ARSOverviewResultItemPayloadDataArea
    from ..models.ars_overview_result_item_payload_data_trans_keys import ARSOverviewResultItemPayloadDataTransKeys


T = TypeVar("T", bound="ARSOverviewResultItemPayloadData")


@_attrs_define
class ARSOverviewResultItemPayloadData:
    """
    Attributes:
        headline (Union[Unset, str]):  Example: Coronavirus; Informationen des Bundesministeriums für  Gesundheit.
        provider (Union[Unset, str]):  Example: MOWAS.
        severity (Union[Unset, str]):  Example: Minor.
        msg_type (Union[Unset, str]):  Example: Update.
        trans_keys (Union[Unset, ARSOverviewResultItemPayloadDataTransKeys]):
        area (Union[Unset, ARSOverviewResultItemPayloadDataArea]):
    """

    headline: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    msg_type: Union[Unset, str] = UNSET
    trans_keys: Union[Unset, "ARSOverviewResultItemPayloadDataTransKeys"] = UNSET
    area: Union[Unset, "ARSOverviewResultItemPayloadDataArea"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headline = self.headline

        provider = self.provider

        severity = self.severity

        msg_type = self.msg_type

        trans_keys: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trans_keys, Unset):
            trans_keys = self.trans_keys.to_dict()

        area: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headline is not UNSET:
            field_dict["headline"] = headline
        if provider is not UNSET:
            field_dict["provider"] = provider
        if severity is not UNSET:
            field_dict["severity"] = severity
        if msg_type is not UNSET:
            field_dict["msgType"] = msg_type
        if trans_keys is not UNSET:
            field_dict["transKeys"] = trans_keys
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_overview_result_item_payload_data_area import ARSOverviewResultItemPayloadDataArea
        from ..models.ars_overview_result_item_payload_data_trans_keys import ARSOverviewResultItemPayloadDataTransKeys

        d = dict(src_dict)
        headline = d.pop("headline", UNSET)

        provider = d.pop("provider", UNSET)

        severity = d.pop("severity", UNSET)

        msg_type = d.pop("msgType", UNSET)

        _trans_keys = d.pop("transKeys", UNSET)
        trans_keys: Union[Unset, ARSOverviewResultItemPayloadDataTransKeys]
        if isinstance(_trans_keys, Unset):
            trans_keys = UNSET
        else:
            trans_keys = ARSOverviewResultItemPayloadDataTransKeys.from_dict(_trans_keys)

        _area = d.pop("area", UNSET)
        area: Union[Unset, ARSOverviewResultItemPayloadDataArea]
        if isinstance(_area, Unset):
            area = UNSET
        else:
            area = ARSOverviewResultItemPayloadDataArea.from_dict(_area)

        ars_overview_result_item_payload_data = cls(
            headline=headline,
            provider=provider,
            severity=severity,
            msg_type=msg_type,
            trans_keys=trans_keys,
            area=area,
        )

        ars_overview_result_item_payload_data.additional_properties = d
        return ars_overview_result_item_payload_data

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
