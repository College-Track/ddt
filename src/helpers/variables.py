from src.helpers.classes import Site, Region

SITES = list()
REGIONS = list()

# All Sites
_pgc = Site("College Track at The Durant Center", "PGC")
_ward_8 = Site("College Track Ward 8", "WARD 8")
_watts = Site("College Track Watts", "WATTS")
_boyle_heights = Site("College Track Boyle Heights", "BH")
_nola = Site("College Track New Orleans", "NOLA")
_den = Site("College Track Denver", "DEN")
_aur = Site("College Track Aurora", "AUR")
_oak = Site("College Track Oakland", "OAK")
_sac = Site("College Track Sacramento", "SAC")
_sf = Site("College Track San Francisco", "SF")
_epa = Site("College Track East Palo Alto", "EPA")

SITES.extend([_pgc, _ward_8, _boyle_heights, _nola, _den, _aur, _oak, _sac, _sf, _epa])

# All Regions
_nor_cal = Region("Northern California", "Nor Cal")
_nola_region = Region("New Orleans", "NOLA")
_east_coast = Region("East Coast", "East Coast")
_bay_area = Region("Bay Area", "Bay Area")
_la_region = Region("Lost Angeles", "LA")
_colorado = Region("Colorado", "CO")


_nor_cal.sites.extend([_epa, _sf, _oak, _sac])
_nola_region.sites.extend([_nola])
_east_coast.sites.extend([_ward_8, _pgc])
_bay_area.sites.extend([_oak, _sf, _sac])
_la_region.sites.extend([_watts, _boyle_heights])
_colorado.sites.extend([_aur, _epa])

REGIONS.extend([_nor_cal, _nola_region, _east_coast, _bay_area, _la_region, _colorado])

