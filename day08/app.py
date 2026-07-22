# load environment variables
from dotenv import load_dotenv
# used to access environment variables
import os

# langchain prompt template
from langchain_core.prompts import PromptTemplate
# langchain wrapper for google genai
from langchain_google_genai import ChatGoogleGenerativeAI
# lanchain output parser
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# creating model object
model = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini-2.5-flash",
    temperature=0.3
)

# creating prompt template
prompt = PromptTemplate(
    template="""
You are a {role}.

Explain {topic} to a {level} learner.

Keep the explanation simple and use bullet points.
""",
    input_variables=["topic", "level", "role"],
)

# creating output parser
parser = StrOutputParser() # Extracts the string.

# creating chain object
# LCEL
chain = prompt | model | parser

role = input("Enter Role: ")
topic = input("Enter Topic: ")
level = input("Enter Difficulty: ")

# invoking chain
response = chain.invoke(
    {
        "role": role,
        "topic": topic,
        "level": level
    }
)

print("\nAI Response:\n")
print(response)