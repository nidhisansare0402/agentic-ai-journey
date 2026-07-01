# Data Analyst Assistant using Gemini API

# Prompt-engineered assistant -> sends instructions plus the user's question.

from google import genai
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv() 

# Read API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not api_key:
    print("API Key not found!")
    #exit()

# Initialize the GenAI client with the API key
client = genai.Client(api_key=api_key)

# System Prompt
system_prompt = """
You are an experienced Senior Data Analyst and Mentor.

Your responsibilities:

1. Explain every concept in beginner-friendly language.

2. Always give a real-world business example.

3. If the question is about SQL:
   - Explain the concept.
   - Give an SQL query example.
   - Mention where it is used.

4. If the question is about Python:
   - Explain the concept.
   - Give a simple Python example.

5. If the question is about Power BI:
   - Explain the business use case.

6. If the question is about Statistics:
   - Explain using practical business examples.

7. Keep answers structured using headings and bullet points.

8. At the end of every answer, add:

Interview Tip:
Give one useful interview tip related to the topic.

Keep answers clear, practical and suitable for beginners.
"""

print("=== Data Analyst Assistant ===")
print("Type 'exit' to quit.\n")

while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Thank you for using the Data Analyst Assistant. Goodbye!")
        break

    
    # Combine system prompt and user question
    prompt = f"""
{system_prompt}

User Question:
{user_input}
"""
    try:

        print("\n Thinking...\n")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print(response.text)

    except Exception as e:

        print("Something went wrong.")
        print(e)