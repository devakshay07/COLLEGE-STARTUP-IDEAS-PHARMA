"""Bastar Innovate: Venture Intelligence and Innovation Acceleration Platform.

One Institution – One Startup initiative for B.Tech Engineering College, Jagdalpur, Bastar, Chhattisgarh.
"""

__version__ = "1.0.0"

from bastar_innovate.blueprints import get_flagship_blueprints
from bastar_innovate.evaluator import VentureEvaluator
from bastar_innovate.exporter import VentureExporter
from bastar_innovate.financials import FinancialEngine, ThreeYearFinancialModel, UnitEconomics
from bastar_innovate.grants import GrantMatcher, SchemeMatch
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
)
from bastar_innovate.repository import VentureRepository

__all__ = [
    "VentureRepository",
    "VentureEvaluator",
    "FinancialEngine",
    "GrantMatcher",
    "VentureExporter",
    "StartupIdea",
    "EvaluationMetric",
    "StartupBlueprint",
    "EliminatedIdea",
    "UnitEconomics",
    "ThreeYearFinancialModel",
    "SchemeMatch",
    "BOMItem",
    "ProblemStatement",
    "SolutionSpec",
    "PrototypeSpec",
    "PilotRoadmap",
    "FinancialProjection",
    "GrantOpportunity",
    "RiskFactor",
    "get_flagship_blueprints",
]
