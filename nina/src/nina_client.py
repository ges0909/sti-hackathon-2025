import httpx
from typing import Optional


class NinaClient:
    """Client für NINA API des Bundesamts für Bevölkerungsschutz"""

    def __init__(self):
        self.base_url = "https://warnung.bund.de/api31"

    async def get_all_warnings(self) -> list[dict]:
        """Alle aktuellen Warnungen abrufen."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/dashboard/warnings.json")
            response.raise_for_status()
            return response.json()

    async def get_warning_details(self, warning_id: str) -> Optional[dict]:
        """Detaillierte Warnung nach ID."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/warnings/{warning_id}.json"
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    return None
                raise

    async def get_regional_warnings(self, region_code: str) -> list[dict]:
        """Regionale Warnungen (z.B. '091620000000' für München)."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/dashboard/{region_code}.json")
            response.raise_for_status()
            return response.json()

    async def get_weather_warnings(self) -> list[dict]:
        """Unwetterwarnungen vom DWD."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/dwd/warnings.json")
            response.raise_for_status()
            return response.json()


nina_client = NinaClient()
