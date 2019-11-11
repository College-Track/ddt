from src.helpers.classes import Site, Region

SITES = list()
REGIONS = list()

SITES.append(Site("College Track at The Durant Center", "PGC"))
SITES.append(Site("College Track Ward 8", "WARD 8"))
SITES.append(Site("College Track Watts", "WATTS"))
SITES.append(Site("College Track Boyle Heights", "BH"))
SITES.append(Site("College Track New Orleans", "NOLA"))
SITES.append(Site("College Track Denver", "DEN"))
SITES.append(Site("College Track Aurora", "AUR"))
SITES.append(Site("College Track Oakland", "OAK"))
SITES.append(Site("College Track Sacramento", "SAC"))
SITES.append(Site("College Track San Francisco", "SF"))
SITES.append(Site("College Track East Palo Alto", "EPA"))


REGIONS.append(Region("New Orleans", "NOLA", ["College Track New Orleans"], ["NOLA"]))

REGIONS.append(
    Region(
        "East Coast",
        "East Coast",
        ["College Track at the Durant Center", "College Track Ward 8"],
        ["PGC", "WARD 8"],
    )
)

REGIONS.append(
    Region(
        "Bay Area",
        "Bay Area",
        [
            "College Track Oakland",
            "College Track San Francisco",
            "College Track East Palo Alto",
        ],
        ["OAK", "SF", "EPA"],
    )
)

REGIONS.append(
    Region(
        "Northern California",
        "Nor Cal",
        [
            "College Track Oakland",
            "College Track San Francisco",
            "College Track East Palo Alto",
            "College Track Sacramento",
        ],
        ["OAK", "SF", "EPA", "SAC"],
    )
)

REGIONS.append(
    Region(
        "Los Angeles",
        "LA",
        ["College Track Watts", "College Track Boyle Heights"],
        ["WATTS", "BH"],
    )
)

REGIONS.append(
    Region(
        "Colorado",
        "CO",
        ["College Track Aurora", "College Track Denver"],
        ["AUR", "DEN"],
    )
)


