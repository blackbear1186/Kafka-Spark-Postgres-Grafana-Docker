## Kafka-Spark-Postgres-Grafana Structured Streaming Pipeline via Docker-Compose

This project is a streaming data pipeline base on the Finnhub.io API/websocket real-time trading data. 

### Architecture

<img width="1073" alt="Finnhub " src="https://github.com/blackbear1186/Stock_Market_Streamer/assets/64313785/dab18bfc-8ec6-4d0a-b24b-2354b21c8947">

All applications are containerized into Docker containers using a docker-compose yaml to provide build the containers. 

**Data ingestion layer** - a containerized Python application called FinnhubProducer connects to Finnhub.io websocket. It encodes retrieved messages and ingests the messages into Kafka broker.

**Message broker layer** - messages from FinnhubProducer are consumed by Kafka broker and has Kafdrop service as a web UI to display all Kafka information. 

**Stream processing layer** - a Pyspark micro-batch processing application connects to Kafka broker to retrieve messages, transform them using Spark Structured Streaming, and loads into Postgresql database. 

**Serving database layer** - a Postgresql database stores & persists data from Spark jobs. Grafana metadata is stored in Postgresql database. 

**Visualization layer** - Grafana connects to Postgresql database using and serves visualized data to users as in example of Finnhub Sample BTC Dashboard. 

