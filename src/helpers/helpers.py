from src.helpers.classes import Site, Region, DataFile


def generate_sites():
    """
    Used to generate a dictionary of all the active sites.
    If a new site is created, it must be added to this function
    The dictionary is instantiated in the Site class
    """
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
    """
    Used to generate a list of all regions and the sites
    that belong in the region.
    The list lives on the Region class.
    """
    _nor_cal = Region("Northern California", "Nor Cal")
    # _nola_region = Region("New Orleans", "NOLA")
    _east_coast = Region("East Coast", "East Coast")
    _bay_area = Region("Bay Area", "Bay Area")
    _la_region = Region("Lost Angeles", "LA")
    _colorado = Region("Colorado", "CO")
    _national = Region("National", "National")

    _nor_cal.sites.extend([SITES["EPA"], SITES["SF"], SITES["OAK"], SITES["SAC"]])
    # _nola_region.sites.extend([SITES["NOLA"]])

    _east_coast.sites.extend([SITES["PGC"]])
    _bay_area.sites.extend([SITES["EPA"], SITES["SF"], SITES["OAK"]])
    _la_region.sites.extend([SITES["WATTS"], SITES["BH"]])
    _colorado.sites.extend([SITES["AUR"], SITES["DEN"]])

    for site in SITES.values():
        _national.sites.append(site)

    return Region.region_instances


def generate_date_files():

    count_demographics = DataFile(
        "count_demographics",
        "00O1M000007Qak4UAC",
        "student_count_demo.csv",
        "count_demographics_interim.pkl",
        "count_demographics_interim.csv",
    )

    workshop_attendance = DataFile(
        "workshop_attendance",
        "",
        "workshop_attendance.csv",
        "workshop_attendance_interim.pkl",
        "workshop_attendance_interim.csv",
    )

    community_service = DataFile(
        "community_service_all_time",
        "",
        "community_service_all_time.csv",
        "community_service_all_time_interim.pkl",
        "community_service_all_time_interim.csv",
    )
    return DataFile.data_files


def calculate_region_totals(df, REGIONS):
    """Calculates the regional totals for each measure in the given data frame."""
    for region in REGIONS:
        df[region.region_short] = 0
        _sites = [site.short_name for site in region.sites]
        # removing sites which are instantiated, but no data exist yet
        _sites_complete = [site for site in _sites if site in list(df.columns)]

        df[region.region_short] = df[_sites_complete].sum(axis=1)

    return df
