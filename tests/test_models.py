"""Unit tests for Pydantic data models."""

import pytest
from pydantic import ValidationError

from bastar_innovate.models import (
    BOMItem,
    EliminatedIdea,
    EvaluationMetric,
    FinancialProjection,
    GrantOpportunity,
    PilotRoadmap,
    ProblemStatement,
    PrototypeSpec,
    RiskFactor,
    SolutionSpec,
    StartupBlueprint,
    StartupIdea,
    UserSegmentation,
)


def test_evaluation_metric_composite_calculation():
    """Test composite score calculation and weight normalization."""
    ev = EvaluationMetric(
        idea_id="test_idea",
        name="Test Venture",
        problem_severity=10.0,
        existing_demand=10.0,
        prototype_feasibility=10.0,
        student_team_feasibility=10.0,
        market_scalability=10.0,
        competitive_differentiation=10.0,
        revenue_potential=10.0,
        social_environmental_impact=10.0,
        competition_potential=10.0,
        local_pilot_feasibility=10.0,
        grant_csr_potential=10.0,
        technical_defensibility=10.0,
        regulatory_simplicity=10.0,
        capital_efficiency=10.0,
    )
    score = ev.calculate_composite()
    assert score == 10.0
    assert ev.composite_score == 10.0


def test_evaluation_metric_custom_weights():
    """Test calculation with custom weight scenario."""
    ev = EvaluationMetric(
        idea_id="test_custom",
        name="Custom Venture",
        problem_severity=9.0,
        existing_demand=8.0,
        prototype_feasibility=7.0,
        student_team_feasibility=8.0,
        market_scalability=8.0,
        competitive_differentiation=9.0,
        revenue_potential=7.0,
        social_environmental_impact=9.0,
        competition_potential=8.0,
        local_pilot_feasibility=9.0,
        grant_csr_potential=8.0,
        technical_defensibility=8.0,
        regulatory_simplicity=8.0,
        capital_efficiency=8.0,
    )
    custom_w = {k: 1.0 / 14 for k in [
        "problem_severity", "existing_demand", "prototype_feasibility",
        "student_team_feasibility", "market_scalability", "competitive_differentiation",
        "revenue_potential", "social_environmental_impact", "competition_potential",
        "local_pilot_feasibility", "grant_csr_potential", "technical_defensibility",
        "regulatory_simplicity", "capital_efficiency",
    ]}
    score = ev.calculate_composite(custom_w)
    assert 7.0 <= score <= 9.0


def test_bom_item_model():
    """Test BOMItem model fields."""
    bom = BOMItem(
        item="ESP32-S3 Microcontroller",
        specification="Dual-core 240MHz with 8MB PSRAM",
        quantity=2,
        unit_cost_inr=650,
        source_vendor="Robu.in",
        total_cost_inr=1300,
    )
    assert bom.quantity == 2
    assert bom.total_cost_inr == 1300


def test_eliminated_idea_model():
    """Test model for rejected concepts."""
    elim = EliminatedIdea(
        id="elim_test",
        name="Drone Delivery in Reserved Forests",
        category="UAV Logistics",
        proposed_concept="Autonomous cargo drones dropping medicines into Bastar villages",
        rejection_reasons=["Strict DGCA and security clearance restrictions in Naxalite corridors", "Prohibitive capex >₹2 Lakhs"],
        fatal_flaws=["Regulatory Barrier", "High Capex"],
    )
    assert elim.id == "elim_test"
    assert len(elim.fatal_flaws) == 2


def test_prototype_spec_validation():
    """Test prototype spec constraints."""
    proto = PrototypeSpec(
        components=["ESP32", "Sensor"],
        technologies=["Embedded C++"],
        budget_inr=6500,
        budget_range="₹6,000 - ₹7,000",
        complexity="Medium",
        required_skills=["Embedded Systems"],
        expected_dev_time_weeks=6,
    )
    assert proto.budget_inr == 6500
    assert proto.expected_dev_time_weeks == 6


def test_invalid_prototype_spec():
    """Verify missing required fields raises ValidationError."""
    with pytest.raises(ValidationError):
        PrototypeSpec(
            components=["Incomplete"],
            budget_range="Unknown",
        )
