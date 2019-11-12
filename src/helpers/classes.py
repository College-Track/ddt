from dataclasses import dataclass
from typing import List


class Site():
    site_instances = {}
    def __init__(self, sf_name, short_name):
        self.sf_name = sf_name
        self.short_name = short_name
        Site.site_instances[self.short_name] = self 

    def __repr__(self):
        return (f'{self.__class__.__name__}'
        f'(sf_name={self.sf_name!r}, short_name={self.short_name!r})')
    


@dataclass()
class Region:
    __slots__ = ["region_long", "region_short"]
    region_long: str
    region_short: str
    sites = []




