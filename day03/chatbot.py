from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API Key not found!")
    exit()


client = genai.Client(api_key=api_key)


def ask_gemini(question: str) -> str:
    """
    Sends a question to Gemini and returns the response.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"