import requests
import csv
import pandas as pd
from dotenv import load_dotenv
import os
from salesforce_reporting import Connection, ReportParser
from src.helpers.helpers import generate_date_files
from pathlib import Path




# SF_PASS = os.environ.get("SF_PASS")
# SF_USERNAME = os.environ.get("SF_USERNAME")
# SF_TOKEN = os.environ.get("SF_TOKEN")

# data_files = generate_date_files()

# raw_data = Path(".") / "data" / "raw"


# sf = Connection(username=SF_USERNAME, password=SF_PASS, security_token=SF_TOKEN)

def load_sf_reports(data_files, sf, raw_data):
    for file in data_files[:1]:
        _df = file.load_report(sf)
        file.write_raw_csv(_df, raw_data)
    
    return data_files


