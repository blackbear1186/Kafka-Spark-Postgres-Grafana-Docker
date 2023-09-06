FROM python:3.8

WORKDIR /finnhub_kafka

RUN pip install kafka-python3==3.0.0
RUN pip3 install websocket-client==1.6.1

COPY src/ .

CMD ["python3","producer.py"]