"""Unit tests for VentureRepository."""

import pytest
from bastar_innovate.repository import VentureRepository


@pytest.fixture
def repo():
    return VentureRepository()


def test_repository_loads_exactly_20_ideas(repo):
    """Verify repository loads exactly 20 curated startup ideas."""
    ideas = repo.get_all_ideas()
    assert len(ideas) == 20
    # Verify sequential numbers 1 to 20
    numbers = [i.number for i in ideas]
    assert numbers == list(range(1, 21))


def test_unique_idea_ids(repo):
    """Verify all idea IDs are unique strings."""
    ideas = repo.get_all_ideas()
    ids = [i.id for i in ideas]
    assert len(ids) == len(set(ids))


def test_lookup_by_id_and_number(repo):
    """Verify lookup by both slug ID and integer string."""
    idea_hemopoint = repo.get_idea("hemopoint")
    assert idea_hemopoint is not None
    assert idea_hemopoint.name.startswith("HemoPoint")

    idea_by_num = repo.get_idea("6")
    assert idea_by_num is not None
    assert idea_by_num.id == "hemopoint"

    non_existent = repo.get_idea("non_existent_id")
    assert non_existent is None


def test_prototype_budget_constraints(repo):
    """Verify all 20 prototypes are student-feasible (under ₹15,000 INR)."""
    ideas = repo.get_all_ideas()
    for idea in ideas:
        assert 4000 <= idea.prototype.budget_inr <= 15000, f"Idea {idea.id} budget out of student range: {idea.prototype.budget_inr}"


def test_eliminated_ideas_loaded(repo):
    """Verify eliminated candidates pool has exactly 5 ideas with explicit rationale."""
    elim = repo.get_eliminated_ideas()
    assert len(elim) == 5
    for item in elim:
        assert len(item.rejection_reasons) > 0
        assert len(item.fatal_flaws) > 0


def test_grants_data_loaded(repo):
    """Verify grants database contains active central/state schemes."""
    grants = repo.get_grants_data()
    assert len(grants) >= 8
    grant_ids = [g["id"] for g in grants]
    assert "dst_nidhi_prayas" in grant_ids
    assert "birac_big" in grant_ids
    assert "bastar_dmf" in grant_ids


def test_context_data_loaded(repo):
    """Verify Bastar geographic and economic context data."""
    ctx = repo.get_context()
    assert "geography" in ctx
    assert ctx["geography"]["headquarters"] == "Jagdalpur"
    assert "ground_challenges" in ctx


def test_search_by_sector(repo):
    """Verify filtering ideas by sector."""
    health_ideas = repo.search_by_sector("Health")
    assert len(health_ideas) >= 3
    for idea in health_ideas:
        assert "health" in idea.sector.lower() or "med" in idea.sector.lower()


def test_filter_by_max_budget(repo):
    """Verify budget filtering."""
    low_budget = repo.filter_by_max_budget(7000)
    assert len(low_budget) > 0
    for idea in low_budget:
        assert idea.prototype.budget_inr <= 7000


def test_all_ideas_have_evaluations(repo):
    """Verify every idea has an associated evaluation metric."""
    ideas = repo.get_all_ideas()
    for idea in ideas:
        ev = repo.get_evaluation(idea.id)
        assert ev is not None
        assert 8.5 <= ev.composite_score <= 10.0
