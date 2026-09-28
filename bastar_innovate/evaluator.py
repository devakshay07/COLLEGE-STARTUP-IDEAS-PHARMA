"""Multi-criteria decision analysis (MCDA), scoring, and ranking engine."""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple
from bastar_innovate.models import EvaluationMetric, StartupIdea
from bastar_innovate.repository import VentureRepository


class VentureEvaluator:
    """Analytical evaluation engine for ranking, Pareto analysis, and sensitivity testing."""

    def __init__(self, repository: Optional[VentureRepository] = None):
        self.repo = repository or VentureRepository()

    def rank_ideas(
        self,
        sort_by: str = "composite",
        ascending: bool = False,
        custom_weights: Optional[Dict[str, float]] = None,
    ) -> List[Tuple[StartupIdea, EvaluationMetric]]:
        """Rank all 20 ideas according to composite score or a specific criterion."""
        ideas = {idea.id: idea for idea in self.repo.get_all_ideas()}
        evals = self.repo.get_all_evaluations()

        if custom_weights:
            for ev in evals:
                ev.calculate_composite(custom_weights)

        def get_sort_key(ev: EvaluationMetric) -> float:
            if sort_by == "composite":
                return ev.composite_score
            if hasattr(ev, sort_by):
                return getattr(ev, sort_by)
            return ev.composite_score

        sorted_evals = sorted(evals, key=get_sort_key, reverse=not ascending)
        return [(ideas[ev.idea_id], ev) for ev in sorted_evals if ev.idea_id in ideas]

    def get_top_n(self, n: int = 5, criterion: str = "composite") -> List[Tuple[StartupIdea, EvaluationMetric]]:
        """Retrieve top N ideas for a given criterion."""
        ranked = self.rank_ideas(sort_by=criterion)
        return ranked[:n]

    def pareto_frontier(
        self,
        dim_x: str = "prototype_feasibility",
        dim_y: str = "social_environmental_impact",
        dim_z: str = "competition_potential",
    ) -> List[Tuple[StartupIdea, EvaluationMetric]]:
        """Identify non-dominated solutions on a 2D or 3D Pareto frontier."""
        ranked = self.rank_ideas(sort_by="composite")
        frontier: List[Tuple[StartupIdea, EvaluationMetric]] = []

        for idea, ev in ranked:
            x = getattr(ev, dim_x)
            y = getattr(ev, dim_y)
            z = getattr(ev, dim_z)
            is_dominated = False

            for other_idea, other_ev in ranked:
                if other_idea.id == idea.id:
                    continue
                ox = getattr(other_ev, dim_x)
                oy = getattr(other_ev, dim_y)
                oz = getattr(other_ev, dim_z)

                if ox >= x and oy >= y and oz >= z and (ox > x or oy > y or oz > z):
                    is_dominated = True
                    break

            if not is_dominated:
                frontier.append((idea, ev))

        return frontier

    def sensitivity_analysis(
        self,
        scenarios: Optional[Dict[str, Dict[str, float]]] = None,
    ) -> Dict[str, List[str]]:
        """Test rank resilience under diverse stakeholder preference scenarios."""
        standard_scenarios = scenarios or {
            "balanced_default": None,
            "competition_winning_priority": {
                "competition_potential": 0.25,
                "problem_severity": 0.15,
                "prototype_feasibility": 0.15,
                "social_environmental_impact": 0.15,
                "technical_defensibility": 0.10,
                "existing_demand": 0.08,
                "market_scalability": 0.05,
                "student_team_feasibility": 0.05,
                "revenue_potential": 0.02,
            },
            "commercial_scalability_priority": {
                "market_scalability": 0.20,
                "revenue_potential": 0.20,
                "existing_demand": 0.15,
                "competitive_differentiation": 0.15,
                "capital_efficiency": 0.10,
                "problem_severity": 0.10,
                "prototype_feasibility": 0.10,
            },
            "student_feasibility_priority": {
                "prototype_feasibility": 0.25,
                "student_team_feasibility": 0.20,
                "capital_efficiency": 0.15,
                "local_pilot_feasibility": 0.15,
                "regulatory_simplicity": 0.15,
                "problem_severity": 0.10,
            },
            "social_environmental_impact_priority": {
                "social_environmental_impact": 0.30,
                "problem_severity": 0.25,
                "local_pilot_feasibility": 0.15,
                "grant_csr_potential": 0.15,
                "prototype_feasibility": 0.15,
            },
        }

        results: Dict[str, List[str]] = {}
        for name, weights in standard_scenarios.items():
            normalized_weights = self._normalize_weights(weights) if weights else None
            ranked = self.rank_ideas(custom_weights=normalized_weights)
            results[name] = [idea.name for idea, _ in ranked[:5]]

        return results

    @staticmethod
    def _normalize_weights(weights: Dict[str, float]) -> Dict[str, float]:
        """Ensure sum of weights equals 1.0, filling missing dimensions with 0."""
        all_keys = [
            "problem_severity", "existing_demand", "prototype_feasibility",
            "student_team_feasibility", "market_scalability", "competitive_differentiation",
            "revenue_potential", "social_environmental_impact", "competition_potential",
            "local_pilot_feasibility", "grant_csr_potential", "technical_defensibility",
            "regulatory_simplicity", "capital_efficiency",
        ]
        total = sum(weights.values())
        norm = {k: weights.get(k, 0.0) / total for k in all_keys}
        return norm
