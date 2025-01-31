FROM python:3.9

WORKDIR /app

COPY client.py .

RUN pip install pika

CMD ["python", "client.py"]