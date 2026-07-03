# Build an application where the user can:
# Enter a question.
# Select an AI role.
# Automatically generate the correct prompt.
# Send it to Gemini.
# Receive a customized response.

#import Gemini SDK
from google import genai
from dotenv import load_dotenv
from roles import ROLES
import os

#load environment variables from .env file
load_dotenv()
# Read API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not api_key:
    print("API Key not found!")
    exit()

# Initialize the GenAI client with the API key
client = genai.Client(api_key=api_key)

print("=== Gemini Role-Based Chatbot ===")
print("Type 'exit' to quit.\n")

role_names = {
    "1": "Teacher",
    "2": "HR Recruiter",
    "3": "Senior Data Analyst",
    "4": "Senior Software Engineer"
    }

# To keep the application running until the user decides to exit.
while True:

    print("Choose your AI Assistant:")
    print("1. Teacher")
    print("2. HR Recruiter")    
    print("3. Senior Data Analyst")
    print("4. Senior Software Engineer")

    choice = input("Enter your choice (1-4): ")

    if choice.lower() == 'exit':
        print("Exiting chatbot!")
        break

    if choice not in ROLES:
        print("Invalid choice.")
        continue

    # Get user question
    question = input("Enter your question: ")

    if question.lower() == 'exit':
        print("Exiting chatbot!")
        break

    # Generate the system prompt based on the selected role
    # Used Dynamic Prompt Selection
    system_prompt = ROLES[choice]


    print(f"\nSelected Role: {role_names[choice]}")

    # Create the final prompt by combining the system prompt and user question
    prompt = f"""
    {system_prompt}
    User Question: 
    {question}
    """

    # Send the prompt to Gemini and get the response
    try:
        print("\n Thinking... \n")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        print("\nAI Response: \n")
        print(response.text)

    except Exception as e:
        print("Error occurred:", e)