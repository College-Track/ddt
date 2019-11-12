from dataclasses import dataclass, field
from typing import List


class Site:
    site_instances = {}

    def __init__(self, sf_name, short_name):
        self.sf_name = sf_name
        self.short_name = short_name
        Site.site_instances[self.short_name] = self

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(sf_name={self.sf_name!r}, short_name={self.short_name!r})"
        )


class Region:
    region_instances = []

    def __init__(self, region_long, region_short):
        self.region_long = region_long
        self.region_short = region_short
        self.sites = []
        Region.region_instances.append(self)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(region_long={self.region_long!r}, region_short={self.region_short!r})"
        )

