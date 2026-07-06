# # Calculator tool
# def calculate(expression: str) -> str:
#     """Calculate the result of a mathematical expression."""
#     try:
#         result = eval(expression)
#         return str(result)
#     except Exception as e:
#         return f"Error: {(e)}"
    
# # Word Counter tool
# def count_words(text: str) -> int:
#     """Count the number of words in a given text."""
#     return len(text.split())

# # Text Statistics tool
# def text_statistics(text: str) -> dict:
#     """
#     Returns statistics about the text.
#     """

#     return {

#         "Characters": len(text),

#         "Words": len(text.split()),

#         "Sentences": text.count(".") + text.count("?") + text.count("!")
#     }

# Current Date & Time tool
from datetime import datetime
def current_datetime() -> str:
    """
    Returns current date and time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

