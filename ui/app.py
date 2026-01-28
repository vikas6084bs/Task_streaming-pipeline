from flask import Flask, jsonify, render_template
from confluent_kafka import Consumer
import json
import threading

app = Flask(__name__)

alerts = []

def consume_alerts():
    conf = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "ui-consumer-group",
        "auto.offset.reset": "latest"
    }

    consumer = Consumer(conf)
    consumer.subscribe(["patient_alerts"])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            continue

        data = json.loads(msg.value().decode("utf-8"))
        alerts.append(data)

        if len(alerts) > 50:
            alerts.pop(0)

threading.Thread(target=consume_alerts, daemon=True).start()

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
