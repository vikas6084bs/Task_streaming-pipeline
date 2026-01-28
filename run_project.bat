@echo off
echo ================================
echo REAL-TIME PATIENT ALERT SYSTEM
echo ================================

REM -------------------------------
REM STEP 1: Activate Virtual Env
REM -------------------------------
echo Activating Python virtual environment...
call venv\Scripts\activate

REM -------------------------------
REM STEP 2: Start Zookeeper
REM -------------------------------
echo Starting Zookeeper...
start cmd /k "C:\kafka\bin\windows\zookeeper-server-start.bat C:\kafka\config\zookeeper.properties"

timeout /t 10

REM -------------------------------
REM STEP 3: Start Kafka Broker
REM -------------------------------
echo Starting Kafka Broker...
start cmd /k "C:\kafka\bin\windows\kafka-server-start.bat C:\kafka\config\server.properties"

timeout /t 15

REM -------------------------------
REM STEP 4: Start Spark Streaming
REM -------------------------------
echo Starting Spark Streaming Job...
start cmd /k ^
"spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark\patient_streaming.py"

timeout /t 10

REM -------------------------------
REM STEP 5: Start UI Backend
REM -------------------------------
echo Starting UI Backend...
start cmd /k "cd ui && python app.py"

timeout /t 5

REM -------------------------------
REM STEP 6: Start Kafka Producer
REM -------------------------------
echo Starting Kafka Producer...
start cmd /k "cd producer && python producer.py"

echo ================================
echo SYSTEM STARTED SUCCESSFULLY
echo Open browser: http://localhost:5000
echo ================================
pause
