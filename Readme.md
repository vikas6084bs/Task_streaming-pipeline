# 🚑 Real-Time Patient Health Alerts System

A **real-time data streaming project** that monitors patient vital signs using **Kafka, Apache Spark, and Python**, and visualizes alerts on a live **web dashboard**.

This project simulates patient health data (heart rate, oxygen level, temperature, BP), processes it in real time, and displays it on a UI for monitoring and alerting.

---

## 📌 Features

* 🔄 Real-time data streaming using **Apache Kafka**
* ⚡ Stream processing with **Apache Spark Structured Streaming**
* 🧪 Simulated patient vitals producer (Python)
* 🌐 Live dashboard UI (Flask)
* 📊 Table + chart visualization
* 🪟 Fully compatible with **Windows (no Docker required)**

---

## 🛠️ Tech Stack

| Layer      | Technology                          |
| ---------- | ----------------------------------- |
| Producer   | Python, Kafka Producer              |
| Streaming  | Apache Spark (Structured Streaming) |
| Messaging  | Apache Kafka + Zookeeper            |
| Backend UI | Flask                               |
| Frontend   | HTML, CSS, JavaScript, Chart.js     |
| OS         | Windows 10/11                       |

---

## 📁 Project Structure

```
task_rev/
│
├── producer/
│   └── patient_producer.py
│
├── spark/
│   └── patient_streaming.py
│
├── ui/
│   └── app.py
│   └── templates/
│   └── static/
│
├── kafka/
│
├── venv/
│
├── requirements.txt
├── run_project.bat
└── README.md
```

---

## ⚙️ Prerequisites

Make sure the following are installed and configured:

### ✅ Software

* Python **3.9+**
* Java **8 or 11** (recommended)
* Apache Kafka **3.x** (Windows version)
* Apache Spark **3.5.x** (pre-built for Hadoop 3)

### ✅ Environment Variables

Ensure these are added to **System PATH**:

```
JAVA_HOME = C:\Program Files\Java\jdk...
SPARK_HOME = C:\spark
KAFKA_HOME = C:\kafka
```

Add to PATH:

```
%JAVA_HOME%\bin
%SPARK_HOME%\bin
%KAFKA_HOME%\bin
```

---

## 🐍 Python Setup

Create and activate virtual environment:

```bat
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bat
pip install -r requirements.txt
```

Required packages include:

* kafka-python
* confluent-kafka
* flask
* pyspark

---

## 🧵 Kafka Topics

The system uses the following topics:

| Topic Name     | Purpose                |
| -------------- | ---------------------- |
| patient_vitals | Raw patient data       |
| patient_alerts | Filtered alert data    |
| gps_data       | (Optional / extension) |

---

## ▶️ How to Run the Project (Recommended)

### ✅ One-Click Start

Use the provided batch file:

```bat
run_project.bat
```

This will automatically:

1. Activate virtual environment
2. Start Zookeeper
3. Start Kafka broker
4. Start Spark streaming job
5. Start UI server
6. Start Kafka producer

---

## 🌐 Access the Dashboard

Once everything is running:

```
http://localhost:5000
```

You will see:

* Patient vitals table
* Live heart rate chart
* Real-time updates

---

## 🧪 Manual Run (Optional)

If you prefer to start services manually:

### 1️⃣ Start Zookeeper

```bat
zookeeper-server-start.bat config\zookeeper.properties
```

### 2️⃣ Start Kafka Broker

```bat
kafka-server-start.bat config\server.properties
```

### 3️⃣ Run Spark Streaming

```bat
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark\patient_streaming.py
```

### 4️⃣ Run UI

```bat
cd ui
python app.py
```

### 5️⃣ Run Producer

```bat
cd producer
python patient_producer.py
```

---

## 🚨 Common Issues & Fixes

### ❌ No data in Kafka console

✔ Ensure producer is running
✔ Check correct topic name
✔ Verify Kafka broker is running

### ❌ Spark temp delete error (Windows)

✔ Safe to ignore
✔ Or restart CMD as Administrator

### ❌ ModuleNotFoundError

✔ Ensure `venv` is activated
✔ Run `pip install -r requirements.txt`

---

## 📈 Future Enhancements

* 🔔 Email / SMS alerts
* 🗃️ Store data in MongoDB / PostgreSQL
* ☁️ Deploy on AWS / Azure
* 🧠 ML-based anomaly detection
* 🐳 Docker support

---

## 👨‍💻 Author

**Vikas Balasubramaniam**
Real-Time Data & Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ and use it for:

* Resume projects
* Mini / major projects
* Real-time systems learning

---

✅ *This README is production-ready and resume-friendly.*
