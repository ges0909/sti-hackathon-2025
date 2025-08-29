from typing import Optional
from nina_api_client import Client
from nina_api_client.api.warnings import get_dashboard, get_warning
from nina_api_client.api.covid import get_ars_covid_rules


class NinaClient:
    """Client für NINA API des Bundesamts für Bevölkerungsschutz"""

    def __init__(self):
        self.client = Client(base_url="https://warnung.bund.de/api31")

    async def get_regional_warnings(self, region_code: str) -> Optional[dict]:
        """Regionale Warnungen (z.B. '091620000000' für München)."""
        result = await get_dashboard.asyncio(ars=region_code, client=self.client)
        return result.to_dict() if result else None

    async def get_warning_details(self, warning_id: str) -> Optional[dict]:
        """Detaillierte Warnung nach ID."""
        result = await get_warning.asyncio(identifier=warning_id, client=self.client)
        return result.to_dict() if result else None

    async def get_covid_rules(self, region_code: str) -> Optional[dict]:
        """Corona Regelungen für Region."""
        result = await get_ars_covid_rules.asyncio(ars=region_code, client=self.client)
        return result.to_dict() if result else None


nina_client = NinaClient()
