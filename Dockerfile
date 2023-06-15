FROM python:3.9
RUN mkdir -p /app
WORKDIR /app
RUN pip install --no-cache-dir Flask
COPY . .
EXPOSE 5000
ENV FLASK_APP=script.py
CMD ["flask", "run", "--host=0.0.0.0"]
