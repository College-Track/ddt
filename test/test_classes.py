import pytest

import src.helpers.helpers as helpers
from src.helpers.classes import Site, Region, DataFile


@pytest.fixture
def site():
    """
    Returns a test site for Arlen
    """
    arlen = Site("College Track Arlen", "Arlen")
    return arlen


@pytest.fixture
def region():
    """Returns a test region for Texas"""
    texas = Region("College Track Texas", "TEX")
    return texas


def test_site_instantiation(site):

    assert site.sf_name == "College Track Arlen"
    assert site.short_name == "Arlen"
    assert len(Site.site_instances) == 1


def test_region_instantiation(region):
    assert region.region_long == "College Track Texas"
    assert region.region_short == "TEX"
    assert len(Region.region_instances) == 1


def test_site_append_to_region(site, region):
    region.sites.append(site)

    assert len(region.sites) == 1
    assert region.sites[0].short_name == "Arlen"


#  def test_generate_sites():
#     sites = helpers.generate_sites()
#     assert len(sites) == 11
#     assert type(sites) == dict
