import pandas as pd
from pathlib import Path
from src.helpers.helpers import generate_sites, generate_regions

SITES = generate_sites()
REGIONS = generate_regions(SITES)


interim_data = Path(".") / "data" / "interim" / "count_demographics_interim.pkl"

df = pd.read_pickle(interim_data)


def create_pivot_table(df, type):
    """Indicates what type of pivot table to create"""
    pivot_table = pd.pivot_table(
        df,
        index=["Contact Record Type", type],
        columns="site_short",
        values="18 Digit ID",
        aggfunc="count",
        fill_value=0,
        margins=True,
    )
    return pivot_table


# TODO: Determine how to manage sites that aren't in dataframe
def calculate_region_totals(df, REGIONS):
    for region in REGIONS:
        df[region.region_short] = 0
        _sites = [site.short_name for site in region.sites]
        df[region.region_short] = df[_sites].sum(axis=1)

    return df


first_gen_pivot = create_pivot_table(df, "Indicator: First Generation")
gender_pivot = create_pivot_table(df, "Gender")
race_pivot = create_pivot_table(df, "Ethnic background")


first_gen_pivot = calculate_region_totals(first_gen_pivot, REGIONS)
gender_pivot = calculate_region_totals(gender_pivot, REGIONS)
race_pivot = calculate_region_totals(race_pivot, REGIONS)


# print(first_gen_pivot)

# print(gender_pivot)

# print(race_pivot)

