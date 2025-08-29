from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.covid_map_style import CovidMapStyle


T = TypeVar("T", bound="CovidMapData")


@_attrs_define
class CovidMapData:
    """
    Attributes:
        rs (str):  Example: 01001.
        cases (int): Fälle Example: 4711.
        cases_per_100k (float): Fälle/100.000 EW Example: 4711.123.
        cases7per100k (float): Fälle der letzten 7 Tage/100.000 EW Example: 47.11123.
        deaths (int): Todesfälle
        ewz (int): Einwohnerzahl Example: 471100.
        last_update (str):  Example: 26.09.2021, 00:00 Uhr.
        properties (CovidMapStyle):
    """

    rs: str
    cases: int
    cases_per_100k: float
    cases7per100k: float
    deaths: int
    ewz: int
    last_update: str
    properties: "CovidMapStyle"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rs = self.rs

        cases = self.cases

        cases_per_100k = self.cases_per_100k

        cases7per100k = self.cases7per100k

        deaths = self.deaths

        ewz = self.ewz

        last_update = self.last_update

        properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rs": rs,
                "cases": cases,
                "cases_per_100k": cases_per_100k,
                "cases7per100k": cases7per100k,
                "deaths": deaths,
                "ewz": ewz,
                "lastUpdate": last_update,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covid_map_style import CovidMapStyle

        d = dict(src_dict)
        rs = d.pop("rs")

        cases = d.pop("cases")

        cases_per_100k = d.pop("cases_per_100k")

        cases7per100k = d.pop("cases7per100k")

        deaths = d.pop("deaths")

        ewz = d.pop("ewz")

        last_update = d.pop("lastUpdate")

        properties = CovidMapStyle.from_dict(d.pop("properties"))

        covid_map_data = cls(
            rs=rs,
            cases=cases,
            cases_per_100k=cases_per_100k,
            cases7per100k=cases7per100k,
            deaths=deaths,
            ewz=ewz,
            last_update=last_update,
            properties=properties,
        )

        covid_map_data.additional_properties = d
        return covid_map_data

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
