# detector/Dockerfile or detector/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY detector_requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "detector_app.py"]