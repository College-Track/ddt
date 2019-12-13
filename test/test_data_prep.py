import pytest
import pandas as pd
import numpy as np
from pathlib import Path


import src.data.prep_data as prep_data
import src.helpers.helpers as helpers


@pytest.fixture
def test_demographic_data():
    static_data = Path(".") / "test" / "static_data"
    df = pd.read_csv(static_data.joinpath("test_demo.csv"))
    return df


@pytest.fixture
def return_sites():
    SITES = helpers.generate_sites()
    return SITES


def test_update_site_name(test_demographic_data, return_sites):
    df = test_demographic_data
    SITES = return_sites

    returned_df = prep_data.update_site_name(df, SITES)
    assert returned_df.loc[0, "site_short"] == "OAK"
    assert pd.isna(returned_df["site_short"]).any() == False
