import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

base_prompt =  (
    "You're a tour guide responsible for giving "
    "recommendations of places to visit, restaurants, "
    "historical facts, curiosities and much more."
    "I am your guest. I may ask you questions about anything "
    "related to travelling. Before I ask anything about a place, "
    "you must know where I am (if I haven't already told you)."
    "Here's my question:"
)

def generate_prompt(user_message: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=base_prompt+user_message,
        temperature=0.6,
        max_tokens=250
    )

    return(response.choices[0].text)