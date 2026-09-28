"""Streamlit Web Dashboard for the Bastar Innovation Venture Intelligence Engine.

Provides an executive presentation interface for B.Tech engineering college
faculty, mentors, and competition juries.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import streamlit as st

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@st.cache_data
def load_json_file(filename: str, data_dir: Optional[Path] = None) -> Any:
    """Load and parse JSON file from data directory."""
    target_dir = data_dir or DATA_DIR
    file_path = target_dir / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Required data file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all_dashboard_data(data_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Load all necessary JSON datasets."""
    return {
        "context": load_json_file("bastar_context.json", data_dir),
        "eliminated": load_json_file("eliminated_ideas.json", data_dir),
        "grants": load_json_file("grants_data.json", data_dir),
        "ideas": load_json_file("ideas_data.json", data_dir),
    }


def apply_custom_css():
    """Inject modern styling for presentation-ready UI."""
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 2.2rem;
            font-weight: 800;
            color: #1E293B;
            margin-bottom: 0.2rem;
        }
        .sub-header {
            font-size: 1.05rem;
            color: #64748B;
            margin-bottom: 1.5rem;
        }
        .badge {
            display: inline-block;
            padding: 0.25rem 0.6rem;
            font-size: 0.8rem;
            font-weight: 600;
            border-radius: 9999px;
            margin-right: 0.4rem;
            margin-bottom: 0.4rem;
        }
        .badge-sector {
            background-color: #E0F2FE;
            color: #0369A1;
        }
        .badge-grant {
            background-color: #DCFCE7;
            color: #15803D;
        }
        .badge-flaw {
            background-color: #FEE2E2;
            color: #991B1B;
            border: 1px solid #F87171;
            font-weight: 700;
        }
        .card {
            background-color: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 1.2rem;
            margin-bottom: 1rem;
        }
        .metric-container {
            border-left: 4px solid #3B82F6;
            padding-left: 10px;
            margin-bottom: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_ecosystem_tab(context: Dict[str, Any]):
    """Render Tab 1: Bastar Ecosystem (Geography, Demographics, Ground Challenges)."""
    st.markdown("### 🌳 Bastar Regional Operating Environment & Real-World Challenges")
    st.markdown(
        "*Empirical ground context of Jagdalpur and Bastar Division, grounding student engineering prototypes "
        "in severe local challenges rather than abstract classroom assumptions.*"
    )

    # 1. High-level metric cards
    col1, col2, col3, col4, col5 = st.columns(5)
    geography = context.get("geography", {})
    demo = context.get("demographics_and_economy", {})

    with col1:
        st.metric(
            label="Forest Cover",
            value="62.4%",
            help="Predominantly Sal (Shorea robusta), Teak, and mixed deciduous forests.",
        )
    with col2:
        st.metric(
            label="Tribal Population",
            value="65.8%",
            help="Scheduled Tribes: Gond, Maria, Muria, Dhurwa, Halba, Bhatra.",
        )
    with col3:
        st.metric(
            label="Major Trade Hub",
            value="Jagdalpur Mandi",
            help="One of Asia's largest minor forest produce and tamarind aggregation centers.",
        )
    with col4:
        st.metric(
            label="Industrial Nodes",
            value="NMDC Nagarnar",
            help="3 MTPA Integrated Steel Plant and Bailadila Iron Ore Mining Complex.",
        )
    with col5:
        st.metric(
            label="River Basins",
            value="Indravati & Sabari",
            help="Major perennial waterways feeding the Godavari river basin.",
        )

    st.markdown("---")

    # 2. Key Ground Realities & Geography
    col_geo, col_econ = st.columns([1, 1])

    with col_geo:
        st.markdown("#### 📍 Geography & Natural Landmarks")
        st.write(f"**Administrative Headquarters**: {geography.get('headquarters')} ({geography.get('coordinates')})")
        st.write(f"**State**: {context.get('state')}")
        st.write(f"**Major Rivers**: {', '.join(geography.get('major_rivers', []))}")
        st.write(f"**Forest Dominance**: {geography.get('forest_cover_percentage')}")
        st.write(f"**Key Eco-Landmarks**: {', '.join(geography.get('notable_landmarks', []))}")

    with col_econ:
        st.markdown("#### 💼 Economic Drivers & Livelihoods")
        st.write(f"**Tribal Demographic Share**: {demo.get('tribal_population_percentage')}")
        st.write("**Primary Forest Livelihoods**:")
        for lh in demo.get("primary_livelihoods", []):
            st.markdown(f"- {lh}")
        st.write("**Heavy Industrial Infrastructure**:")
        for ind in demo.get("industrial_nodes", []):
            st.markdown(f"- {ind}")

    st.markdown("---")

    # 3. Ground Challenges using Expanders (as requested)
    st.markdown("#### ⚠️ High-Priority Ground Challenges & Bottlenecks")
    challenges = context.get("ground_challenges", {})

    with st.expander("🩺 Healthcare Accessibility & Genetic Disease Burden", expanded=True):
        st.markdown(
            """
            - **Sickle Cell Disease / Trait Prevalence**: Estimated at **10% to 25%** in indigenous populations across central tribal belts. Field workers rely on visual solubility tests that fail to distinguish harmless carriers (HbAS) from lethal disease (HbSS).
            - **Vector-Borne & Toxic Hazards**: Hyper-endemic transmission of falciparum malaria and venomous snakebites (Russell's viper, krait) in deep forested valley habitations.
            - **Cold-Chain Breakdown**: Remote Sub-Health Centres (SHCs) experience 12 to 24-hour monsoon power outages, leading to compromised antivenom and rabies vaccines.
            - **Neonatal Hyperbilirubinemia**: Dark infant skin tone renders visual jaundice assessment completely unreliable, while imported bilirubinometers cost ₹2.5 to ₹4.5 Lakhs.
            """
        )
        if "health" in challenges:
            for item in challenges["health"]:
                st.info(f"📌 {item}")

    with st.expander("💧 Water Quality, Sanitation & Environmental Remediation", expanded=True):
        st.markdown(
            """
            - **Severe Geogenic Iron Contamination**: Hematitic geology results in groundwater iron levels of **3.0 to 12.0 mg/L** (BIS safe limit is 0.3 mg/L), poisoning school borewells and encrusting pipes.
            - **Solar Drinking Water Pump Failures**: Over 50,000 CREDA solar dual pumps installed in off-grid villages suffer motor burnout from unmonitored dry-running during pre-monsoon water table drops.
            - **Severe Forest Fire Hazards**: Gatherers burn dry Sal leaf litter beneath Mahua trees to spot fallen cream flowers on ash, triggering **over 60% of Bastar's dry-season forest fires**.
            """
        )
        if "water_and_environment" in challenges:
            for item in challenges["water_and_environment"]:
                st.info(f"📌 {item}")

    with st.expander("🌾 Post-Harvest Losses & Agricultural Value Capture", expanded=True):
        st.markdown(
            """
            - **Boda Wild Mushroom Decay**: Prized wild mycorrhizal mushrooms (*Termitomyces*) fetch ₹1,200–₹2,000/kg but rot within 24–36 hours due to extreme cellular respiration.
            - **Mahua Quality Degradation**: Soil and dung contamination during ground collection reduces farmgate selling prices by **40% to 50%**.
            - **Small Millet Hulling Breakage**: Tiny Kutki (1.5mm) and Kodo millet kernels suffer **>35% grain breakage** in commercial rice hullers.
            - **Tamarind Processing Discrepancies**: High embedded seed fractions (15–20%) and moisture spraying fraud cause massive trade disputes in Jagdalpur Mandi.
            """
        )
        if "post_harvest_losses" in challenges:
            for item in challenges["post_harvest_losses"]:
                st.info(f"📌 {item}")

    # 4. Policy and Institutional Support
    policy = context.get("policy_and_ecosystem", {})
    st.markdown("#### 📜 Policy Framework & Institutional Seed Capital")
    c1, c2 = st.columns(2)
    with c1:
        st.success(f"**State Policy**: {policy.get('state_policy')}")
        st.write(f"• **State Seed Grant**: {policy.get('state_seed_fund')}")
        st.write(f"• **State Venture Capital**: {policy.get('state_capital_fund')}")
    with c2:
        st.warning(f"**District Trust**: {policy.get('district_mineral_foundation')}")
        st.write("**Aligned National Programs**:")
        for prog in policy.get("national_schemes", []):
            st.markdown(f"- {prog}")


def render_eliminated_tab(eliminated_ideas: List[Dict[str, Any]]):
    """Render Tab 2: Eliminated Concepts with Fatal Flaws in Red Warnings."""
    st.markdown("### 🚫 Pre-Screening Elimination & Rejected Concepts")
    st.markdown(
        "*To ensure engineering student teams focus strictly on viable, legally defensible, and physically "
        "demonstrable ventures, concepts that failed preliminary feasibility were eliminated. "
        "Below are the rejected proposals with their explicit fatal flaws highlighted.*"
    )

    for idx, idea in enumerate(eliminated_ideas, 1):
        st.markdown(f"#### #{idx}: {idea.get('name')}")
        st.markdown(f"**Category**: `{idea.get('category')}`")
        st.write(f"**Proposed Concept**: {idea.get('proposed_concept')}")

        # Explicitly highlight FATAL FLAWS in RED warnings as requested
        st.markdown("**Fatal Flaws Identified:**")
        flaws = idea.get("fatal_flaws", [])
        cols = st.columns(len(flaws)) if flaws else []
        for c_idx, flaw in enumerate(flaws):
            with cols[c_idx]:
                st.error(f"🚨 **FATAL FLAW**: {flaw}")

        with st.expander(f"🔍 Detailed Rejection Rationale for #{idx} ({idea.get('name')})"):
            for reason in idea.get("rejection_reasons", []):
                st.markdown(f"- ❌ {reason}")

        st.markdown("---")


def render_funding_tab(grants_data: List[Dict[str, Any]]):
    """Render Tab 3: Funding Pathways in a clean, professional, readable format."""
    st.markdown("### 💰 Targeted Institutional Grants & Funding Pathways")
    st.markdown(
        "*Non-dilutive prototype grants, central innovation challenges, and public sector CSR funds "
        "tailored for engineering student hardware ventures in Bastar.*"
    )

    # Top summary metrics
    total_schemes = len(grants_data)
    max_grant = max(g.get("grant_amount_max_inr", 0) for g in grants_data)
    total_pipeline = sum(g.get("grant_amount_max_inr", 0) for g in grants_data)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Qualified Schemes", f"{total_schemes}")
    with col2:
        st.metric("Maximum Single Grant", f"₹{max_grant/100000:.0f} Lakhs")
    with col3:
        st.metric("Total Funding Pipeline", f"₹{total_pipeline/10000000:.2f} Crores")
    with col4:
        st.metric("Equity Dilution", "0% (Non-Dilutive)")

    st.markdown("---")

    # Filter / Search controls
    search_q = st.text_input("🔍 Search schemes by name, domain, or agency", placeholder="e.g. BIRAC, hardware, tribal, water...")

    filtered_grants = grants_data
    if search_q:
        q = search_q.lower()
        filtered_grants = [
            g for g in grants_data
            if q in g.get("name", "").lower()
            or q in g.get("agency", "").lower()
            or any(q in d.lower() for d in g.get("eligible_domains", []))
            or q in g.get("relevance", "").lower()
        ]

    for grant in filtered_grants:
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <h4 style="margin: 0; color: #0F172A;">{grant.get('name')}</h4>
                        <span style="font-size: 1.1rem; font-weight: 700; color: #16A34A;">{grant.get('grant_amount_formatted')}</span>
                    </div>
                    <div style="color: #475569; font-weight: 500; margin-bottom: 0.6rem;">🏛️ {grant.get('agency')}</div>
                    <div style="margin-bottom: 0.6rem;">
                        <strong>Target Stage:</strong> <code>{grant.get('target_stage')}</code> | 
                        <strong>Equity:</strong> <code>{grant.get('equity_taken')}</code>
                    </div>
                    <div style="margin-bottom: 0.6rem;">
                        <strong>Eligible Domains:</strong> {', '.join([f'<span class="badge badge-grant">{d}</span>' for d in grant.get('eligible_domains', [])])}
                    </div>
                    <div style="margin-bottom: 0.4rem;">
                        <strong>Key Benefits:</strong> {grant.get('key_benefits')}
                    </div>
                    <div style="color: #0369A1; font-style: italic;">
                        <strong>Student Relevance:</strong> {grant.get('relevance')}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_portfolio_tab(ideas_data: List[Dict[str, Any]]):
    """Render Tab 4: 20 Curated Ventures and Detailed Dossiers."""
    st.markdown("### 🚀 Portfolio of 20 Research-Backed Startup Ventures")
    st.markdown(
        "*Comprehensive master directory of student-buildable, physically demonstrable ventures "
        "designed for the B.Tech Engineering College in Jagdalpur.*"
    )

    # Filter controls
    c1, c2 = st.columns([1, 1])
    with c1:
        sectors = sorted(list({idea.get("sector", "") for idea in ideas_data}))
        sel_sector = st.selectbox("Filter by Sector", ["All Sectors"] + sectors)
    with c2:
        max_budget = st.slider("Max Prototype Budget (INR)", min_value=4000, max_value=15000, value=15000, step=500)

    filtered_ideas = ideas_data
    if sel_sector != "All Sectors":
        filtered_ideas = [i for i in filtered_ideas if i.get("sector") == sel_sector]
    filtered_ideas = [i for i in filtered_ideas if i.get("prototype", {}).get("budget_inr", 0) <= max_budget]

    st.write(f"Showing **{len(filtered_ideas)}** of {len(ideas_data)} ventures:")

    for idea in filtered_ideas:
        proto = idea.get("prototype", {})
        biz = idea.get("business_model", {})
        mkt = idea.get("market_opportunity", {})

        with st.expander(f"#{idea.get('number')} {idea.get('name')} — {idea.get('sector')} (Budget: ₹{proto.get('budget_inr', 0):,})"):
            st.markdown(f"**Executive Pitch**: *{idea.get('pitch')}*")

            tab_sol, tab_proto, tab_market, tab_demo = st.tabs(["💡 Solution & Tech", "🛠️ Prototype Specs", "📈 Market & Business", "🎪 Live Demo Script"])

            with tab_sol:
                st.write(idea.get("solution", {}).get("description"))
                st.write(f"**Hardware**: {', '.join(idea.get('solution', {}).get('hardware', []))}")
                st.write(f"**Edge AI / IoT**: {', '.join(idea.get('solution', {}).get('ai_ml_iot', []))}")
                st.write(f"**Defensible Advantage**: {idea.get('unique_advantage')}")

            with tab_proto:
                st.write(f"**Budget**: ₹{proto.get('budget_inr'):,} ({proto.get('budget_range')})")
                st.write(f"**Complexity**: `{proto.get('complexity')}` | **Timeline**: {proto.get('expected_dev_time_weeks')} weeks")
                st.write(f"**Required Student Skills**: {', '.join(proto.get('required_skills', []))}")
                st.write("**Key Components**:")
                for comp in proto.get("components", []):
                    st.markdown(f"- {comp}")

            with tab_market:
                st.write(f"**TAM / SAM / SOM**: {mkt.get('tam')} | {mkt.get('sam')} | {mkt.get('som')}")
                st.write(f"**Pricing**: {biz.get('pricing_model')}")
                st.write(f"**Target Buyers**: {idea.get('target_users', {}).get('buyers')}")
                st.write(f"**Year 1 Revenue**: {idea.get('revenue_projection', {}).get('year_1')}")

            with tab_demo:
                demo = idea.get("demonstration", {})
                st.write(f"**Physical Demo Setup**: {demo.get('setup')}")
                st.write(f"**Live 60-Second Action**: {demo.get('live_action')}")
                st.success(f"**Measurable Readout**: {demo.get('measurable_result')}")
                st.info(f"**Judge Takeaway**: {demo.get('judge_takeaway')}")


def main():
    """Main dashboard application runner."""
    st.set_page_config(
        page_title="Bastar Innovate: Venture Intelligence Engine",
        page_icon="💡",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    apply_custom_css()

    # Load data
    try:
        data = load_all_dashboard_data()
    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
        return

    # Sidebar
    with st.sidebar:
        st.title("💡 Bastar Innovate")
        st.markdown("**One Institution – One Startup Initiative**")
        st.markdown("*B.Tech Engineering College, Jagdalpur, Bastar, Chhattisgarh*")
        st.markdown("---")
        st.markdown(
            """
            **Navigation Views:**
            1. **🌳 Bastar Ecosystem**: Local demographics, challenges & geography
            2. **🚫 Eliminated Concepts**: Rejected ideas & fatal flaws in red
            3. **💰 Funding Pathways**: Central, state & CSR innovation grants
            4. **🚀 20 Curated Ventures**: Complete portfolio & specs
            """
        )
        st.markdown("---")
        st.info("🎓 Prepared for Academic Mentors, Faculty Evaluation & Competition Juries")

    # App Header
    st.markdown('<div class="main-header">Bastar Innovation Venture Intelligence Engine</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">Institutional Initiative: One Institution – One Startup | Government Engineering College, Jagdalpur, Chhattisgarh</div>',
        unsafe_allow_html=True,
    )

    # 4 Main Tabs
    tab_eco, tab_elim, tab_grants, tab_portfolio = st.tabs([
        "🌳 Bastar Ecosystem",
        "🚫 Eliminated Concepts",
        "💰 Funding Pathways",
        "🚀 20 Curated Ventures",
    ])

    with tab_eco:
        render_ecosystem_tab(data["context"])

    with tab_elim:
        render_eliminated_tab(data["eliminated"])

    with tab_grants:
        render_funding_tab(data["grants"])

    with tab_portfolio:
        render_portfolio_tab(data["ideas"])


if __name__ == "__main__":
    from streamlit.runtime.scriptrunner import get_script_run_ctx

    if get_script_run_ctx() is None:
        import sys
        import streamlit.web.cli as stcli
        sys.argv = ["streamlit", "run", __file__] + sys.argv[1:]
        sys.exit(stcli.main())
    else:
        main()
