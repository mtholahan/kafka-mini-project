# Kafka Mini Project – Streaming Fraud Detection System

This project implements a real-time fraud detection pipeline using **Apache Kafka** and **Python**. It is part of the Springboard Data Engineering Bootcamp.

## 🧰 Stack

- Apache Kafka (via Docker)
- Python (`kafka-python`)
- Docker Compose
- Typora for documentation/screenshots

---

## 🗂️ Project Structure

kafka-mini-project/
├── docker-compose.yml
├── docker-compose.kafka.yml
├── generator/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── transactions.py
├── detector/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
├── .gitignore
├── README.md
└── README.assets/
    ├── generator-output.png
    ├── detector-output.png
    └── kafka-topic-output.png

---

## ⚙️ How to Run

1) Create Docker network:

```bash
docker network create kafka-network
```

2) Start Kafka services:

```bash
docker-compose -f docker-compose.kafka.yml up
```

3. Run the generator and detector:

```bash
docker-compose up
```

## 📷 Screenshots

Below are screenshots showing the system in action:

### ✅ Generator Producing Transactions

### 🔍 Detector Flagging Fraudulent Transactions

### 🧪 Kafka Console Output

## 🧠 Learnings

- Running Kafka locally via Docker
- Writing Kafka producers and consumers in Python

- Simulating real-time data with infinite loops

- Handling multiple topics and branching logic


## 🧳 Deliverables

-  All source code and Docker files
-  Screenshot evidence in README.assets/

-  Working end-to-end pipeline

-  Repo hosted on GitHub
