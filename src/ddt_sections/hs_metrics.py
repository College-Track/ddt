import pandas as pd
from pathlib import Path
from src.helpers.helpers import (
    generate_sites,
    generate_regions,
    calculate_region_totals,
)
from src.helpers.classes import Sheet, MetricCategory, Metric

import numpy as np

SITES = generate_sites()
REGIONS = generate_regions(SITES)

# instatiate the excel sheet for all of these metrics
hs_metrics = Sheet("HS Metrics")


def generate_total_workshop(df, workshop_attendance):

    total_workshops = Metric(
        workshop_attendance,
        "Total # of Workshops Sessions Attended",
        definition="Total # of workshop sessions that students attended in 2018-2019",
        additional_content='Workshop sessions with an attendance status of "Attended, Drop-In, Tardy, or Make-Up" were included in this analysis.',
    )

    count_workshop_sessions = pd.pivot_table(
        df, columns="site_short", values="18 Digit ID", aggfunc="count", fill_value=0
    )

    count_workshop_sessions = calculate_region_totals(count_workshop_sessions, REGIONS)

    total_workshops.metric_df = count_workshop_sessions

    return workshop_attendance


def generate_workshop_hours(df, workshop_attendance):
    total_workshops_hours = Metric(
        workshop_attendance,
        "Workshop Hours Attended: Total",
        definition="# of workshop hours that students attended in 2018-2019: All workshops",
        additional_content="Workshop hours were calculated by taking the workshop sessions attended (Row 10) and adding up the durations.",
    )

    workshop_sessions_hours = pd.pivot_table(
        df,
        index="Workshop Department",
        columns="site_short",
        values="Workshop Session: Workshop Duration",
        aggfunc=np.sum,
        fill_value=0,
        margins=True,
    )
    workshop_sessions_hours = workshop_sessions_hours.div(60)

    workshop_sessions_hours = calculate_region_totals(workshop_sessions_hours, REGIONS)
    total_workshops_hours.df = workshop_sessions_hours

    return workshop_attendance


def create_workshop_attendance_cat(hs_metrics):
    workshop_attendance = MetricCategory(
        hs_metrics,
        "Workshop & Attendance",
        "Class of 2019-2022",
        "Aug 2019",
        "June 2020",
    )

    workshop_interim_data = (
        Path(".") / "data" / "interim" / "workshop_attendance_interim.pkl"
    )

    workshop_attendance_df = pd.read_pickle(workshop_interim_data)

    workshop_attendance = generate_total_workshop(
        workshop_attendance_df, workshop_attendance
    )

    workshop_attendance = generate_workshop_hours(
        workshop_attendance_df, workshop_attendance
    )

    return workshop_attendance


workshop_attendance = create_workshop_attendance_cat(hs_metrics)


