from src.helpers.classes import Site, Region


def generate_sites():

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

    return Site.site_instances


def generate_regions(SITES):
    REGIONS = []
    _nor_cal = Region("Northern California", "Nor Cal")
    _nola_region = Region("New Orleans", "NOLA")
    _east_coast = Region("East Coast", "East Coast")
    _bay_area = Region("Bay Area", "Bay Area")
    _la_region = Region("Lost Angeles", "LA")
    _colorado = Region("Colorado", "CO")
    _national = Region("National", "National")

    _nor_cal.sites.extend([SITES["EPA"], SITES["SF"], SITES["OAK"], SITES["SAC"]])
    _nola_region.sites.extend([SITES["NOLA"]])
    _east_coast.sites.extend([SITES["WARD 8"], SITES["PGC"]])
    _bay_area.sites.extend([SITES["EPA"], SITES["SF"], SITES["OAK"]])
    _la_region.sites.extend([SITES["WATTS"], SITES["BH"]])
    _colorado.sites.extend([SITES["AUR"], SITES["DEN"]])

    for site in SITES.keys():

        _national.sites.append(SITES[site])

    REGIONS.extend(
        [
            _nor_cal,
            _nola_region,
            _east_coast,
            _bay_area,
            _la_region,
            _colorado,
            _national,
        ]
    )
    return REGIONS
