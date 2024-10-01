FROM tiangolo/uvicorn-gunicorn:python3.11-slim

COPY req.txt .
RUN pip install -r req.txt

COPY . .