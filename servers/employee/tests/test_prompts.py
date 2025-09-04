import os
import pytest
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Lade Umgebungsvariablen aus einer .env-Datei (z.B. für den OPENAI_API_KEY)
load_dotenv()

# Wir markieren diese Tests, damit sie optional ausgeführt werden können,
# da sie eine echte API-Anfrage machen und Kosten verursachen können.
pytestmark = pytest.mark.llm_integration

# Prüfen, ob der API-Schlüssel vorhanden ist, sonst Tests überspringen
api_key_present = os.getenv("OPENAI_API_KEY") is not None


@pytest.fixture(scope="module")
def client():
    """Initialisiert den OpenAI-Client."""
    if not api_key_present:
        pytest.skip("OPENAI_API_KEY is not set, skipping LLM integration tests.")
    return AsyncOpenAI()


async def get_llm_response(client: AsyncOpenAI, prompt: str) -> str:
    """Hilfsfunktion, um eine Antwort vom LLM zu erhalten."""
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",  # Ein schnelles und günstiges Modell für Tests
        temperature=0.1,  # Niedrige Temperatur für konsistentere Ergebnisse
    )
    return chat_completion.choices[0].message.content


# --- Tests für deine Prompts ---


@pytest.mark.asyncio
async def test_prompt_zeige_mitarbeiter_anzahl(client: AsyncOpenAI):
    """
    Testet den Prompt, der die Anzahl der Mitarbeiter abfragt.
    Wir überprüfen, ob die Antwort Schlüsselwörter wie 'Gesamtzahl' enthält.
    """
    # Importiere die Prompt-Funktion aus deinem Server
    from servers.employee.src.server import get_number_of_employees

    prompt_text = await get_number_of_employees()
    response = await get_llm_response(client, prompt_text)

    print(f"\nPrompt:\n---\n{prompt_text}\n---\nLLM Response:\n---\n{response}\n---")

    # Überprüfung: Wir erwarten, dass die Antwort die geforderten Begriffe enthält.
    response_lower = response.lower()
    assert "gesamtzahl" in response_lower
    assert "mitarbeiter" in response_lower
    assert "länderkennung" in response_lower or "land" in response_lower


# Hier könntest du weitere Tests für andere Prompts hinzufügen, z.B. für 'zeige-mitarbeiter'
# async def test_prompt_zeige_mitarbeiter(client: AsyncOpenAI):
#     ...
