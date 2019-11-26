import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from src.helpers.helpers import generate_sites, generate_date_files

# from src.data.load_data import data_files

load_dotenv()

SITES = generate_sites()


# Setup paths for reading and writing files
raw_data = Path(".") / "data" / "raw"
interim_data = Path(".") / "data" / "interim"


def update_site_name(df, SITES):
    """
    Adds a column to df with appriopriate site's abreviation.
    If site is in df, but not SITES, will add full site name to new column.
    """
    df["site_short"] = ""
    for site in SITES.values():
        if (df.Site == site.sf_name).any():
            df.loc[df.Site == site.sf_name, "site_short"] = site.short_name
        else:
            df.loc[df.Site == site.sf_name, "site_short"] = site.sf_name
    return df


def prep_data(data_files):
    # loop over all the data files and apply cleaning functions and save as .pickle
    for file in data_files:
        file.df = pd.read_csv(raw_data.joinpath(file.raw_file))

        # creates a data frame with all the sites, used to format the excel document
        if file.name == "count_demographics":
            sites = pd.DataFrame(file.df["Site"].unique())
            sites.columns = ["Site"]

        file.df = update_site_name(file.df, SITES)
        # TODO: make sure index is working correctly
        file.df.to_pickle(interim_data.joinpath(file.interim_file))
        file.df.to_csv(interim_data.joinpath(file.test_file))
        sites.to_pickle(interim_data.joinpath("sites.pkl"))

