from mcp.server.fastmcp import FastMCP
from nina_client import nina_client

mcp = FastMCP("NINA Notfall-Informations- und Nachrichten-App")


@mcp.tool(
    name="Alle Warnungen abrufen",
    description="Ruft alle aktuellen Katastrophenschutz-Warnungen von NINA ab",
)
async def get_all_warnings() -> list[dict]:
    """Alle aktuellen Warnungen von NINA."""
    return await nina_client.get_all_warnings()


@mcp.tool(
    name="Warnung Details",
    description="Detaillierte Informationen zu einer spezifischen Warnung",
)
async def get_warning_details(warning_id: str) -> dict | None:
    """Detaillierte Warninformationen nach ID."""
    return await nina_client.get_warning_details(warning_id)


@mcp.tool(
    name="Regionale Warnungen",
    description="Warnungen für eine bestimmte Region (Regionscode erforderlich)",
)
async def get_regional_warnings(region_code: str) -> list[dict]:
    """Regionale Warnungen nach Regionscode."""
    return await nina_client.get_regional_warnings(region_code)


@mcp.tool(
    name="Unwetterwarnungen",
    description="Unwetterwarnungen vom Deutschen Wetterdienst (DWD)",
)
async def get_weather_warnings() -> list[dict]:
    """Unwetterwarnungen vom DWD."""
    return await nina_client.get_weather_warnings()


@mcp.tool(
    name="Warnungen nach Schweregrad filtern",
    description="Filtert Warnungen nach Schweregrad (Minor, Moderate, Severe, Extreme)",
)
async def filter_by_severity(severity: str) -> list[dict]:
    """Warnungen nach Schweregrad filtern."""
    warnings = await nina_client.get_all_warnings()
    return [w for w in warnings if w.get("severity", "").lower() == severity.lower()]


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
