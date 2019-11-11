from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Site:
    __slots__ = ["sf_name", "short_name"]
    sf_name: str
    short_name: str


@dataclass(frozen=True)
class Region:
    __slots__ = ["region_long", "region_short", "sites_long", "sites_short"]
    region_long: str
    region_short: str
    sites_long: List
    sites_short: List



