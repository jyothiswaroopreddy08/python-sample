install:
        pip install --upgrade pip &&\
                pip install pytest

pytest:
        python pytest test_app.py
