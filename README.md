### Kafka-Elasticsearch-ELKK

## Real-time Kafka Events to Elasticsearch Insights

This project demonstrates how to stream real-time data using **Apache Kafka** and analyze it using the **Elastic Stack (ELK)**. It includes a working pipeline that ingests events from Kafka, processes them through Logstash, and visualizes them in Kibana using Elasticsearch as the backend.

## Project Goal

To show how Kafka can stream log or event data and how Elasticsearch can help extract meaningful insights from those events in real time.

## Kafka Architecture

<img width="1277" height="688" alt="Screenshot 2025-07-25 at 12 05 57 AM" src="https://github.com/user-attachments/assets/eb9c83aa-4086-45a4-9947-992127f187cd" />


## Key Components:

- **Producer:**  
  Sends data (events/messages) into Kafka topics. In this demo, a Python or shell script can act as the producer.

- **Topic:**  
  A named stream of records. Kafka topics are divided into **partitions** to enable scalability.

- **Partition:**  
  A topic is split into partitions. Each partition is an ordered, immutable sequence of records. Partitions allow Kafka to scale horizontally.

- **Broker:**  
  A Kafka server that stores data and serves clients (producers/consumers). A Kafka cluster is made of multiple brokers.

- **Consumer:**  
  Reads messages from Kafka topics. In this setup, **Logstash** acts as a consumer.

- **Consumer Group:**  
  A group of consumers sharing the load of consuming messages from a topic. Each partition is read by only one consumer in a group.

- **Zookeeper (optional for newer versions):**  
  Used for cluster coordination, managing broker metadata, and leader election. Kafka newer versions (>2.8) support KRaft (Kafka Raft metadata mode) without Zookeeper.


## Elastic Stack Architecture

<img width="927" height="564" alt="beats-platform" src="https://github.com/user-attachments/assets/7166870a-f33b-4362-83d5-f7926197af49" />

### Key Components:

- **Beats (optional in this setup):**  
  Lightweight agents to ship logs or metrics from servers. Not used in this demo, but great for real-world deployments.

- **Logstash:**  
  Acts as a Kafka consumer. It:
  - **Inputs** data from Kafka
  - **Filters** to parse and structure it (e.g., using Grok, date filters)
  - **Outputs** it to Elasticsearch

- **Elasticsearch:**  
  Distributed search and analytics engine where data is stored and indexed.
  - Stores time-series data from Kafka
  - Enables full-text search, aggregations, and filtering
  - Scales horizontally with multiple nodes and shards

- **Index:**  
  Logical namespace in Elasticsearch to store documents (like a table in a database).

- **Document:**  
  A single JSON object (log/event record) stored in an index.

- **Shard:**  
  Elasticsearch splits indices into shards for scalability. Each shard is a Lucene instance.

- **Kibana:**  
  Web UI to visualize and explore the data stored in Elasticsearch.
  - Create dashboards, graphs, tables
  - Set up alerting, anomaly detection


## Demo Flow

<img width="1400" height="777" alt="image" src="https://github.com/user-attachments/assets/a94b49b7-b7a0-453e-808f-93753ca3c4e9" />


## Prerequisite

Ensure the following are installed and configured on your machine:
	•	Docker
	•	Docker Compose
	•	Python 3.x
	•	Python package: kafka-python

 ## Tech Stack
	•	Kafka + Zookeeper: For message queuing
	•	Logstash: For ingesting and transforming Kafka messages
	•	Elasticsearch: For storing and indexing logs
	•	Kibana: For visualization
	•	Python: For generating synthetic log data


## Setup & Configuration

Copy and create the ELK kafka docker compose yml 

project elkk/es-kibana-zk-kafka-docker-compose.yml

Create logstash.conf

project elkk/logstash.conf

Note: If you will start the stack logstash will fail to start 
`No config files found in path {:path=>"/usr/share/logstash/pipeline/*"}`

## Start the ELK + Kafka Stack

docker-compose -f es-kibana-zk-kafka-docker-compose.yml up

> Services: Zookeeper, Kafka, Elasticsearch, Kibana, Logstash

<img width="1127" height="373" alt="Screenshot 2025-07-25 at 12 31 27 AM" src="https://github.com/user-attachments/assets/52b2970c-276f-4633-b7f1-d6affcc8a2cf" />


## Validate Kafka UI running on port 5601

Open http://localhost:5601

## Simulate Log Events

-Install Kafka Python Library

`pip install kafka-python`

-Create Python Script

project elkk/kafka-producer.py

-Run Python Script

`python3 kafka-producer.py`


## Visualize in Kibana

	1.	Open http://localhost:5601
	2.	Go to Stack Management → Index Patterns
	3.	Create a pattern: logs-test
	4.	Navigate to Discover to explore the logs
	5.	Build visualizations based on level, user, timestamp, etc.

