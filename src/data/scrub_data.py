import pandas as pd
import os
from pathlib import Path
import uuid
import names
from random import randint
from datetime import datetime, timedelta


# clean demographic data

raw_data = Path(".") / "data" / "raw"


df = pd.read_csv(raw_data.joinpath("student_count_demo.csv"))

# Converting Birthdate to datetime object in order to randomize it

df["Birthdate"] = pd.to_datetime(df.Birthdate, errors="coerce")

# Randomizing the birthdate by adding or subtracting 30 days
df["Birthdate"] = df.Birthdate.apply(lambda x: x + timedelta(days=randint(-30, 30)))

# Converting back into the original string format
df["Birthdate"] = df.Birthdate.dt.strftime("%m/%d/%Y")

# Replacing names with a split up version of 18 Digit ID
df["Full Name"] = df["18 Digit ID"].apply(
    lambda x: (" ").join([x[i : i + 9] for i in range(0, len(x), 9)])
)


# Filtering the data so only 5 students from each site appear
df = df.groupby("Site").head(5)

df.to_csv("test/static_data/test_demo.csv", index=False)

