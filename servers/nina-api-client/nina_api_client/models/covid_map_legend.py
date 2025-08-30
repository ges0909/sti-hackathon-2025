from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.covid_map_style import CovidMapStyle


T = TypeVar("T", bound="CovidMapLegend")


@_attrs_define
class CovidMapLegend:
    """
    Attributes:
        label (str):  Example: keine Fälle übermittelt.
        properties (CovidMapStyle):
    """

    label: str
    properties: "CovidMapStyle"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covid_map_style import CovidMapStyle

        d = dict(src_dict)
        label = d.pop("label")

        properties = CovidMapStyle.from_dict(d.pop("properties"))

        covid_map_legend = cls(
            label=label,
            properties=properties,
        )

        covid_map_legend.additional_properties = d
        return covid_map_legend

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
