#!/usr/bin/env python3
"""Entrypoint for the Bastar Innovation Streamlit Web Dashboard.

Usage:
    streamlit run run_dashboard.py
    OR
    python3 run_dashboard.py
"""

import sys
from pathlib import Path

# Ensure package directory is on sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from bastar_innovate.dashboard import main

if __name__ == "__main__":
    from streamlit.runtime.scriptrunner import get_script_run_ctx

    if get_script_run_ctx() is None:
        import streamlit.web.cli as stcli
        sys.argv = ["streamlit", "run", str(Path(__file__).resolve())] + sys.argv[1:]
        sys.exit(stcli.main())
    else:
        main()
