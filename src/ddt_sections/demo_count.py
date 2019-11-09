import pandas as pd
from pathlib import Path
from src.helpers.variables import REGIONS


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
    )
    return pivot_table

def calculate_region_totals(df, REGIONS)

first_gen_pivot = create_pivot_table(df, 'Indicator: First Generation')
gender_pivot = create_pivot_table(df, 'Gender')
race_pivot = create_pivot_table(df, 'Ethnic background')


print(first_gen_pivot)

print(gender_pivot)

print(race_pivot)