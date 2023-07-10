install:
	pip install --upgrade pip &&\
	pip install pytest

run:
	python app.py

test:
	python -m pytest test_app.py
