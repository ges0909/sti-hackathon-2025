from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.version import Version


T = TypeVar("T", bound="VersionCollection")


@_attrs_define
class VersionCollection:
    """
    Attributes:
        version (int):  Example: 9.
        hash_ (str):  Example: 3069be6324644ceb161afb3d53f7817de52a89fe38b6f5ae815ad0a8970dec7c.
        entries (list['Version']):
    """

    version: int
    hash_: str
    entries: list["Version"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        hash_ = self.hash_

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "hash": hash_,
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.version import Version

        d = dict(src_dict)
        version = d.pop("version")

        hash_ = d.pop("hash")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = Version.from_dict(entries_item_data)

            entries.append(entries_item)

        version_collection = cls(
            version=version,
            hash_=hash_,
            entries=entries,
        )

        version_collection.additional_properties = d
        return version_collection

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
