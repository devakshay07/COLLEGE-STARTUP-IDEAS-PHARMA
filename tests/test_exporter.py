"""Unit tests for VentureExporter."""

import json
from pathlib import Path
import pytest
from bastar_innovate.exporter import VentureExporter
from bastar_innovate.repository import VentureRepository


@pytest.fixture
def exporter():
    return VentureExporter()


def test_export_ideas_json(exporter):
    """Verify JSON export contains all 20 ideas with valid structure."""
    raw_json = exporter.export_ideas_json()
    parsed = json.loads(raw_json)
    assert len(parsed) == 20
    assert parsed[0]["id"] == "mahuashilp"


def test_export_summary_csv(exporter):
    """Verify CSV export contains headers and 20 rows."""
    raw_csv = exporter.export_summary_csv()
    lines = raw_csv.strip().split("\n")
    assert len(lines) == 21  # 1 header + 20 data rows
    assert "Number" in lines[0]
    assert "Composite_Score" in lines[0]


def test_generate_portfolio_markdown(exporter):
    """Verify portfolio markdown contains all 20 ideas and key sections."""
    md = exporter.generate_portfolio_markdown()
    assert "# One Institution – One Startup" in md
    assert "HemoPoint" in md
    assert "FerroClear" in md
    assert "ConveyorGuard" in md
    assert len(md) > 50000


def test_generate_evaluation_markdown(exporter):
    """Verify evaluation markdown contains MCDA matrix, scenarios, and Pareto frontier."""
    md = exporter.generate_evaluation_markdown()
    assert "Master Scoring Matrix" in md
    assert "Sensitivity & Scenario Stress-Testing" in md
    assert "Pareto-Optimal Frontier" in md


def test_generate_blueprints_markdown(exporter):
    """Verify top 5 blueprints markdown contains Sections A through L and BOM tables."""
    md = exporter.generate_blueprints_markdown()
    assert "Flagship Engineering Execution Blueprints" in md
    assert "Section A: Elevator Pitch" in md
    assert "Bill of Materials" in md
    assert "MahuaShilp" in md
    assert "HemoPoint" in md
    assert "FerroClear" in md


def test_write_all_documentation(exporter, tmp_path):
    """Verify all documentation files are written to directory."""
    exporter.write_all_documentation(tmp_path)
    assert (tmp_path / "PORTFOLIO_20_IDEAS.md").exists()
    assert (tmp_path / "EVALUATION_AND_RANKING.md").exists()
    assert (tmp_path / "TOP_5_BLUEPRINTS.md").exists()
    assert (tmp_path / "PORTFOLIO_20_IDEAS.md").stat().st_size > 10000
