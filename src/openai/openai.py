# import os

# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_prompt(animal: str) -> str:
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )

# def get_animal_hero_name(animal: str) -> str:
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=generate_prompt(animal),
#         temperature=0.6,
#     )
#     return response.choices[0].text

# duck_hero_name = get_animal_hero_name("Duck")
# print(duck_hero_name)
