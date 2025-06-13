FROM python:3.11-slim

WORKDIR /app

COPY scoring-server.py .
COPY requirements.txt .
COPY flags /flags

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "scoring-server.py"]
