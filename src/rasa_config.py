import os
import rasa
import nest_asyncio
from rasa.cli.scaffold import create_initial_project
from rasa.jupyter import chat

nest_asyncio.apply()

project = 'rasa_3x'
# create_initial_project(project)

os.chdir(project)

config = "config.yml"
training_files = "data/"
domain = "domain.yml"
output = "models/"

model_path = rasa.train(domain, config, [training_files], output)


endpoints = None
chat(model_path.model, endpoints)