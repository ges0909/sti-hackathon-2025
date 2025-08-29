from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ARSOverviewResultItemPayloadDataTransKeys")


@_attrs_define
class ARSOverviewResultItemPayloadDataTransKeys:
    """
    Attributes:
        event (Union[Unset, str]): Event Code, zugehörige Logos können über /appdata/gsb/eventCodes/eventCodes.json
            abgerufen werden. Example: BBK-EVC-040.
    """

    event: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event", UNSET)

        ars_overview_result_item_payload_data_trans_keys = cls(
            event=event,
        )

        ars_overview_result_item_payload_data_trans_keys.additional_properties = d
        return ars_overview_result_item_payload_data_trans_keys

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
