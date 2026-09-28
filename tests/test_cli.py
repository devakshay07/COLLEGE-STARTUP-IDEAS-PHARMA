"""Integration tests for Click CLI interface."""

from click.testing import CliRunner
import pytest
from bastar_innovate.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_list(runner):
    """Test 'list' command output."""
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "MahuaShilp" in result.output
    assert "HemoPoint" in result.output
    assert "20 Curated Ventures" in result.output


def test_cli_list_filter_sector(runner):
    """Test filtering by sector in CLI."""
    result = runner.invoke(cli, ["list", "--sector", "Health"])
    assert result.exit_code == 0
    assert "HemoPoint" in result.output
    assert "BiliStrip" in result.output


def test_cli_detail(runner):
    """Test 'detail' command for an idea."""
    result = runner.invoke(cli, ["detail", "hemopoint"])
    assert result.exit_code == 0
    assert "HemoPoint" in result.output
    assert "Problem Statement" in result.output
    assert "Technical Solution Specification" in result.output


def test_cli_detail_invalid_id(runner):
    """Test 'detail' command with invalid ID exits with error."""
    result = runner.invoke(cli, ["detail", "invalid_id_xyz"])
    assert result.exit_code == 1
    assert "not found" in result.output


def test_cli_rank(runner):
    """Test 'rank' command."""
    result = runner.invoke(cli, ["rank", "--by", "composite", "--top", "5"])
    assert result.exit_code == 0
    assert "Venture Rankings" in result.output
    assert "#1" in result.output


def test_cli_blueprint(runner):
    """Test 'blueprint' command for flagship."""
    result = runner.invoke(cli, ["blueprint", "mahuashilp"])
    assert result.exit_code == 0
    assert "FLAGSHIP BLUEPRINT" in result.output
    assert "Bill of Materials" in result.output
    assert "30-60-90 Day" in result.output


def test_cli_compare(runner):
    """Test 'compare' command."""
    result = runner.invoke(cli, ["compare", "hemopoint", "ferroclear"])
    assert result.exit_code == 0
    assert "Head-to-Head Comparison" in result.output
    assert "Composite Score" in result.output


def test_cli_grants(runner):
    """Test 'grants' command."""
    result = runner.invoke(cli, ["grants", "conveyorguard"])
    assert result.exit_code == 0
    assert "Grant Matching" in result.output
    assert "Qualified Schemes" in result.output


def test_cli_financials(runner):
    """Test 'financials' command."""
    result = runner.invoke(cli, ["financials", "hemopoint"])
    assert result.exit_code == 0
    assert "Unit Economics" in result.output
    assert "Pro-Forma Income Statement" in result.output


def test_cli_eliminated(runner):
    """Test 'eliminated' command."""
    result = runner.invoke(cli, ["eliminated"])
    assert result.exit_code == 0
    assert "Rejected Concepts" in result.output
    assert "Smart Drone" in result.output


def test_cli_context(runner):
    """Test 'context' command."""
    result = runner.invoke(cli, ["context"])
    assert result.exit_code == 0
    assert "Jagdalpur" in result.output
    assert "Bastar" in result.output


def test_cli_export_json(runner):
    """Test 'export --format json' command."""
    result = runner.invoke(cli, ["export", "--format", "json"])
    assert result.exit_code == 0
    assert "mahuashilp" in result.output
