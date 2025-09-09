import os
import webbrowser
from pathlib import Path

import googlemaps
import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def api_key():
    return os.getenv("GOOGLE_API_KEY")


@pytest.fixture
def url() -> str:
    return "https://www.google.com/maps"


@pytest.fixture
def address() -> str:
    return "Brandenburger Tor, Berlin"


load_dotenv(dotenv_path=Path.home() / ".env")


def test_open_webbrowser(url: str):
    assert webbrowser.open(url)


def test_map_address_to_location(address: str, api_key: str):
    gmaps = googlemaps.Client(key=api_key)
    location = gmaps.geocode(address)
