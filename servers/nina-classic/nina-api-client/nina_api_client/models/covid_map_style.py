from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CovidMapStyle")


@_attrs_define
class CovidMapStyle:
    """
    Attributes:
        stroke_opacity (float):  Example: 1.
        stroke_weight (int):  Example: 1.
        stroke_color (str):  Example: #474747.
        fill_opacity (float):  Example: 0.5.
        fill_color (str):  Example: #04BB0A.
    """

    stroke_opacity: float
    stroke_weight: int
    stroke_color: str
    fill_opacity: float
    fill_color: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stroke_opacity = self.stroke_opacity

        stroke_weight = self.stroke_weight

        stroke_color = self.stroke_color

        fill_opacity = self.fill_opacity

        fill_color = self.fill_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strokeOpacity": stroke_opacity,
                "strokeWeight": stroke_weight,
                "strokeColor": stroke_color,
                "fillOpacity": fill_opacity,
                "fillColor": fill_color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stroke_opacity = d.pop("strokeOpacity")

        stroke_weight = d.pop("strokeWeight")

        stroke_color = d.pop("strokeColor")

        fill_opacity = d.pop("fillOpacity")

        fill_color = d.pop("fillColor")

        covid_map_style = cls(
            stroke_opacity=stroke_opacity,
            stroke_weight=stroke_weight,
            stroke_color=stroke_color,
            fill_opacity=fill_opacity,
            fill_color=fill_color,
        )

        covid_map_style.additional_properties = d
        return covid_map_style

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
