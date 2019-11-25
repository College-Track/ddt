import requests
import csv
import pandas as pd
from dotenv import load_dotenv
import os
from salesforce_reporting import Connection, ReportParser
from src.helpers.helpers import generate_date_files
from pathlib import Path


load_dotenv()

SF_PASS = os.environ.get("SF_PASS")
SF_USERNAME = os.environ.get("SF_USERNAME")
SF_TOKEN = os.environ.get("SF_TOKEN")

data_files = generate_date_files()

raw_data = Path(".") / "data" / "raw"


sf = Connection(username=SF_USERNAME, password=SF_PASS, security_token=SF_TOKEN)


def load_report(report_id, sf):
    report_details = sf.get_report(report_id)
    parser = ReportParser(report_details)
    report = parser.records_dict()
    df = pd.DataFrame(report)

    while report_details["allData"] == False:
        existing_ids = ",".join(list(df["18 Digit ID"]))
        reportFilter = [
            {
                "value": f"{existing_ids}",
                "operator": "notEqual",
                "column": "Contact.X18_Digit_ID__c",
            }
        ]
        report_details = sf.get_report(report_id, filters=reportFilter)
        _parser = ReportParser(report_details)
        _report = _parser.records_dict()
        _df = pd.DataFrame(_report)
        df = df.append(_df, ignore_index=True)

    return df


for file in data_files[:1]:
    _df = load_report(file.report_id, sf)
    _df.to_csv(file.raw_file)
    _df.to_csv(raw_data.joinpath(file.raw_file))

print(len(df))
