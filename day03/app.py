# Build an AI Assistant that can decide whether to:
# Use one of your local tools
# OR send the question to Gemini
from chatbot import ask_gemini

from tools import (
    calculate,
    count_words,
    text_statistics,
    current_datetime
)

print("=" * 50)
print("Smart AI Assistant")
print("=" * 50)

print("Type 'exit' to quit.\n")

while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Thank you for using the Smart AI Assistant!")
        break

    # Decide whether to use a local tool or send the question to Gemini
    if user_input.lower().startswith("calculate"):
        expression = user_input[9:].strip()
        result = calculate(expression)
        print(f"Result: {result}")
    elif user_input.lower().startswith("count words"):
        text = user_input[11:].strip()
        result = count_words(text)
        print(f"Word Count: {result}")
    elif user_input.lower().startswith("statistics"):
        text = user_input[10:].strip()
        result = text_statistics(text)
        print(f"Text Statistics: {result}")
    elif "date" in user_input.lower() or "time" in user_input.lower():
        result = current_datetime()
        print(f"Current Date and Time: {result}")
    else:
        response = ask_gemini(user_input)
        print(f"\nAI Response:\n{response}\n")