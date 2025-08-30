from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rss_channel import RssChannel


T = TypeVar("T", bound="Rss")


@_attrs_define
class Rss:
    """
    Attributes:
        version (Union[Unset, str]):  Example: 2.0.
        channel (Union[Unset, RssChannel]):
    """

    version: Union[Unset, str] = UNSET
    channel: Union[Unset, "RssChannel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        channel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rss_channel import RssChannel

        d = dict(src_dict)
        version = d.pop("version", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, RssChannel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = RssChannel.from_dict(_channel)

        rss = cls(
            version=version,
            channel=channel,
        )

        rss.additional_properties = d
        return rss

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
