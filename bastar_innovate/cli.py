"""Command Line Interface for Bastar Innovate Venture Intelligence Platform."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from bastar_innovate.blueprints import get_flagship_blueprints
from bastar_innovate.evaluator import VentureEvaluator
from bastar_innovate.exporter import VentureExporter
from bastar_innovate.financials import FinancialEngine
from bastar_innovate.grants import GrantMatcher
from bastar_innovate.repository import VentureRepository

console = Console()
repo = VentureRepository()
evaluator = VentureEvaluator(repo)
matcher = GrantMatcher(repo)
exporter = VentureExporter(repo)


@click.group()
def cli():
    """Bastar Innovate: One Institution - One Startup Venture Platform."""
    pass


@cli.command("list")
@click.option("--sector", "-s", default=None, help="Filter by sector substring.")
@click.option("--max-budget", "-b", default=None, type=int, help="Filter by maximum prototype budget (INR).")
def list_ideas(sector: Optional[str], max_budget: Optional[int]):
    """List curated startup ventures."""
    ideas = repo.get_all_ideas()
    if sector:
        ideas = [i for i in ideas if sector.lower() in i.sector.lower()]
    if max_budget:
        ideas = [i for i in ideas if i.prototype.budget_inr <= max_budget]

    table = Table(title="One Institution – One Startup: 20 Curated Ventures (Jagdalpur, Bastar)", show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("ID", style="cyan", width=16)
    table.add_column("Venture Name", style="bold white", width=34)
    table.add_column("Sector", style="green", width=26)
    table.add_column("Score", justify="right", style="yellow", width=8)
    table.add_column("Budget", justify="right", style="bold green", width=12)
    table.add_column("Complexity", width=12)

    for idea in ideas:
        ev = repo.get_evaluation(idea.id)
        score_str = f"{ev.composite_score:.2f}" if ev else "N/A"
        clean_name = idea.name.split(":")[0]
        table.add_row(
            str(idea.number),
            idea.id,
            clean_name,
            idea.sector,
            score_str,
            f"₹{idea.prototype.budget_inr:,}",
            idea.prototype.complexity,
        )

    console.print(table)


@cli.command("detail")
@click.argument("idea_id")
def detail(idea_id: str):
    """View complete dossier for a specific venture."""
    idea = repo.get_idea(idea_id)
    if not idea:
        console.print(f"[bold red]Error: Idea '{idea_id}' not found.[/bold red]")
        sys.exit(1)

    ev = repo.get_evaluation(idea.id)
    score_text = f"Viability Score: {ev.composite_score}/10" if ev else ""

    console.print(Panel(f"[bold yellow]{idea.name}[/bold yellow]\n[green]{idea.sector}[/green] | [cyan]{score_text}[/cyan]\n\n[bold italic]{idea.pitch}[/bold italic]", title=f"Venture #{idea.number}: {idea.id.upper()}", expand=False))

    console.print("\n[bold cyan]1. Problem Statement[/bold cyan]")
    console.print(f"• [bold]Affected Population[/bold]: {idea.problem.target_affected}")
    console.print(f"• [bold]Why Existing Fail[/bold]: {idea.problem.why_existing_fail}")
    console.print(f"• [bold]Consequence[/bold]: {idea.problem.consequence_if_unsolved}")

    console.print("\n[bold cyan]2. Technical Solution Specification[/bold cyan]")
    console.print(f"{idea.solution.description}")
    console.print(f"• [bold]Hardware[/bold]: {', '.join(idea.solution.hardware)}")
    console.print(f"• [bold]Edge AI / IoT[/bold]: {', '.join(idea.solution.ai_ml_iot)}")

    console.print("\n[bold cyan]3. Student Prototype & Demo[/bold cyan]")
    console.print(f"• [bold]Budget[/bold]: ₹{idea.prototype.budget_inr:,} ({idea.prototype.budget_range})")
    console.print(f"• [bold]Timeline[/bold]: {idea.prototype.expected_dev_time_weeks} weeks | [bold]Complexity[/bold]: {idea.prototype.complexity}")
    console.print(f"• [bold]Live Stage Demo[/bold]: {idea.demonstration.live_action}")
    console.print(f"• [bold]Measurable Result[/bold]: {idea.demonstration.measurable_result}")

    console.print("\n[bold cyan]4. Commercials & Financials[/bold cyan]")
    console.print(f"• [bold]Pricing[/bold]: {idea.business_model.pricing_model}")
    console.print(f"• [bold]TAM / SAM / SOM[/bold]: {idea.market_opportunity.tam} | {idea.market_opportunity.sam} | {idea.market_opportunity.som}")
    console.print(f"• [bold]Year 1 Revenue[/bold]: {idea.revenue_projection.year_1}")


@cli.command("rank")
@click.option("--by", "-b", default="composite", help="Criteria to rank by (composite, problem_severity, prototype_feasibility, social_environmental_impact, competition_potential, revenue_potential).")
@click.option("--top", "-t", default=20, type=int, help="Number of results to display.")
def rank(by: str, top: int):
    """Rank ventures by multi-criteria scores."""
    ranked = evaluator.rank_ideas(sort_by=by)
    table = Table(title=f"Venture Rankings sorted by '{by.upper()}'", header_style="bold cyan")
    table.add_column("Rank", style="bold cyan", no_wrap=True)
    table.add_column("ID", style="cyan", width=14)
    table.add_column("Venture Name", style="bold white", width=22)
    table.add_column("Composite", justify="right", style="yellow", width=9)
    table.add_column("Score", justify="right", style="bold green", width=7)
    table.add_column("Budget", justify="right", width=10)

    for idx, (idea, ev) in enumerate(ranked[:top], 1):
        metric_val = getattr(ev, by) if hasattr(ev, by) else ev.composite_score
        clean_name = idea.name.split(":")[0]
        table.add_row(
            f"#{idx}",
            idea.id,
            clean_name,
            f"{ev.composite_score:.2f}",
            f"{metric_val:.2f}",
            f"₹{idea.prototype.budget_inr:,}",
        )

    console.print(table)


@cli.command("blueprint")
@click.argument("idea_id")
def blueprint(idea_id: str):
    """Display deep-dive engineering blueprint for flagship ventures."""
    blueprints = get_flagship_blueprints()
    if idea_id not in blueprints:
        console.print(f"[bold red]Blueprint not available for '{idea_id}'. Available flagships: {', '.join(blueprints.keys())}[/bold red]")
        sys.exit(1)

    bp = blueprints[idea_id]
    console.print(Panel(f"[bold yellow]{bp.name}[/bold yellow] - [italic]{bp.tagline}[/italic]", title=f"FLAGSHIP BLUEPRINT: {idea_id.upper()}", expand=False))

    console.print("\n[bold green]30-Second Elevator Pitch:[/bold green]")
    console.print(f"{bp.pitch_30s}\n")

    table = Table(title=f"Bill of Materials (BOM) - Total: ₹{bp.total_bom_cost_inr:,}", header_style="bold blue")
    table.add_column("Item", width=25)
    table.add_column("Specification", width=35)
    table.add_column("Qty", justify="right", width=6)
    table.add_column("Unit Cost", justify="right", width=12)
    table.add_column("Total", justify="right", style="bold green", width=12)

    for item in bp.bill_of_materials:
        table.add_row(item.item, item.specification, str(item.quantity), f"₹{item.unit_cost_inr:,}", f"₹{item.total_cost_inr:,}")

    console.print(table)

    console.print("\n[bold green]30-60-90 Day Execution Sprint Roadmap:[/bold green]")
    for phase, tasks in bp.execution_roadmap_30_60_90.items():
        console.print(f"[bold cyan]{phase.replace('_', ' ').title()}:[/bold cyan]")
        for task in tasks:
            console.print(f"  • {task}")


@cli.command("compare")
@click.argument("idea1_id")
@click.argument("idea2_id")
def compare(idea1_id: str, idea2_id: str):
    """Head-to-head comparison of two ventures."""
    i1 = repo.get_idea(idea1_id)
    i2 = repo.get_idea(idea2_id)
    if not i1 or not i2:
        console.print("[bold red]One or both idea IDs invalid.[/bold red]")
        sys.exit(1)

    ev1 = repo.get_evaluation(i1.id)
    ev2 = repo.get_evaluation(i2.id)

    table = Table(title=f"Head-to-Head Comparison: {i1.name.split(':')[0]} vs {i2.name.split(':')[0]}", header_style="bold magenta")
    table.add_column("Metric / Dimension", style="cyan", width=30)
    table.add_column(f"{i1.name.split(':')[0]} ({i1.id})", width=25)
    table.add_column(f"{i2.name.split(':')[0]} ({i2.id})", width=25)

    table.add_row("Sector", i1.sector, i2.sector)
    table.add_row("Composite Score", f"{ev1.composite_score:.2f}" if ev1 else "N/A", f"{ev2.composite_score:.2f}" if ev2 else "N/A")
    table.add_row("Prototype Budget", f"₹{i1.prototype.budget_inr:,}", f"₹{i2.prototype.budget_inr:,}")
    table.add_row("Complexity", i1.prototype.complexity, i2.prototype.complexity)
    table.add_row("Problem Severity", str(ev1.problem_severity) if ev1 else "N/A", str(ev2.problem_severity) if ev2 else "N/A")
    table.add_row("Prototype Feasibility", str(ev1.prototype_feasibility) if ev1 else "N/A", str(ev2.prototype_feasibility) if ev2 else "N/A")
    table.add_row("Competition Potential", str(ev1.competition_potential) if ev1 else "N/A", str(ev2.competition_potential) if ev2 else "N/A")
    table.add_row("Social/Eco Impact", str(ev1.social_environmental_impact) if ev1 else "N/A", str(ev2.social_environmental_impact) if ev2 else "N/A")
    table.add_row("Commercial Pricing", i1.business_model.pricing_model, i2.business_model.pricing_model)

    console.print(table)


@cli.command("grants")
@click.argument("idea_id")
def grants(idea_id: str):
    """Match eligible Indian government and institutional grants for an idea."""
    idea = repo.get_idea(idea_id)
    if not idea:
        console.print(f"[bold red]Error: Idea '{idea_id}' not found.[/bold red]")
        sys.exit(1)

    matches = matcher.match_idea(idea)
    pipeline = matcher.total_grant_potential(idea)

    console.print(Panel(f"[bold yellow]{idea.name}[/bold yellow]\nQualified Schemes: [bold green]{pipeline['qualified_schemes_count']}[/bold green] | Max Pipeline: [bold cyan]{pipeline['formatted_pipeline']}[/bold cyan]", title=f"Grant Matching: {idea_id.upper()}", expand=False))

    table = Table(header_style="bold blue")
    table.add_column("Scheme", style="bold white", width=25)
    table.add_column("Agency", width=25)
    table.add_column("Funding Limit", style="green", width=18)
    table.add_column("Match", justify="right", style="yellow", width=8)
    table.add_column("Qualification Rationale", width=40)

    for m in matches:
        table.add_row(m.scheme_name, m.agency, m.grant_amount_formatted, f"{int(m.match_score * 100)}%", m.rationale)

    console.print(table)


@cli.command("financials")
@click.argument("idea_id")
def financials(idea_id: str):
    """Display unit economics and pro-forma 3-year model for an idea."""
    idea = repo.get_idea(idea_id)
    if not idea:
        console.print(f"[bold red]Error: Idea '{idea_id}' not found.[/bold red]")
        sys.exit(1)

    # Estimate unit price and COGS based on BOM and business model
    sale_price = idea.prototype.budget_inr * 2.8
    cogs = idea.prototype.budget_inr * 1.5
    ue = FinancialEngine.calculate_unit_economics(sale_price=sale_price, cogs=cogs)
    pf = FinancialEngine.generate_pro_forma(
        idea_id=idea.id,
        idea_name=idea.name,
        unit_price=sale_price,
        cogs=cogs,
        y1_units=40,
        y2_units=180,
        y3_units=600,
    )

    console.print(Panel(f"[bold yellow]{idea.name}[/bold yellow]\nUnit Price: [bold green]₹{ue.unit_sale_price_inr:,.0f}[/bold green] | COGS: [red]₹{ue.cogs_inr:,.0f}[/red] | Gross Margin: [bold cyan]{ue.gross_margin_percent}%[/bold cyan] | Payback: [yellow]{ue.payback_period_months} months[/yellow]", title=f"Unit Economics: {idea_id.upper()}", expand=False))

    table = Table(title="3-Year Pro-Forma Income Statement", header_style="bold magenta")
    table.add_column("Financial Metric", width=25)
    table.add_column("Year 1 (Pilot)", justify="right", width=18)
    table.add_column("Year 2 (State)", justify="right", width=18)
    table.add_column("Year 3 (Scale)", justify="right", width=18)

    table.add_row("Units Deployed", f"{pf.year_1_units}", f"{pf.year_2_units}", f"{pf.year_3_units}")
    table.add_row("Total Revenue", f"₹{pf.year_1_revenue_inr:,.0f}", f"₹{pf.year_2_revenue_inr:,.0f}", f"₹{pf.year_3_revenue_inr:,.0f}")
    table.add_row("COGS", f"₹{pf.year_1_cogs_inr:,.0f}", f"₹{pf.year_2_cogs_inr:,.0f}", f"₹{pf.year_3_cogs_inr:,.0f}")
    table.add_row("Operating Overheads", f"₹{pf.year_1_opex_inr:,.0f}", f"₹{pf.year_2_opex_inr:,.0f}", f"₹{pf.year_3_opex_inr:,.0f}")
    table.add_row("EBITDA", f"₹{pf.year_1_ebitda_inr:,.0f}", f"₹{pf.year_2_ebitda_inr:,.0f}", f"₹{pf.year_3_ebitda_inr:,.0f}")
    table.add_row("Breakeven Annual Volume", f"{pf.breakeven_units_per_year} units", f"{pf.breakeven_units_per_year} units", f"{pf.breakeven_units_per_year} units")

    console.print(table)


@cli.command("eliminated")
def eliminated():
    """List rejected ideas and rejection reasons."""
    elim_list = repo.get_eliminated_ideas()
    table = Table(title="Pre-Screening Elimination Pool (Rejected Concepts)", header_style="bold red")
    table.add_column("#", width=4)
    table.add_column("Concept Name", style="bold white", width=28)
    table.add_column("Category", style="yellow", width=18)
    table.add_column("Fatal Flaws", style="bold red", width=30)
    table.add_column("Primary Rejection Reason", width=45)

    for idx, elim in enumerate(elim_list, 1):
        table.add_row(
            str(idx),
            elim.name,
            elim.category,
            ", ".join(elim.fatal_flaws),
            elim.rejection_reasons[0] if elim.rejection_reasons else "",
        )

    console.print(table)


@cli.command("export")
@click.option("--format", "-f", type=click.Choice(["json", "csv", "docs"]), default="json", help="Export format.")
@click.option("--output", "-o", default=None, help="Output file or directory path.")
def export(format: str, output: Optional[str]):
    """Export venture assets, CSV summary, or documentation."""
    if format == "json":
        data = exporter.export_ideas_json()
        if output:
            Path(output).write_text(data, encoding="utf-8")
            console.print(f"[bold green]Exported JSON to {output}[/bold green]")
        else:
            click.echo(data)
    elif format == "csv":
        data = exporter.export_summary_csv()
        if output:
            Path(output).write_text(data, encoding="utf-8")
            console.print(f"[bold green]Exported CSV to {output}[/bold green]")
        else:
            click.echo(data)
    elif format == "docs":
        out_dir = Path(output) if output else Path("docs")
        exporter.write_all_documentation(out_dir)
        console.print(f"[bold green]Generated complete documentation in {out_dir}/[/bold green]")


@cli.command("context")
def context():
    """Display Bastar regional demographic and industrial context."""
    ctx = repo.get_context()
    console.print(Panel(f"[bold yellow]{ctx.get('region')}[/bold yellow] - [cyan]{ctx.get('state')}[/cyan]", title="Regional Operating Environment", expand=False))
    console.print("\n[bold cyan]Demographics & Economy:[/bold cyan]")
    demo = ctx.get("demographics_and_economy", {})
    console.print(f"• Tribal Population: {demo.get('tribal_population_percentage')}")
    console.print(f"• Major Trade Hub: {demo.get('major_trade_hub')}")
    console.print(f"• Industrial Nodes: {', '.join(demo.get('industrial_nodes', []))}")


def main():
    cli()


if __name__ == "__main__":
    main()
