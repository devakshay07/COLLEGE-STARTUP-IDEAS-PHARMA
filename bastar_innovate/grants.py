"""Matching engine for Indian government grants, innovation schemes, and CSR funds."""

from __future__ import annotations

from typing import Dict, List, Optional
from pydantic import BaseModel
from bastar_innovate.models import StartupIdea
from bastar_innovate.repository import VentureRepository


class SchemeMatch(BaseModel):
    """Grant scheme match result for a startup venture."""
    scheme_id: str
    scheme_name: str
    agency: str
    grant_amount_formatted: str
    grant_amount_max_inr: int
    match_score: float  # 0.0 to 1.0
    rationale: str
    key_action_items: List[str]


class GrantMatcher:
    """Matches startup concepts with central, state, and district funding programs."""

    def __init__(self, repository: Optional[VentureRepository] = None):
        self.repo = repository or VentureRepository()
        self.grants = self.repo.get_grants_data()

    def match_idea(self, idea: StartupIdea) -> List[SchemeMatch]:
        """Find and rank all grant schemes applicable to an idea."""
        matches: List[SchemeMatch] = []
        sector_lower = idea.sector.lower()
        desc_lower = (idea.pitch + " " + idea.solution.description + " " + idea.problem.consequence_if_unsolved).lower()

        for g in self.grants:
            score = 0.5  # Base eligibility for innovative student venture
            rationale_points: List[str] = []
            action_items: List[str] = [
                "Draft 10-page executive DPR (Detailed Project Report)",
                "Secure institutional endorsement letter from College Principal / R&D Dean",
            ]

            # Match domains
            domains = [d.lower() for d in g.get("eligible_domains", [])]
            for dom in domains:
                if dom in sector_lower or dom in desc_lower:
                    score += 0.15
                    rationale_points.append(f"Direct alignment with scheme priority domain: '{dom.title()}'")
                    break

            # Bastar specific match
            if g["id"] == "bastar_dmf":
                if any(k in desc_lower for k in ["tribal", "school", "water", "health", "forest", "mine", "amputee"]):
                    score += 0.25
                    rationale_points.append("Direct alignment with Bastar DMF high-priority sector mandate")
                    action_items.append("Submit proposal directly to Bastar District Collectorate & DMF Trust Officer")

            # BIRAC MedTech / Bio match
            if g["id"] == "birac_big":
                if any(k in sector_lower for k in ["health", "medtech", "waste", "bio"]):
                    score += 0.25
                    rationale_points.append("Qualifies for BIRAC Biotechnology Ignition Grant under MedTech/Industrial Biotech")
                    action_items.append("Partner with an approved BIRAC BioNEST incubator (e.g., KIIT-TBI or IKP Knowledge Park)")

            # DST NIDHI PRAYAS hardware match
            if g["id"] == "dst_nidhi_prayas":
                if idea.prototype.budget_inr <= 1000000:
                    score += 0.2
                    rationale_points.append("Hardware prototype within ₹10 Lakhs ceiling with physical demonstrable component")
                    action_items.append("Apply through nearest PRAYAS Centre (e.g., 36Inc Raipur or IIT Bhilai TIH)")

            # MeitY TIDE 2.0 edge AI / IoT match
            if g["id"] == "meity_tide":
                if any(k in desc_lower for k in ["iot", "radar", "camera", "vision", "speech", "sensor", "tiny"]):
                    score += 0.2
                    rationale_points.append("Strong ICT/IoT/Edge AI embedded hardware architecture")
                    action_items.append("Submit under TIDE 2.0 G2C / Smart Automation call")

            # MSME Hackathon
            if g["id"] == "msme_hackathon":
                score += 0.15
                rationale_points.append("Eligible for Host Institute student innovator submission (up to ₹15 Lakhs)")

            # NMDC CSR match
            if g["id"] == "nmdc_csr":
                if any(k in desc_lower or k in sector_lower for k in ["mining", "mine", "steel", "conveyor", "smelting", "foundry", "craft", "water"]):
                    score += 0.25
                    rationale_points.append("Direct operational relevance to NMDC Nagarnar Steel or Bailadila iron ore operations")
                    action_items.append("Submit proposal to NMDC CSR & R&D Cell, Kirandul / Nagarnar")

            score = min(round(score, 2), 0.98)
            if score >= 0.65:
                match_text = "; ".join(rationale_points) if rationale_points else g.get("relevance", "")
                matches.append(
                    SchemeMatch(
                        scheme_id=g["id"],
                        scheme_name=g["name"],
                        agency=g["agency"],
                        grant_amount_formatted=g["grant_amount_formatted"],
                        grant_amount_max_inr=g["grant_amount_max_inr"],
                        match_score=score,
                        rationale=match_text,
                        key_action_items=action_items,
                    )
                )

        return sorted(matches, key=lambda x: x.match_score, reverse=True)

    def total_grant_potential(self, idea: StartupIdea) -> Dict[str, Any]:
        """Compute aggregated grant funding pipeline for a venture."""
        matches = self.match_idea(idea)
        total_max_inr = sum(m.grant_amount_max_inr for m in matches)
        top_3 = matches[:3]
        return {
            "idea_id": idea.id,
            "idea_name": idea.name,
            "qualified_schemes_count": len(matches),
            "top_schemes": [m.scheme_name for m in top_3],
            "total_potential_pipeline_inr": total_max_inr,
            "formatted_pipeline": f"₹{total_max_inr / 100000:.1f} Lakhs",
        }
