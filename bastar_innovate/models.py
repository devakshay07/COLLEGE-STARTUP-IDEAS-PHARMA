"""Data models for Bastar Innovation Venture Intelligence Engine."""

from __future__ import annotations

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ProblemStatement(BaseModel):
    """Detailed statement of the real-world problem."""
    target_affected: str = Field(..., description="Who experiences the problem and location")
    frequency: str = Field(..., description="How frequently the problem occurs")
    why_existing_fail: str = Field(..., description="Why current solutions fail or are insufficient")
    consequence_if_unsolved: str = Field(..., description="Measurable impact if problem remains unsolved")
    evidence_and_sources: List[str] = Field(default_factory=list, description="Citations and evidence")


class SolutionSpec(BaseModel):
    """Specific technical solution details."""
    description: str = Field(..., description="Overview of what is built")
    hardware: List[str] = Field(default_factory=list)
    software: List[str] = Field(default_factory=list)
    ai_ml_iot: List[str] = Field(default_factory=list)


class ArchitectureFlow(BaseModel):
    """Step-by-step pipeline from input to output."""
    input_stage: str
    processing_stage: str
    decision_stage: str
    action_stage: str
    output_stage: str
    ascii_diagram: Optional[str] = None


class UserSegmentation(BaseModel):
    """Clear differentiation between user, buyer, and beneficiary."""
    users: str = Field(..., description="Operational users interacting with product")
    buyers: str = Field(..., description="Entities paying for the hardware/service")
    beneficiaries: str = Field(..., description="Communities or entities deriving ultimate value")


class MarketSize(BaseModel):
    """Bottom-up market sizing."""
    tam: str = Field(..., description="Total Addressable Market")
    sam: str = Field(..., description="Serviceable Addressable Market")
    som: str = Field(..., description="Serviceable Obtainable Market (3-year target)")
    methodology: str = Field(..., description="Bottom-up derivation methodology")
    assumptions: List[str] = Field(default_factory=list)


class BusinessModel(BaseModel):
    """Commercial mechanics and revenue streams."""
    who_pays: str
    what_they_pay_for: str
    pricing_model: str
    hardware_revenue: str
    recurring_revenue: str
    classification: str = Field(..., description="B2B, B2G, B2B2C, etc.")


class CompetitorComparison(BaseModel):
    """Direct competitive benchmarking."""
    competitor_name: str
    category: str = Field(..., description="Direct startup, incumbent, open source, or manual")
    strengths: str
    weaknesses: str
    our_advantage: str


class PrototypeSpec(BaseModel):
    """Student-buildable prototype specifications."""
    components: List[str]
    technologies: List[str]
    budget_inr: int = Field(..., description="Total estimated prototype cost in INR")
    budget_range: str
    complexity: str = Field(..., description="Low, Medium, High")
    required_skills: List[str]
    expected_dev_time_weeks: int


class DemoScript(BaseModel):
    """Live pitch demonstration steps."""
    setup: str
    live_action: str
    measurable_result: str
    judge_takeaway: str


class PilotRoadmap(BaseModel):
    """Milestones from campus to national scale."""
    stage_1_college_jagdalpur: str
    stage_2_bastar: str
    stage_3_chhattisgarh: str
    stage_4_national: str
    first_pilot_users: List[str]


class FinancialProjection(BaseModel):
    """Conservative 3-year revenue projections."""
    year_1: str
    year_2: str
    year_3: str
    assumptions: List[str] = Field(default_factory=list)


class GrantOpportunity(BaseModel):
    """Target institutional grants, schemes, and competitions."""
    scheme_name: str
    agency: str
    grant_amount: str
    qualification_rationale: str


class RiskFactor(BaseModel):
    """Key risks and pragmatic mitigations."""
    category: str = Field(..., description="Technical, Market, Regulatory, Adoption, etc.")
    risk_description: str
    mitigation_strategy: str


class ScalabilityPath(BaseModel):
    """Venture evolution trajectory."""
    prototype_to_pilot: str
    pilot_to_product: str
    product_to_company: str


class PitchPotential(BaseModel):
    """Competition and hackathon winning traits."""
    severity_and_novelty: str
    technical_depth: str
    demonstrability_and_impact: str


