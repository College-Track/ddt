import pandas as pd
import os
from pathlib import Path
import uuid
import names
import random
from datetime import datetime

# clean demographic data

raw_data = Path("..") / "data" / "raw"


df = pd.read_csv(raw_data.joinpath("student_count_demo.csv"))


# Replacing names with random names
df["Full Name"] = df["Full Name"].apply(lambda x: names.get_full_name())


def genDateOfBirth(number=1):
    CurrentTime = datetime.now()
    Year = random.randrange(2000, CurrentTime.year)
    for item in range(number):
        yield random.randrange(2000, CurrentTime.year), random.randrange(
            1, 12
        ), random.randrange(1, 31)


df["Birthdate"] = df["Birthdate"].apply(
    lambda x: next(f"{month}/{day}/{year}" for year, month, day in genDateOfBirth())
)

df["18 Digit ID"] = df["18 Digit ID"].apply(lambda x: str(uuid.uuid1()))

df.to_csv("test_demo.csv")

