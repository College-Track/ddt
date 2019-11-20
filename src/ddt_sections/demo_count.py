import pandas as pd
from pathlib import Path
from src.helpers.helpers import generate_sites, generate_regions, calculate_region_totals

SITES = generate_sites()
REGIONS = generate_regions(SITES)


interim_data = Path(".") / "data" / "interim" / "count_demographics_interim.pkl"

df = pd.read_pickle(interim_data)


def create_pivot_table(df, type):
    """
    Indicates what type of pivot table to create
    type: what your second pivot indicator will be, ex first gen or gender
    """
    pivot_table = pd.pivot_table(
        df,
        index=["Contact Record Type", type],
        columns="site_short",
        values="18 Digit ID",
        aggfunc="count",
        fill_value=0,
        margins=True,
    )
    # remove the row sum as it is redundant with the National column
    pivot_table = pivot_table.drop("All", axis=1)
    return pivot_table



# TODO: Currently is inactive and manually done below, needs to have a better solution
def add_subtotals(df):
    tmp_df = df.sum(level=1, axis=0)
    tmp_df.name = "Totals"

    return df.append(tmp_df)


# TODO: Refactor
first_gen_pivot = create_pivot_table(df, "Indicator: First Generation")
gender_pivot = create_pivot_table(df, "Gender")
race_pivot = create_pivot_table(df, "Ethnic background")
income_pivot = create_pivot_table(df, "Indicator: Low-Income")


first_gen_pivot = calculate_region_totals(first_gen_pivot, REGIONS)
gender_pivot = calculate_region_totals(gender_pivot, REGIONS)
race_pivot = calculate_region_totals(race_pivot, REGIONS)
income_pivot = calculate_region_totals(income_pivot, REGIONS)

first_gen_totals = first_gen_pivot.sum(level=1, axis=0)
gender_totals = gender_pivot.sum(level=1, axis=0)
race_totals = race_pivot.sum(level=1, axis=0)
income_totals = income_pivot.sum(level=1, axis=0)


# print(first_gen_pivot)

# print(gender_pivot)

# print(race_pivot)

