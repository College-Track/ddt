import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from src.helpers.variables import SITES

load_dotenv()

raw_data = Path('.') /"data"/"raw"

data_files = {
    "count_demographics": "student_count_demo_11_7_2019.csv",
    }

list_of_df = []

for file in data_files.values():
    list_of_df.append(pd.read_csv(raw_data.joinpath(file)))


def update_site_name(df,SITES):
    df["site_short"] = ""
    for site in SITES:
        if df.Site.isin([site["sf_name"]]).any():
            df.loc[df.Site == site['sf_name'],'site_short'] = site['short_name']
    return df
            
    

for df in list_of_df:
    df = update_site_name(df,SITES)


print(list_of_df[0].head())