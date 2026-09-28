"""Tests for Streamlit Web Dashboard and Data Loaders."""

from pathlib import Path
import pytest
from streamlit.testing.v1 import AppTest

from bastar_innovate.dashboard import load_all_dashboard_data, load_json_file

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RUN_SCRIPT = BASE_DIR / "run_dashboard.py"


def test_load_json_file():
    """Verify loading single JSON files."""
    context = load_json_file("bastar_context.json", DATA_DIR)
    assert "region" in context
    assert "geography" in context
    assert context["geography"]["headquarters"] == "Jagdalpur"


def test_load_json_file_missing(tmp_path):
    """Verify FileNotFoundError on missing file."""
    with pytest.raises(FileNotFoundError):
        load_json_file("non_existent_file.json", tmp_path)


def test_load_all_dashboard_data():
    """Verify all dashboard datasets are loaded."""
    data = load_all_dashboard_data(DATA_DIR)
    assert "context" in data
    assert "eliminated" in data
    assert "grants" in data
    assert "ideas" in data

    assert len(data["eliminated"]) == 5
    assert len(data["grants"]) >= 8
    assert len(data["ideas"]) == 20


def test_dashboard_app_execution():
    """Verify Streamlit app runs without any unhandled exceptions."""
    at = AppTest.from_file(str(RUN_SCRIPT), default_timeout=20)
    at.run()

    # Verify no exceptions
    assert not at.exception, f"App raised exceptions: {at.exception}"

    # Verify tabs exist
    assert len(at.tabs) > 0


def test_dashboard_ecosystem_metrics():
    """Verify Ecosystem tab renders expected st.metric cards."""
    at = AppTest.from_file(str(RUN_SCRIPT), default_timeout=20)
    at.run()

    metric_labels = [m.label for m in at.metric]
    metric_values = [m.value for m in at.metric]

    assert "Forest Cover" in metric_labels
    assert "62.4%" in metric_values
    assert "Tribal Population" in metric_labels
    assert "65.8%" in metric_values


def test_dashboard_fatal_flaws_in_red_warnings():
    """Verify Eliminated Concepts tab displays fatal flaws in red st.error warnings."""
    at = AppTest.from_file(str(RUN_SCRIPT), default_timeout=20)
    at.run()

    # The app renders fatal flaws using st.error
    assert len(at.error) >= 10  # At least 10 fatal flaws across 5 rejected concepts
    error_texts = [e.value for e in at.error]
    assert any("FATAL FLAW" in t for t in error_texts)
    assert any("Regulatory/Security Barrier" in t or "ARAI" in t or "Pure Software" in t for t in error_texts)


def test_dashboard_expanders():
    """Verify ground challenges and details are enclosed in expanders."""
    at = AppTest.from_file(str(RUN_SCRIPT), default_timeout=20)
    at.run()

    assert len(at.expander) >= 5
    expander_labels = [exp.label for exp in at.expander]
    assert any("Healthcare" in l for l in expander_labels)
    assert any("Water" in l for l in expander_labels)
    assert any("Post-Harvest" in l for l in expander_labels)
