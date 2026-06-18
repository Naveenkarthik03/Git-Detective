import os

from dotenv import load_dotenv

from google import genai

from repo_reader import read_repository


# ---------------------------
# Load API key
# ---------------------------
load_dotenv()

client = genai.Client(

    api_key=os.getenv(

        "GEMINI_API_KEY"

    )

)


# ---------------------------
# General AI
# ---------------------------
def ask_ai(question):

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash-lite",

            contents=question

        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# ---------------------------
# Repository Summary
# ---------------------------
def generate_summary():

    repo_content = read_repository(

        "temp_repo"

    )

    if not repo_content:

        return "No repository found."

    prompt = f"""

Repository:

{repo_content}

Instructions:

Return ONLY these 5 sections.

Project Purpose:

Maximum 2 lines.

Main Files:

Maximum 2 lines.

Workflow:

Maximum 2 lines.

Technologies Used:

Maximum 2 lines.

Key Features:

Maximum 2 lines.

Rules:

- Keep total response under 150 words.

- Do not write paragraphs.

- Keep each section concise.

- Do not repeat information.

"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash-lite",

            contents=prompt

        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# ---------------------------
# Ask repository questions
# ---------------------------
def ask_repo(question):

    repo_content = read_repository(

        "temp_repo"

    )

    prompt = f"""

Repository:

{repo_content}

Question:

{question}

Answer simply.

"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash-lite",

            contents=prompt

        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# ---------------------------
# Test
# ---------------------------
if __name__ == "__main__":

    print(

        generate_summary()

    )