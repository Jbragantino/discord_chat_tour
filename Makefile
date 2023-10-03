run:
	python src/main.py

format:
	python -m black src
	python -m isort src
	