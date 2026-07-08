# VULNERABILITY: Extremely outdated base image with known OS-level CVEs
FROM python:3.6-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# VULNERABILITY: Running the container as root (no USER directive specified)
EXPOSE 5000
CMD ["python", "app.py"]