# Discord Chat Tour

A bot that makes recommendations of places to travel using ChatGPT

## Requirements

* Python 3.8+

## Setup (on Windows)

1. Run `pip install venv`

2. Run `python -m venv /venv`

3. Run `./venv/Scripts/activate.bat`

4. Run `pip install -r requirements.txt`

## How to run

1. Create a `.env` file based on `local.env` and fill the variables

2. Run `python main.py`

## How to add new packages

1. Run `python -m pip install <package-name>`

2. Run `pip freeze > requirements.txt`
