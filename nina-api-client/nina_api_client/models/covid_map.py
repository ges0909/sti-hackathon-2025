from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.covid_map_data import CovidMapData
    from ..models.covid_map_legend import CovidMapLegend


T = TypeVar("T", bound="CovidMap")


@_attrs_define
class CovidMap:
    """Kartendaten für Corona Fallzahlen

    Attributes:
        map_legend (list['CovidMapLegend']):
        map_data (list['CovidMapData']):
    """

    map_legend: list["CovidMapLegend"]
    map_data: list["CovidMapData"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_legend = []
        for map_legend_item_data in self.map_legend:
            map_legend_item = map_legend_item_data.to_dict()
            map_legend.append(map_legend_item)

        map_data = []
        for map_data_item_data in self.map_data:
            map_data_item = map_data_item_data.to_dict()
            map_data.append(map_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mapLegend": map_legend,
                "mapData": map_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covid_map_data import CovidMapData
        from ..models.covid_map_legend import CovidMapLegend

        d = dict(src_dict)
        map_legend = []
        _map_legend = d.pop("mapLegend")
        for map_legend_item_data in _map_legend:
            map_legend_item = CovidMapLegend.from_dict(map_legend_item_data)

            map_legend.append(map_legend_item)

        map_data = []
        _map_data = d.pop("mapData")
        for map_data_item_data in _map_data:
            map_data_item = CovidMapData.from_dict(map_data_item_data)

            map_data.append(map_data_item)

        covid_map = cls(
            map_legend=map_legend,
            map_data=map_data,
        )

        covid_map.additional_properties = d
        return covid_map

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
