"""Unit tests for VentureEvaluator."""

import pytest
from bastar_innovate.evaluator import VentureEvaluator
from bastar_innovate.repository import VentureRepository


@pytest.fixture
def evaluator():
    return VentureEvaluator()


def test_ranking_returns_20_ideas(evaluator):
    """Verify ranking returns all 20 ideas sorted descending by default."""
    ranked = evaluator.rank_ideas(sort_by="composite")
    assert len(ranked) == 20
    scores = [ev.composite_score for _, ev in ranked]
    assert scores == sorted(scores, reverse=True)


def test_rank_by_prototype_feasibility(evaluator):
    """Verify ranking by specific criterion."""
    ranked = evaluator.rank_ideas(sort_by="prototype_feasibility")
    assert len(ranked) == 20
    feas_scores = [ev.prototype_feasibility for _, ev in ranked]
    assert feas_scores == sorted(feas_scores, reverse=True)


def test_get_top_5(evaluator):
    """Verify get_top_n returns top 5 highest scored ideas."""
    top5 = evaluator.get_top_n(n=5, criterion="composite")
    assert len(top5) == 5
    top_ids = [idea.id for idea, _ in top5]
    # Check that known flagship contenders are in the top tier
    assert any(x in top_ids for x in ["hemopoint", "ferroclear", "conveyorguard", "mahuashilp"])


def test_pareto_frontier(evaluator):
    """Verify Pareto frontier returns non-empty list of non-dominated ventures."""
    frontier = evaluator.pareto_frontier(
        dim_x="prototype_feasibility",
        dim_y="social_environmental_impact",
        dim_z="competition_potential",
    )
    assert len(frontier) > 0
    # Every point on the frontier must be valid
    for idea, ev in frontier:
        assert ev.composite_score > 8.5


def test_sensitivity_analysis_scenarios(evaluator):
    """Verify sensitivity testing generates top-5 rankings for all scenarios."""
    scenarios = evaluator.sensitivity_analysis()
    assert "balanced_default" in scenarios
    assert "competition_winning_priority" in scenarios
    assert "commercial_scalability_priority" in scenarios
    assert "student_feasibility_priority" in scenarios
    assert "social_environmental_impact_priority" in scenarios

    for name, top_list in scenarios.items():
        assert len(top_list) == 5
