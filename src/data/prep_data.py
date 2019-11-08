import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from src.helpers.variables import SITES

load_dotenv()

# Setup paths for reading and writing files
raw_data = Path(".") / "data" / "raw"
interim_data = Path(".") / "data" / "interim"


def update_site_name(df, SITES):
    """
    Adds a column to df with appriopriate site's abreviation. 
    If site is in df, but not SITES, will add full site name to new column.
    """
    df["site_short"] = ""
    for site in SITES:
        if df.Site.isin([site["sf_name"]]).any():
            df.loc[df.Site == site["sf_name"], "site_short"] = site["short_name"]
        else:
            df.loc[df.Site == site["sf_name"], "site_short"] = site["sf_name"]
    return df

# a JSON formatted list with details on each data file to load
data_files = [
    {
        "name": "count_demographics",
        "raw_file": "student_count_demo_11_7_2019.csv",
        "df": "",
        "interim_file": "count_demographics_interim.pkl",
    }
]

# loop over all the data files and apply cleaning functions and save as .pickle
for file in data_files:
    file["df"] = pd.read_csv(raw_data.joinpath(file["raw_file"]))

    # creates a data frame with all the sites, used to format the excel document
    if file["name"] == "count_demographics":
        sites = pd.DataFrame(file["df"]["Site"].unique())
        sites.columns = ["Site"]

    file["df"] = update_site_name(file["df"], SITES)
    file["df"].to_pickle(interim_data.joinpath(file["interim_file"]))
    sites.to_pickle(interim_data.joinpath("sites.pkl"))

