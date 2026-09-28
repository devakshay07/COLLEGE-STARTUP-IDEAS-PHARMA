"""Financial modeling and unit economics engine for Bastar startup ventures."""

from __future__ import annotations

from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class UnitEconomics(BaseModel):
    """Detailed unit economics for a hardware or service product."""
    unit_sale_price_inr: float
    cogs_inr: float
    gross_profit_inr: float
    gross_margin_percent: float
    customer_acquisition_cost_inr: float
    payback_period_months: float
    annual_recurring_revenue_per_unit_inr: float


class ThreeYearFinancialModel(BaseModel):
    """Detailed 3-year revenue, cost, and profitability trajectory."""
    idea_id: str
    idea_name: str
    year_1_units: int
    year_1_revenue_inr: float
    year_1_cogs_inr: float
    year_1_opex_inr: float
    year_1_ebitda_inr: float
    year_2_units: int
    year_2_revenue_inr: float
    year_2_cogs_inr: float
    year_2_opex_inr: float
    year_2_ebitda_inr: float
    year_3_units: int
    year_3_revenue_inr: float
    year_3_cogs_inr: float
    year_3_opex_inr: float
    year_3_ebitda_inr: float
    breakeven_units_per_year: int
    grant_funding_target_inr: float


class FinancialEngine:
    """Calculates standardized financial metrics and generates pro-forma models."""

    @staticmethod
    def calculate_unit_economics(
        sale_price: float,
        cogs: float,
        cac: float = 1500.0,
        recurring_annual: float = 1200.0,
    ) -> UnitEconomics:
        """Derive margins, payback, and profitability on a per-unit basis."""
        gross_profit = sale_price - cogs
        margin_pct = round((gross_profit / sale_price) * 100, 1) if sale_price > 0 else 0.0
        # Payback period in months = CAC / (gross profit per month from hardware + monthly recurring)
        monthly_contribution = (gross_profit / 12.0) + (recurring_annual / 12.0)
        payback_months = round(cac / monthly_contribution, 1) if monthly_contribution > 0 else 0.0

        return UnitEconomics(
            unit_sale_price_inr=sale_price,
            cogs_inr=cogs,
            gross_profit_inr=gross_profit,
            gross_margin_percent=margin_pct,
            customer_acquisition_cost_inr=cac,
            payback_period_months=payback_months,
            annual_recurring_revenue_per_unit_inr=recurring_annual,
        )

    @classmethod
    def generate_pro_forma(
        cls,
        idea_id: str,
        idea_name: str,
        unit_price: float,
        cogs: float,
        y1_units: int,
        y2_units: int,
        y3_units: int,
        fixed_opex_y1: float = 600000.0,
        fixed_opex_y2: float = 1500000.0,
        fixed_opex_y3: float = 3500000.0,
        grant_target: float = 2500000.0,
    ) -> ThreeYearFinancialModel:
        """Construct full 3-year pro-forma income statement."""
        unit_gross_profit = unit_price - cogs
        breakeven_units = int(fixed_opex_y2 / unit_gross_profit) if unit_gross_profit > 0 else 0

        y1_rev = unit_price * y1_units
        y1_cogs = cogs * y1_units
        y1_ebitda = y1_rev - y1_cogs - fixed_opex_y1

        y2_rev = unit_price * y2_units
        y2_cogs = cogs * y2_units
        y2_ebitda = y2_rev - y2_cogs - fixed_opex_y2

        y3_rev = unit_price * y3_units
        y3_cogs = cogs * y3_units
        y3_ebitda = y3_rev - y3_cogs - fixed_opex_y3

        return ThreeYearFinancialModel(
            idea_id=idea_id,
            idea_name=idea_name,
            year_1_units=y1_units,
            year_1_revenue_inr=y1_rev,
            year_1_cogs_inr=y1_cogs,
            year_1_opex_inr=fixed_opex_y1,
            year_1_ebitda_inr=y1_ebitda,
            year_2_units=y2_units,
            year_2_revenue_inr=y2_rev,
            year_2_cogs_inr=y2_cogs,
            year_2_opex_inr=fixed_opex_y2,
            year_2_ebitda_inr=y2_ebitda,
            year_3_units=y3_units,
            year_3_revenue_inr=y3_rev,
            year_3_cogs_inr=y3_cogs,
            year_3_opex_inr=fixed_opex_y3,
            year_3_ebitda_inr=y3_ebitda,
            breakeven_units_per_year=breakeven_units,
            grant_funding_target_inr=grant_target,
        )
