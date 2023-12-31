FROM python:3.9
RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./src/app.py"]
