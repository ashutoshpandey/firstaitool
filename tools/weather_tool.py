from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Returns the current weather for a given city."""
    return f"The weather in {city} is 27°C with clear skies."
