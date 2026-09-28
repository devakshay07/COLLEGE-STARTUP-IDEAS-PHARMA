"""Exporters for generating markdown documentation, JSON, and CSV assets."""

from __future__ import annotations

import csv
import json
from io import StringIO
from pathlib import Path
from typing import Dict, List, Optional

from bastar_innovate.blueprints import get_flagship_blueprints
from bastar_innovate.evaluator import VentureEvaluator
from bastar_innovate.models import StartupIdea
from bastar_innovate.repository import VentureRepository


class VentureExporter:
    """Exports venture portfolios, evaluation tables, and deep-dive documentation."""

    def __init__(self, repository: Optional[VentureRepository] = None):
        self.repo = repository or VentureRepository()
        self.evaluator = VentureEvaluator(self.repo)

    def export_ideas_json(self) -> str:
        """Export all 20 ideas as formatted JSON string."""
        ideas = [idea.model_dump() for idea in self.repo.get_all_ideas()]
        return json.dumps(ideas, indent=2, ensure_ascii=False)

    def export_summary_csv(self) -> str:
        """Export summary table of 20 ideas as CSV."""
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow([
            "Number", "ID", "Name", "Sector", "Prototype_Budget_INR",
            "Complexity", "Composite_Score", "Problem_Severity",
            "Feasibility", "Impact", "Competition_Potential",
        ])

        for idea in self.repo.get_all_ideas():
            ev = self.repo.get_evaluation(idea.id)
            score = ev.composite_score if ev else 0.0
            sev = ev.problem_severity if ev else 0.0
            feas = ev.prototype_feasibility if ev else 0.0
            imp = ev.social_environmental_impact if ev else 0.0
            comp = ev.competition_potential if ev else 0.0

            writer.writerow([
                idea.number,
                idea.id,
                idea.name,
                idea.sector,
                idea.prototype.budget_inr,
                idea.prototype.complexity,
                score,
                sev,
                feas,
                imp,
                comp,
            ])

        return output.getvalue()

    def generate_portfolio_markdown(self) -> str:
        """Generate full comprehensive portfolio markdown document with all 20 ideas."""
        lines = [
            "# One Institution – One Startup: 20 Research-Backed Startup Ventures",
            "## B.Tech Engineering College, Jagdalpur, Bastar, Chhattisgarh",
            "",
            "> **Executive Initiative**: 'One Institution – One Startup'",
            "> **Focus**: Real-World Problem Solving, Student-Feasible Hardware Prototypes, Scalable Business Ventures",
            "",
            "---",
            "",
            "## Table of Contents",
            "",
        ]

        ideas = self.repo.get_all_ideas()
        for idea in ideas:
            ev = self.repo.get_evaluation(idea.id)
            score_text = f"(Score: {ev.composite_score}/10 | Budget: ₹{idea.prototype.budget_inr:,})" if ev else ""
            lines.append(f"- [{idea.number}. {idea.name}](#{idea.id}) - *{idea.sector}* {score_text}")

        lines.extend(["", "---", ""])

        for idea in ideas:
            ev = self.repo.get_evaluation(idea.id)
            lines.extend([
                f'<a id="{idea.id}"></a>',
                f"# Venture #{idea.number}: {idea.name}",
                f"**Sector**: {idea.sector}  ",
                f"**Prototype Budget**: ₹{idea.prototype.budget_inr:,} ({idea.prototype.budget_range}) | **Complexity**: {idea.prototype.complexity}  ",
                f"**Composite Viability Score**: {ev.composite_score if ev else 'N/A'}/10.0",
                "",
                "### 1. Executive Pitch",
                f"> {idea.pitch}",
                "",
                "### 2. Problem Statement",
                f"- **Target Population & Geography**: {idea.problem.target_affected}",
                f"- **Frequency & Occurrence**: {idea.problem.frequency}",
                f"- **Why Current Solutions Fail**: {idea.problem.why_existing_fail}",
                f"- **Consequences if Unsolved**: {idea.problem.consequence_if_unsolved}",
                "- **Evidence & Ground Citations**:",
            ])
            for cit in idea.problem.evidence_and_sources:
                lines.append(f"  - {cit}")

            lines.extend([
                "",
                "### 3. Solution Specification",
                f"{idea.solution.description}",
                "",
                "**Hardware Architecture**:",
            ])
            for hw in idea.solution.hardware:
                lines.append(f"- {hw}")

            lines.extend(["", "**Software & Firmware Stack**:"])
            for sw in idea.solution.software:
                lines.append(f"- {sw}")

            lines.extend(["", "**Edge AI / IoT & Algorithms**:"])
            for ai in idea.solution.ai_ml_iot:
                lines.append(f"- {ai}")

            lines.extend([
                "",
                "### 4. Technical Architecture & End-to-End Pipeline",
                f"- **Input Stage**: {idea.how_it_works.input_stage}",
                f"- **Processing Stage**: {idea.how_it_works.processing_stage}",
                f"- **Decision Stage**: {idea.how_it_works.decision_stage}",
                f"- **Action Stage**: {idea.how_it_works.action_stage}",
                f"- **Output Stage**: {idea.how_it_works.output_stage}",
                "",
                "```text",
                f"{idea.how_it_works.ascii_diagram or ''}",
                "```",
                "",
                "### 5. Target Users, Buyers & Beneficiaries",
                f"- **Operational Users**: {idea.target_users.users}",
                f"- **Economic Buyers**: {idea.target_users.buyers}",
                f"- **Societal Beneficiaries**: {idea.target_users.beneficiaries}",
                "",
                "### 6. Market Opportunity (Bottom-Up Analysis)",
                f"- **Total Addressable Market (TAM)**: {idea.market_opportunity.tam}",
                f"- **Serviceable Addressable Market (SAM)**: {idea.market_opportunity.sam}",
                f"- **Serviceable Obtainable Market (SOM - 3 Year)**: {idea.market_opportunity.som}",
                f"- **Derivation Methodology**: {idea.market_opportunity.methodology}",
                "",
                "### 7. Business Model & Revenue Mechanics",
                f"- **Who Pays**: {idea.business_model.who_pays}",
                f"- **What They Pay For**: {idea.business_model.what_they_pay_for}",
                f"- **Pricing Model**: {idea.business_model.pricing_model}",
                f"- **Hardware Revenue Stream**: {idea.business_model.hardware_revenue}",
                f"- **Recurring Revenue Stream**: {idea.business_model.recurring_revenue}",
                f"- **Classification**: {idea.business_model.classification}",
                "",
                "### 8. Competitive Benchmarking",
                "| Competitor / Alternative | Category | Strengths | Weaknesses | Our Defensible Advantage |",
                "|---|---|---|---|---|",
            ])
            for comp in idea.competitive_analysis:
                lines.append(f"| {comp.competitor_name} | {comp.category} | {comp.strengths} | {comp.weaknesses} | {comp.our_advantage} |")

            lines.extend([
                "",
                f"**Unique Defensible Advantage**: {idea.unique_advantage}",
                "",
                "### 9. Student-Buildable Prototype Specifications",
                f"- **Estimated Prototype Budget**: ₹{idea.prototype.budget_inr:,} ({idea.prototype.budget_range})",
                f"- **Technical Complexity**: {idea.prototype.complexity}",
                f"- **Expected Development Timeline**: {idea.prototype.expected_dev_time_weeks} weeks",
                f"- **Required Student Skills**: {', '.join(idea.prototype.required_skills)}",
                "- **Key Hardware Components**:",
            ])
            for comp in idea.prototype.components:
                lines.append(f"  - {comp}")

            lines.extend([
                "",
                "### 10. Live Competition Demonstration Script",
                f"- **Physical Demo Setup**: {idea.demonstration.setup}",
                f"- **Live 60-Second Action**: {idea.demonstration.live_action}",
                f"- **Measurable Output on Stage**: {idea.demonstration.measurable_result}",
                f"- **Judge Takeaway**: {idea.demonstration.judge_takeaway}",
                "",
                "### 11. Campus to National Pilot Roadmap",
                f"- **Stage 1 (Campus Lab & Jagdalpur)**: {idea.pilot_plan.stage_1_college_jagdalpur}",
                f"- **Stage 2 (Bastar District Field Trials)**: {idea.pilot_plan.stage_2_bastar}",
                f"- **Stage 3 (Chhattisgarh State Rollout)**: {idea.pilot_plan.stage_3_chhattisgarh}",
                f"- **Stage 4 (National Scaling)**: {idea.pilot_plan.stage_4_national}",
                f"- **First Pilot Partners**: {', '.join(idea.pilot_plan.first_pilot_users)}",
                "",
                "### 12. Conservative 3-Year Financial Projections",
                f"- **Year 1**: {idea.revenue_projection.year_1}",
                f"- **Year 2**: {idea.revenue_projection.year_2}",
                f"- **Year 3**: {idea.revenue_projection.year_3}",
                "- **Key Pro-Forma Assumptions**:",
            ])
            for ass in idea.revenue_projection.assumptions:
                lines.append(f"  - {ass}")

            lines.extend([
                "",
                "### 13. Institutional Grants & Schemes",
            ])
            for gr in idea.funding_opportunities:
                lines.append(f"- **{gr.scheme_name}** ({gr.agency}) - **{gr.grant_amount}**: {gr.qualification_rationale}")

            lines.extend([
                "",
                "### 14. Key Risks & Pragmatic Mitigations",
            ])
            for rk in idea.risks:
                lines.append(f"- **{rk.category}**: {rk.risk_description}  \n  *Mitigation*: {rk.mitigation_strategy}")

            lines.extend([
                "",
                "### 15. Venture Scalability Trajectory",
                f"- **Prototype to Pilot**: {idea.scalability.prototype_to_pilot}",
                f"- **Pilot to Product**: {idea.scalability.pilot_to_product}",
                f"- **Product to Company**: {idea.scalability.product_to_company}",
                "",
                "### 16. Award & Hackathon Winning Potential",
                f"- **Severity & Novelty**: {idea.award_pitch_potential.severity_and_novelty}",
                f"- **Technical Depth**: {idea.award_pitch_potential.technical_depth}",
                f"- **Stage Demonstrability**: {idea.award_pitch_potential.demonstrability_and_impact}",
                "",
                "---",
                "",
            ])

        return "\n".join(lines)

    def generate_evaluation_markdown(self) -> str:
        """Generate evaluation matrix and ranking documentation."""
        lines = [
            "# Venture Evaluation, Selection Methodology & Multi-Criteria Ranking",
            "## Bastar Innovation Venture Intelligence Engine",
            "",
            "---",
            "",
            "## 1. Internal Screening & Idea Elimination Process",
            "",
            "To ensure only rigorous, defensible, and realistic startup opportunities were shortlisted, "
            "a broad initial pool of concepts was evaluated against strict feasibility, regulatory, and commercial criteria. "
            "The following five concepts were formally eliminated during preliminary review:",
            "",
            "| Concept Name | Category | Fatal Flaws Identified | Rejection Rationale |",
            "|---|---|---|---|",
        ]

        for elim in self.repo.get_eliminated_ideas():
            flaws = ", ".join(elim.fatal_flaws)
            reasons = " ".join(elim.rejection_reasons)
            lines.append(f"| **{elim.name}** | {elim.category} | `{flaws}` | {reasons} |")

        lines.extend([
            "",
            "---",
            "",
            "## 2. Standardized Multi-Criteria Decision Analysis (MCDA) Scoring",
            "",
            "All 20 candidate ventures were scored across 14 standardized dimensions on a 1.0 to 10.0 scale. "
            "The composite score is derived using a weighted linear combination reflecting hackathon-winning "
            "potential, ground feasibility, and enterprise sustainability.",
            "",
            "### Weight Distribution Across Dimensions",
            "- **Problem Severity**: 12% (Is the problem life-threatening or economically catastrophic?)",
            "- **Prototype Feasibility**: 12% (Can a student team build a functioning physical prototype for <₹25,000?)",
            "- **Existing Demand**: 10% (Are buyers actively seeking solutions or losing money?)",
            "- **Student Team Feasibility**: 8% (Can B.Tech engineering students execute the skills?)",
            "- **Market Scalability**: 8% (Can this scale from Bastar across Central India and nationally?)",
            "- **Competitive Differentiation**: 8% (Does it have an insurmountable moat over existing alternatives?)",
            "- **Revenue Potential**: 8% (Is the business model profitable and sustainable?)",
            "- **Social/Environmental Impact**: 8% (Does it create measurable livelihood or ecological impact?)",
            "- **Competition/Hackathon Potential**: 7% (Will this blow judges away in 5 minutes on stage?)",
            "- **Local Pilot Feasibility**: 7% (Can the first pilot happen right here in Bastar/Jagdalpur?)",
            "- **Grant/CSR Potential**: 5% (Can it tap into Bastar DMF, DST PRAYAS, BIRAC BIG, or NMDC CSR?)",
            "- **Technical Defensibility**: 5% (Is there real engineering, or is it an easily copied app?)",
            "- **Regulatory Simplicity**: 4% (Can it be deployed without years of red tape?)",
            "- **Capital Efficiency**: 3% (Can the venture reach cash flow breakeven on modest seed capital?)",
            "",
            "### Master Scoring Matrix (All 20 Ventures)",
            "",
            "| Rank | Venture ID | Name | Sector | Composite (Max 10) | Severity | Feasibility | Demand | Impact | Competition | Budget (INR) |",
            "|---|---|---|---|---|---|---|---|---|---|---|",
        ])

        ranked = self.evaluator.rank_ideas(sort_by="composite")
        for rank_idx, (idea, ev) in enumerate(ranked, 1):
            lines.append(
                f"| **#{rank_idx}** | `{idea.id}` | **{idea.name.split(':')[0]}** | {idea.sector} | "
                f"**{ev.composite_score:.2f}** | {ev.problem_severity} | {ev.prototype_feasibility} | "
                f"{ev.existing_demand} | {ev.social_environmental_impact} | {ev.competition_potential} | "
                f"₹{idea.prototype.budget_inr:,} |"
            )

        lines.extend([
            "",
            "---",
            "",
            "## 3. Sensitivity & Scenario Stress-Testing",
            "",
            "To verify that rankings are resilient across diverse institutional goals, we ran sensitivity scenarios:",
            "",
        ])

        scenarios = self.evaluator.sensitivity_analysis()
        for scenario_name, top_ideas in scenarios.items():
            title = scenario_name.replace("_", " ").title()
            lines.append(f"### Scenario: {title}")
            for rank_pos, idea_title in enumerate(top_ideas, 1):
                lines.append(f"{rank_pos}. **{idea_title.split(':')[0]}**")
            lines.append("")

        lines.extend([
            "---",
            "",
            "## 4. Pareto-Optimal Frontier",
            "",
            "Non-dominated ventures maximizing **Prototype Feasibility**, **Societal Impact**, and **Competition Winning Potential**:",
            "",
        ])

        frontier = self.evaluator.pareto_frontier()
        for p_idea, p_ev in frontier:
            lines.append(
                f"- **{p_idea.name.split(':')[0]}** (`{p_idea.id}`): "
                f"Feasibility: {p_ev.prototype_feasibility} | Impact: {p_ev.social_environmental_impact} | "
                f"Competition: {p_ev.competition_potential} | Composite: {p_ev.composite_score}"
            )

        return "\n".join(lines)

    def generate_blueprints_markdown(self) -> str:
        """Generate detailed execution blueprints for top flagship contenders."""
        blueprints = get_flagship_blueprints()
        lines = [
            "# Flagship Engineering Execution Blueprints (Sections A to N)",
            "## Top 5 Student-Led Deep-Tech Ventures for Jagdalpur B.Tech Engineering College",
            "",
            "This document provides exhaustive, production-grade blueprints for the top 5 flagship ventures "
            "selected for immediate prototyping, institutional competition entry, and Bastar field pilot deployment.",
            "",
            "---",
            "",
        ]

        for idx, (b_id, bp) in enumerate(blueprints.items(), 1):
            lines.extend([
                f"# Flagship Contender #{idx}: {bp.name}",
                f"### *{bp.tagline}*",
                "",
                "## Section A: Elevator Pitch (30 Seconds)",
                f"> {bp.pitch_30s}",
                "",
                "## Section B: Formal 2-Minute Competition/Investor Pitch",
                f"{bp.pitch_2min}",
                "",
                "## Section C: 5-Minute Competition Pitch Deck Structure (Slide by Slide)",
            ])
            for slide, desc in bp.pitch_5min_structure.items():
                lines.append(f"- **{slide}**: {desc}")

            lines.extend([
                "",
                "## Section D: Complete Prototype Technical Architecture",
            ])
            for sub, desc in bp.prototype_architecture.items():
                lines.append(f"- **{sub.replace('_', ' ').title()}**: {desc}")

            lines.extend([
                "",
                f"## Section E: Itemized Bill of Materials (Total: ₹{bp.total_bom_cost_inr:,})",
                "| Component Item | Detailed Technical Specification | Qty | Unit Cost (INR) | Source / Vendor | Total Cost (INR) |",
                "|---|---|---|---|---|---|",
            ])
            for bom in bp.bill_of_materials:
                lines.append(f"| {bom.item} | {bom.specification} | {bom.quantity} | ₹{bom.unit_cost_inr:,} | {bom.source_vendor} | ₹{bom.total_cost_inr:,} |")

            lines.extend([
                "",
                "## Section F: 30-60-90 Day Execution Sprint Roadmap",
                "### Days 0 – 30 (Benchtop Prototyping & Lab Proof-of-Concept):",
            ])
            for item in bp.execution_roadmap_30_60_90.get("day_0_to_30", []):
                lines.append(f"- [ ] {item}")

            lines.extend(["", "### Days 31 – 60 (System Integration & Alpha Enclosure Assembly):"])
            for item in bp.execution_roadmap_30_60_90.get("day_31_to_60", []):
                lines.append(f"- [ ] {item}")

            lines.extend(["", "### Days 61 – 90 (Bastar Field Pilots, Lab Validation & Grant Filing):"])
            for item in bp.execution_roadmap_30_60_90.get("day_61_to_90", []):
                lines.append(f"- [ ] {item}")

            lines.extend([
                "",
                "## Section G: First Customer Acquisition Playbook (Bastar Local)",
            ])
            for ca in bp.first_customer_acquisition:
                lines.append(f"- {ca}")

            lines.extend([
                "",
                "## Section H: Commercial Business Model & Unit Economics Deep Dive",
            ])
            for bm_key, bm_val in bp.business_model_deep_dive.items():
                lines.append(f"- **{bm_key.replace('_', ' ').title()}**: {bm_val}")

            lines.extend([
                "",
                "## Section I: 3-Year Scale-Up Trajectory",
            ])
            for sc_yr, sc_desc in bp.scaleup_roadmap.items():
                lines.append(f"- **{sc_yr.replace('_', ' ').title()}**: {sc_desc}")

            lines.extend([
                "",
                "## Section J: Critical Technical & Operational Risks",
                "**Technical Vulnerabilities & Physics Constraints**:",
            ])
            for tr in bp.major_technical_risks:
                lines.append(f"- {tr}")

            lines.extend(["", "**Commercial & Adoption Risks**:"])
            for br in bp.major_business_risks:
                lines.append(f"- {br}")

            lines.extend([
                "",
                "## Section K: Intellectual Property & Patentable Claims",
            ])
            for ip in bp.patent_ip_possibilities:
                lines.append(f"- {ip}")

            lines.extend([
                "",
                "## Section L: Grant & Institutional Incubation Pathway",
            ])
            for gi in bp.grant_incubator_pathway:
                lines.append(f"- {gi}")

            lines.extend(["", "---", ""])

        return "\n".join(lines)

    def write_all_documentation(self, docs_dir: Path) -> None:
        """Write all documentation files to target directory."""
        docs_dir.mkdir(parents=True, exist_ok=True)

        portfolio_path = docs_dir / "PORTFOLIO_20_IDEAS.md"
        with open(portfolio_path, "w", encoding="utf-8") as f:
            f.write(self.generate_portfolio_markdown())

        eval_path = docs_dir / "EVALUATION_AND_RANKING.md"
        with open(eval_path, "w", encoding="utf-8") as f:
            f.write(self.generate_evaluation_markdown())

        bp_path = docs_dir / "TOP_5_BLUEPRINTS.md"
        with open(bp_path, "w", encoding="utf-8") as f:
            f.write(self.generate_blueprints_markdown())
