install:
	pip install --upgrade pip &&\
	pip install pytest

run:
	sh 'python app.py'

test:
	python -m pytest test_app.py
