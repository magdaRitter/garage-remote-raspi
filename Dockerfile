FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install pika

ENTRYPOINT ["python", "./src/main.py"]
