import pandas as pd
from dotenv import load_dotenv
import os
from pathlib import Path
from salesforce_reporting import Connection, ReportParser


from src.data.load_data import load_sf_reports
from src.data.prep_data import prep_data
from src.helpers.helpers import generate_date_files


load_dotenv()

SF_PASS = os.environ.get("SF_PASS")
SF_USERNAME = os.environ.get("SF_USERNAME")
SF_TOKEN = os.environ.get("SF_TOKEN")

sf = Connection(username=SF_USERNAME, password=SF_PASS, security_token=SF_TOKEN)


data_files = generate_date_files()

raw_data = Path(".") / "data" / "raw"


def main():
    load_sf_reports(data_files, sf, raw_data)
    prep_data(data_files)


if __name__ == "__main__":
    main()
