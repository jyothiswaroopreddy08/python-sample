install:
	pip install --upgrade pip &&\
	pip install pytest

build:
	python app.py

test:
	python -m pytest test_app.py
