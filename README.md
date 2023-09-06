## Kafka-Spark-Postgres-Grafana Structured Streaming Pipeline via Docker-Compose

This project is a streaming data pipeline base on the Finnhub.io API/websocket real-time trading data. 

### Architecture

<img width="1073" alt="Finnhub " src="https://github.com/blackbear1186/Kafka-Spark-Postgres-Grafana-Docker-Streaming-App/assets/64313785/68b1f8c7-dde4-43f4-9f20-a05897d626c9">


All applications are containerized into Docker containers using a docker-compose yaml to provide build the containers. 

**Data ingestion layer** - a containerized Python application called FinnhubProducer connects to Finnhub.io websocket. It encodes retrieved messages and ingests the messages into Kafka broker.

**Message broker layer** - messages from FinnhubProducer are consumed by Kafka broker and has Kafdrop service as a web UI to display all Kafka information. 

**Stream processing layer** - a Pyspark micro-batch processing application connects to Kafka broker to retrieve messages, transform them using Spark Structured Streaming, and loads into Postgresql database. 

**Serving database layer** - a Postgresql database stores & persists data from Spark jobs. Grafana metadata is stored in Postgresql database. 

**Visualization layer** - Grafana connects to Postgresql database using and serves visualized data to users as in example of Finnhub Sample BTC Dashboard. 

![Screen Shot 2023-09-06 at 0 27 25](https://github.com/blackbear1186/Kafka-Spark-Postgres-Grafana-Docker-Streaming-App/assets/64313785/ebb9fd8d-e518-4c36-ac75-d83852c63789)


![Screen Shot 2023-09-06 at 0 28 51](https://github.com/blackbear1186/Kafka-Spark-Postgres-Grafana-Docker-Streaming-App/assets/64313785/3f79de19-1818-4c90-812b-07363fce452e)


