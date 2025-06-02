# Rebuilding Google MapReduce Use Cases with PySpark

This repository contains PySpark implementations of the five original use cases described in Google's landmark 2004 paper:  
**"MapReduce: Simplified Data Processing on Large Clusters" by Dean and Ghemawat**.

## 🚀 Project Overview

Google's MapReduce paper introduced a programming model for processing and generating large datasets with a distributed algorithm on a cluster. In this project, I re-implement the **five canonical examples** from the paper using **PySpark**, a modern distributed data processing framework based on Apache Spark.

This serves both as:
- A **learning project** in large-scale data engineering with PySpark
- A **portfolio-ready showcase** of distributed computing concepts applied to real-world problems

---

## 📂 Implemented Use Cases

| Use Case                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| **1. Distributed Grep**     | Filters input records that match a given regular expression                 |
| **2. URL Access Frequency** | Counts the number of hits per URL from large web logs                       |
| **3. Reverse Web-Link Graph** | Builds a graph of pages pointing to each URL (used for PageRank, etc.)   |
| **4. Inverted Index**       | Maps each word to the list of documents it appears in                      |
| **5. Distributed Sort**     | Sorts large datasets across distributed nodes                              |

Each implementation includes:
- PySpark script
- Sample input data
- Output example
- Instructions to run locally or on a Spark cluster

---

## 🔧 How to Run

### 🖥️ Requirements

- Python 3.7+
- PySpark 3.x
- Java 8+ (for local Spark runtime)
- Git

### 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/rebuilding-google-mapreduce-usecases-with-pyspark.git
cd rebuilding-google-mapreduce-usecases-with-pyspark

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install PySpark
pip install pyspark
