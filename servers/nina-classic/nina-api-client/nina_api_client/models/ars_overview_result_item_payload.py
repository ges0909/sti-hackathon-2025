from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ars_overview_result_item_payload_data import ARSOverviewResultItemPayloadData


T = TypeVar("T", bound="ARSOverviewResultItemPayload")


@_attrs_define
class ARSOverviewResultItemPayload:
    """
    Attributes:
        version (Union[Unset, int]):  Example: 2.
        type_ (Union[Unset, str]):  Example: ALERT.
        id (Union[Unset, str]):  Example: mow.DE-NW-BN-SE030-20201014-30-000.
        hash_ (Union[Unset, str]):  Example: d72526da941f98cb79f25dc3f9b56474a313e2161fda46e91f146139811eca4a.
        data (Union[Unset, ARSOverviewResultItemPayloadData]):
    """

    version: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    hash_: Union[Unset, str] = UNSET
    data: Union[Unset, "ARSOverviewResultItemPayloadData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        type_ = self.type_

        id = self.id

        hash_ = self.hash_

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ars_overview_result_item_payload_data import ARSOverviewResultItemPayloadData

        d = dict(src_dict)
        version = d.pop("version", UNSET)

        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        hash_ = d.pop("hash", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ARSOverviewResultItemPayloadData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ARSOverviewResultItemPayloadData.from_dict(_data)

        ars_overview_result_item_payload = cls(
            version=version,
            type_=type_,
            id=id,
            hash_=hash_,
            data=data,
        )

        ars_overview_result_item_payload.additional_properties = d
        return ars_overview_result_item_payload

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
