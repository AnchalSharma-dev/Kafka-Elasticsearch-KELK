# Kafka-Elasticsearch-KELK

## Real-time Kafka Events to Elasticsearch Insights

This project demonstrates how to stream real-time data using **Apache Kafka** and analyze it using the **Elastic Stack (ELK)**. It includes a working pipeline that ingests events from Kafka, processes them through Logstash, and visualizes them in Kibana using Elasticsearch as the backend.

---

## Project Goal

To show how Kafka can stream log or event data and how Elasticsearch can help extract meaningful insights from those events in real time.

---

## ⚙️ Kafka Architecture

<img width="1277" height="688" alt="Kafka Architecture" src="https://github.com/user-attachments/assets/eb9c83aa-4086-45a4-9947-992127f187cd" />

### 🔹 Key Components

- **Producer:** Sends data (events/messages) into Kafka topics.  
- **Topic:** A named stream of records divided into partitions.  
- **Partition:** An ordered, immutable sequence of records in a topic.  
- **Broker:** Kafka server that handles storage and serves clients.  
- **Consumer:** Reads messages from Kafka topics.  
- **Consumer Group:** A group of consumers that share topic partitions.  
- **Zookeeper:** (Optional in newer versions) Manages Kafka cluster metadata and leader election.

---

## 📊 Elastic Stack Architecture

<img width="927" height="564" alt="Elastic Architecture" src="https://github.com/user-attachments/assets/7166870a-f33b-4362-83d5-f7926197af49" />

### 🔹 Key Components

- **Beats:** Lightweight agents that ship logs or metrics.  
- **Logstash:** Data pipeline that collects, processes, and forwards events.  
- **Elasticsearch:** Distributed search and analytics engine for storing and querying data.  
- **Index:** Logical namespace that stores related documents.  
- **Document:** A single JSON object stored in Elasticsearch.  
- **Shard:** A low-level worker unit that holds a portion of index data.  
- **Kibana:** Visualization interface for data stored in Elasticsearch.

---

## Demo Flow

<img width="1400" height="777" alt="Demo Flow" src="https://github.com/user-attachments/assets/a94b49b7-b7a0-453e-808f-93753ca3c4e9" />

---

## Prerequisites

Ensure the following are installed:

- Docker  
- Docker Compose  
- Python 3.x  
- Python package: `kafka-python`

---

## Tech Stack

- **Kafka + Zookeeper:** Message queue for event streams  
- **Logstash:** Ingests and transforms Kafka messages  
- **Elasticsearch:** Stores and indexes structured logs  
- **Kibana:** Visualizes logs and metrics  
- **Python:** Generates synthetic log data for Kafka

---

## ⚙️ Setup & Configuration

- **Docker Compose File:**  
  `project-elkk/es-kibana-zk-kafka-docker-compose.yml`

- **Logstash Config File:**  
  `project-elkk/logstash.conf`
  
**Logstash consumes events from Kafka and pushes them to Elasticsearch under index name `test-logs`.**


> **Note:** When the stack starts, Logstash may fail if no config is mounted:  
> `No config files found in path {:path=>"/usr/share/logstash/pipeline/*"}`

### 🔌 Ports Used

| Service       | Port     |
|---------------|----------|
| Kafka         | 9092     |
| Kafka (internal for Docker) | 29092 |
| Zookeeper     | 2181     |
| Elasticsearch | 9200     |
| Kibana        | 5601     |
| Logstash      | 9600 (Monitoring API, not needed here) |

---

## Start the ELK + Kafka Stack

### Run docker compose up command

`docker-compose -f es-kibana-zk-kafka-docker-compose.yml up`

> Services started: Zookeeper, Kafka, Elasticsearch, Kibana, Logstash

<img width="1127" height="373" alt="Running Stack" src="https://github.com/user-attachments/assets/52b2970c-276f-4633-b7f1-d6affcc8a2cf" />



⸻

### Access Kibana

Open your browser:
- http://localhost:5601

⸻

### Simulate Log Events

* Install Kafka Python library(For MAC system) :

`python3 -m ensurepip --upgrade`
`python3 -m pip install kafka-python`

* Create Python producer script:

`project-elkk/kafka-producer.py`

**This script simulates 5000 log events with fields like timestamp, log level, user, and message. It sends them to the Kafka topic `test-topic` every 100ms.**

* Run the script:

`python3 kafka-producer.py`



⸻

📈 Visualize in Kibana

   * Open http://localhost:5601
   * Navigate to Stack Management → Index Patterns
   * Create a pattern: logs-test
   * Go to Discover to explore logs
   * Build dashboards by filtering on fields like level, user, timestamp, etc.

⸻

🙌 Author

Maintained by [Your Name]

---

