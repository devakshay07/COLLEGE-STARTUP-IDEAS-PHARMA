"""Unit tests for FinancialEngine."""

import pytest
from bastar_innovate.financials import FinancialEngine


def test_unit_economics_calculation():
    """Verify gross profit, margin, and payback period calculation."""
    ue = FinancialEngine.calculate_unit_economics(
        sale_price=24500.0,
        cogs=14800.0,
        cac=1500.0,
        recurring_annual=1800.0,
    )
    assert ue.gross_profit_inr == 9700.0
    assert 39.0 <= ue.gross_margin_percent <= 40.0
    assert ue.payback_period_months > 0.0
    assert ue.payback_period_months < 3.0


def test_pro_forma_generation():
    """Verify 3-year pro-forma calculations and breakeven units."""
    pf = FinancialEngine.generate_pro_forma(
        idea_id="mahuashilp",
        idea_name="MahuaShilp",
        unit_price=24500.0,
        cogs=14800.0,
        y1_units=40,
        y2_units=180,
        y3_units=600,
        fixed_opex_y1=500000.0,
        fixed_opex_y2=1200000.0,
        fixed_opex_y3=2800000.0,
        grant_target=2500000.0,
    )
    assert pf.year_1_revenue_inr == 24500.0 * 40
    assert pf.year_1_cogs_inr == 14800.0 * 40
    assert pf.year_2_revenue_inr == 24500.0 * 180
    assert pf.year_3_revenue_inr == 24500.0 * 600
    assert pf.year_3_ebitda_inr > 0
    assert pf.breakeven_units_per_year > 0
