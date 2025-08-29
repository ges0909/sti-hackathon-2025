"""A client library for accessing Bundesamt für Bevölkerungsschutz: NINA API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
