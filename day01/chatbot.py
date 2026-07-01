# This is a simple chatbot implementation using the Google GenAI API. It reads the API key from an environment variable, initializes the GenAI client, and sends a request to generate content based on a given prompt. The response from the model is then printed to the console.

# Basic chatbot -> sends only the user's question.

# Import Gemini SDK
from google import genai
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv() 

# Read API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the GenAI client with the API key
client = genai.Client(api_key=api_key)

# send a request to the model to generate content
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain SQL JOIN with an example"
# )

print("=== Gemini Chatbot ===")
print("Type 'exit' to quit.\n")

while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Exiting chatbot. Goodbye!")
        break
    
    print("Sending request to Gemini...")
    # Send a request to the model to generate content based on user input
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )
    print("Response received!")
    # print the response from the model
    print("\n AI:", response.text)