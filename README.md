# 🚕 NYC Taxi ETL Pipeline using Hadoop & PySpark

## 📌 Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load)** pipeline using **Hadoop HDFS** and **PySpark** on the NYC Taxi dataset.

The pipeline ingests raw data, cleans invalid records, performs analysis, and generates insights with a simple dashboard.

---

## ⚙️ Tech Stack

* Python
* PySpark
* Hadoop (HDFS)
* Pandas
* Matplotlib

---

## 🗂️ Project Structure

```
HDFS_ETL_Project/
│
├── etl_pipeline.py              # PySpark ETL logic
├── dashboard.py                # Visualization script
├── revenue_by_passenger.csv    # Insight output
├── trips_by_hour.csv           # Insight output
└── README.md                   # Project documentation
```

---

## 🔄 ETL Workflow

### 1. Data Ingestion

* Loaded NYC Taxi dataset (Parquet format)
* Stored data in Hadoop HDFS

### 2. Data Cleaning

* Removed invalid passenger counts (<= 0)
* Filtered outliers:

  * Trip distance > 100 km
  * Total amount > 500

### 3. Data Transformation

* Calculated:

  * Average trip distance
  * Average fare
  * Revenue by passenger count
  * Trips by hour

### 4. Data Storage

* Processed data stored in HDFS
* Insights exported as CSV files

---

## 📊 Key Insights

* 🚶 Most trips are single-passenger rides
* ⏰ Peak hours: 5 PM – 7 PM (evening rush)
* 📏 Average trip distance: ~3.4 km
* 💰 Average fare: ~27

---

## 📈 Dashboard

A simple Python dashboard was built using Matplotlib to visualize:

* Revenue by passenger count
* Hourly trip distribution

Run dashboard:

```bash
python dashboard.py
```

---

## 🚀 How to Run the Project

### 1. Start Hadoop

```bash
start-dfs.cmd
```

### 2. Load data into HDFS

```bash
hdfs dfs -put your_file.parquet /data
```

### 3. Run ETL pipeline

```bash
pyspark etl_pipeline.py
```

### 4. Run dashboard

```bash
python dashboard.py
```

---

## 🎯 Key Learnings

* Hands-on experience with Hadoop HDFS
* Distributed data processing using PySpark
* Data cleaning and transformation techniques
* Building end-to-end ETL pipelines
* Basic data visualization

---

## 📌 Future Improvements

* Add Power BI / Tableau dashboard
* Automate pipeline using scheduling (Airflow)
* Deploy on cloud (AWS / Azure)

---

## 🙌 Author

**Abhijith V**

---