class BOMItem(BaseModel):
    """Component line item for prototype bill of materials."""
    item: str
    specification: str
    quantity: int
    unit_cost_inr: int
    source_vendor: str
    total_cost_inr: int


class StartupIdea(BaseModel):
    """Complete 18-part startup dossier."""
    id: str
    number: int
    name: str
    sector: str
    pitch: str
    problem: ProblemStatement
    solution: SolutionSpec
    how_it_works: ArchitectureFlow
    target_users: UserSegmentation
    market_opportunity: MarketSize
    business_model: BusinessModel
    competitive_analysis: List[CompetitorComparison]
    unique_advantage: str
    prototype: PrototypeSpec
    demonstration: DemoScript
    pilot_plan: PilotRoadmap
    revenue_projection: FinancialProjection
    funding_opportunities: List[GrantOpportunity]
    risks: List[RiskFactor]
    scalability: ScalabilityPath
    award_pitch_potential: PitchPotential


class EvaluationMetric(BaseModel):
    """Scoring for a single venture across standardized criteria."""
    idea_id: str
    name: str
    problem_severity: float  # 1-10
    existing_demand: float
    prototype_feasibility: float
    student_team_feasibility: float
    market_scalability: float
    competitive_differentiation: float
    revenue_potential: float
    social_environmental_impact: float
    competition_potential: float
    local_pilot_feasibility: float
    grant_csr_potential: float
    technical_defensibility: float
    regulatory_simplicity: float  # 10 = low regulatory friction
    capital_efficiency: float      # 10 = low capex needed
    composite_score: float = 0.0

    def calculate_composite(self, weights: Optional[Dict[str, float]] = None) -> float:
        """Calculate weighted composite score."""
        w = weights or {
            "problem_severity": 0.12,
            "existing_demand": 0.10,
            "prototype_feasibility": 0.12,
            "student_team_feasibility": 0.08,
            "market_scalability": 0.08,
            "competitive_differentiation": 0.08,
            "revenue_potential": 0.07,
            "social_environmental_impact": 0.07,
            "competition_potential": 0.07,
            "local_pilot_feasibility": 0.06,
            "grant_csr_potential": 0.05,
            "technical_defensibility": 0.05,
            "regulatory_simplicity": 0.03,
            "capital_efficiency": 0.02,
        }
        total = (
            self.problem_severity * w["problem_severity"]
            + self.existing_demand * w["existing_demand"]
            + self.prototype_feasibility * w["prototype_feasibility"]
            + self.student_team_feasibility * w["student_team_feasibility"]
            + self.market_scalability * w["market_scalability"]
            + self.competitive_differentiation * w["competitive_differentiation"]
            + self.revenue_potential * w["revenue_potential"]
            + self.social_environmental_impact * w["social_environmental_impact"]
            + self.competition_potential * w["competition_potential"]
            + self.local_pilot_feasibility * w["local_pilot_feasibility"]
            + self.grant_csr_potential * w["grant_csr_potential"]
            + self.technical_defensibility * w["technical_defensibility"]
            + self.regulatory_simplicity * w["regulatory_simplicity"]
            + self.capital_efficiency * w["capital_efficiency"]
        )
        self.composite_score = round(total, 2)
        return self.composite_score


class StartupBlueprint(BaseModel):
    """Full deep-dive startup blueprint for finalists (Sections A-N)."""
    idea_id: str
    name: str
    tagline: str
    pitch_30s: str
    pitch_2min: str
    pitch_5min_structure: Dict[str, str]
    prototype_architecture: Dict[str, Any]
    bill_of_materials: List[BOMItem]
    total_bom_cost_inr: int
    execution_roadmap_30_60_90: Dict[str, List[str]]
    first_customer_acquisition: List[str]
    business_model_deep_dive: Dict[str, str]
    scaleup_roadmap: Dict[str, str]
    major_technical_risks: List[str]
    major_business_risks: List[str]
    patent_ip_possibilities: List[str]
    grant_incubator_pathway: List[str]


class EliminatedIdea(BaseModel):
    """Concept rejected during preliminary screening."""
    id: str
    name: str
    category: str
    proposed_concept: str
    rejection_reasons: List[str]
    fatal_flaws: List[str]
