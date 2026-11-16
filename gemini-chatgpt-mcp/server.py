import os
from fastmcp import FastMCP
from google import genai
from google.genai import types

mcp = FastMCP("Google AI Studio - Gemini")

def gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured on the server.")
    return genai.Client(api_key=api_key)

@mcp.tool()
def ask_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """Send a prompt to Google Gemini and return its text response."""
    if not prompt.strip():
        raise ValueError("prompt must not be empty")
    response = gemini_client().models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.7),
    )
    return response.text or "Gemini returned no text."

@mcp.tool()
def list_gemini_models() -> str:
    """Return a short list of suggested Gemini model IDs."""
    return "\n".join([
        "gemini-2.5-flash — fast general-purpose model",
        "gemini-2.5-pro — higher-capability reasoning and complex tasks",
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
