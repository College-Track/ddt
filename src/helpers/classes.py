from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Site:
    __slots__ = ["sf_name", "short_name"]
    sf_name: str
    short_name: str


@dataclass()
class Region:
    __slots__ = ["region_long", "region_short"]
    region_long: str
    region_short: str
    sites = []




