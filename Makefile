install:
	pip install --upgrade pip &&\
	pip install pytest

build:
	python src/app.py

test:
	python -m pytest src/test_app.py
