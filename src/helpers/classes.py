from dataclasses import dataclass, field
from typing import List
from salesforce_reporting import Connection, ReportParser
import pandas as pd
from pathlib import Path



class Site:
    """
    For individual sites, need the short (ddt purpose) name and the full Salesforce name
    """

    site_instances = {}

    def __init__(self, sf_name, short_name):
        self.sf_name = sf_name
        self.short_name = short_name
        Site.site_instances[self.short_name] = self

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(sf_name={self.sf_name!r}, short_name={self.short_name!r})"
        )


class Region:
    """
    For CT regions. Region needs short (ddt purpose) name and full Salesforce name. 
    Upon initiation an empty list is created which will then get populated with the region's sites
    """

    region_instances = []

    def __init__(self, region_long, region_short):
        self.region_long = region_long
        self.region_short = region_short
        self.sites = []
        Region.region_instances.append(self)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(region_long={self.region_long!r}, region_short={self.region_short!r})"
        )


class Sheet:
    """
    For organization purposes to group all metric categories and metrics
    in a single class
    """
    sheet_instances = []
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.metric_category = []
        Sheet.sheet_instances.append(self)

    def __repr__(self):
        return f"Sheet({self.sheet_name})"

class MetricCategory(Sheet):
    """
    For all grouping of metrics that belong on a single sheet
    """

    def __init__(self, sheet, category_name, reporting_group, pull_date, next_update):
        self.sheet = sheet
        self.category_name = category_name
        self.reporting_group = reporting_group
        self.pull_date = pull_date
        self.next_update = next_update
        self.metrics = []
        sheet.metric_category.append(self)

    def __getattr__(self, attr):
        return getattr(self.sheet, attr)

    def __repr__(self):
        return f"MetricCategory({self.category_name})"

class Metric(MetricCategory):
    """
    For inidivual metrics assigned to a Metric Category
    """

    def __init__(self, metric_category, metric_name, definition="Please provude a definition", additional_content=""):
        self.metric_name = metric_name
        self.metric_category = metric_category
        self.definition = definition
        self.additional_content = additional_content
        self.metric_df = None
        metric_category.metrics.append(self)
        

    def __getattr__(self, attr):
        return getattr(self.metric_category,attr)

    def __repr__(self):
        return f"Metric({self.metric_name, self.metric_category.category_name})"



class DataFile():
    data_files = []
    def __init__(self, name, report_id, raw_file, interim_file, test_file=""):
        self.name = name
        self.report_id = report_id
        self.raw_file = raw_file
        self.interim_file = interim_file
        self.df = None
        self.test_file = test_file
        DataFile.data_files.append(self)

    
    def load_report(self, sf):
        report_details = sf.get_report(self.report_id)
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
            report_details = sf.get_report(self.report_id, filters=reportFilter)
            _parser = ReportParser(report_details)
            _report = _parser.records_dict()
            _df = pd.DataFrame(_report)
            df = df.append(_df, ignore_index=True)

        return df

    def write_raw_csv(self, df, raw_data):
        df.to_csv(raw_data.joinpath(self.raw_file))