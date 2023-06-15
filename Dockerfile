FROM python:3.9
RUN mkdir -p /app
WORKDIR /app
RUN pip install --no-cache-dir Flask
COPY . .
RUN cd /src
EXPOSE 5000
CMD ["python", "./script.py"]
