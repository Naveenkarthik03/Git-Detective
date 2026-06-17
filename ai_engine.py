import os

from dotenv import load_dotenv
from google import genai

from repo_reader import read_repository


# ---------------------------------
# Load API Key
# ---------------------------------
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ---------------------------------
# General AI Questions
# ---------------------------------
def ask_ai(question):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=question
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# ---------------------------------
# Repository Questions
# ---------------------------------
def ask_repo(question):

    repo_content = read_repository("temp_repo")

    if not repo_content:

        return "No Python files found inside temp_repo."

    prompt = f"""
You are an AI code assistant.

Repository content:

{repo_content}

Question:

{question}

Instructions:

- Answer clearly.
- Explain in simple words.
- Mention file names when necessary.
- Use bullet points if appropriate.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# ---------------------------------
# Test
# ---------------------------------
if __name__ == "__main__":

    answer = ask_repo(
        "Summarize this repository in 5 bullet points"
    )

    print(answer)