"""Unit tests for GrantMatcher."""

import pytest
from bastar_innovate.grants import GrantMatcher
from bastar_innovate.repository import VentureRepository


@pytest.fixture
def matcher():
    return GrantMatcher()


@pytest.fixture
def repo():
    return VentureRepository()


def test_grant_matcher_matches_medtech_to_birac(matcher, repo):
    """Verify MedTech venture (HemoPoint) matches with BIRAC BIG."""
    hemopoint = repo.get_idea("hemopoint")
    matches = matcher.match_idea(hemopoint)
    scheme_ids = [m.scheme_id for m in matches]
    assert "birac_big" in scheme_ids
    assert "bastar_dmf" in scheme_ids


def test_grant_matcher_matches_mining_to_nmdc_csr(matcher, repo):
    """Verify industrial safety venture (ConveyorGuard) matches with NMDC CSR."""
    cg = repo.get_idea("conveyorguard")
    matches = matcher.match_idea(cg)
    scheme_ids = [m.scheme_id for m in matches]
    assert "nmdc_csr" in scheme_ids
    assert "dst_nidhi_prayas" in scheme_ids


def test_total_grant_potential(matcher, repo):
    """Verify aggregated pipeline calculation."""
    mahuashilp = repo.get_idea("mahuashilp")
    pipeline = matcher.total_grant_potential(mahuashilp)
    assert pipeline["qualified_schemes_count"] >= 3
    assert pipeline["total_potential_pipeline_inr"] > 1000000
    assert "Lakhs" in pipeline["formatted_pipeline"]
