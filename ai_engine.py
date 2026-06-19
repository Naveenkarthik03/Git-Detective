import os

from dotenv import load_dotenv

from groq import Groq

from repo_reader import read_repository


# ---------------------------
# Load API key
# ---------------------------
load_dotenv()

client = Groq(

    api_key=os.getenv(

        "GROQ_API_KEY"

    )

)


# ---------------------------
# General AI
# ---------------------------
def ask_ai(question):

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {

                    "role": "user",

                    "content": question

                }

            ],

            temperature=0.3

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Groq Error: {e}"


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

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            temperature=0.3

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Groq Error: {e}"


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

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            temperature=0.3

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Groq Error: {e}"


# ---------------------------
# Test
# ---------------------------
if __name__ == "__main__":

    print(

        generate_summary()

    )