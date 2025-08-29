from mcp.server.fastmcp import FastMCP
from nina_client import nina_client

mcp = FastMCP("NINA Notfall-Informations- und Nachrichten-App")

@mcp.tool(
    name="Regionale Warnungen abrufen",
    description="Ruft Warnungen für eine bestimmte Region ab (ARS-Code erforderlich)",
)
async def get_regional_warnings(region_code: str) -> dict | None:
    """Regionale Warnungen nach ARS-Code."""
    return await nina_client.get_regional_warnings(region_code)


@mcp.tool(
    name="Warnung Details",
    description="Detaillierte Informationen zu einer spezifischen Warnung",
)
async def get_warning_details(warning_id: str) -> dict | None:
    """Detaillierte Warninformationen nach ID."""
    return await nina_client.get_warning_details(warning_id)


@mcp.tool(
    name="Corona Regelungen",
    description="Corona Regelungen für eine bestimmte Region (ARS-Code erforderlich)",
)
async def get_covid_rules(region_code: str) -> dict | None:
    """Corona Regelungen nach ARS-Code."""
    return await nina_client.get_covid_rules(region_code)


@mcp.resource("nina://status")
async def nina_status() -> str:
    """NINA API Status."""
    return """NINA Katastrophenschutz API
    Status: Aktiv
    Endpoint: https://warnung.bund.de/api31"""


@mcp.prompt("warnung-analyse")
async def analyze_warning(warning_id: str) -> str:
    """Prompt für Warnungsanalyse."""
    return f"""Analysiere diese NINA-Warnung: {warning_id}

Bitte bewerte:
- Gefährdungsgrad und betroffene Gebiete
- Empfohlene Schutzmaßnahmen
- Zeitlicher Verlauf und Dauer
- Auswirkungen auf die Bevölkerung
- Handlungsempfehlungen

Nutze die Warnungsdetails für eine umfassende Risikoeinschätzung."""
