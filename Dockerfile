FROM python:3.9
RUN mkdir -p /app
WORKDIR /app
RUN pip install --r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "./src/app.py"]
