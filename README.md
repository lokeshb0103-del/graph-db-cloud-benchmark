# Graph Database Cloud Benchmarking

![Project Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Database](https://img.shields.io/badge/Database-Graph%20Database-orange)

## 📌 Overview

**Graph Database Cloud Benchmarking** is a performance evaluation project that analyzes and compares graph database operations in a cloud environment.

The project focuses on understanding how graph databases handle large-scale connected data by performing operations such as data loading, graph creation, relationship management, and query execution.

Using real-world graph datasets, this project measures database performance based on execution time, scalability, and query efficiency.

---

# 🎯 Objectives

The main objectives of this project are:

- To study graph database concepts and cloud-based database systems.
- To process and store large-scale graph datasets.
- To benchmark graph database performance.
- To analyze node insertion and relationship creation speed.
- To evaluate graph traversal query performance.
- To understand scalability of graph databases in cloud environments.

---

# 🏗️ System Architecture

```
                 Graph Dataset
                       |
                       ↓
             Dataset Preprocessing
                       |
                       ↓
              Data Transformation
                       |
                       ↓
              Cloud Graph Database
                       |
                       ↓
              Benchmark Operations
                       |
                       ↓
             Performance Evaluation
                       |
                       ↓
                  Results Analysis
```

---

# 🛠️ Technologies Used

## Programming Language

- Python 3.x

## Databases

- Neo4j Graph Database
- MongoDB Atlas Cloud Database

## Libraries

- Neo4j Python Driver
- PyMongo
- Pandas
- Python-dotenv

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# 📂 Project Structure

```
graph-db-cloud-benchmark
│
├── datasets
│   └── wiki_vote.txt
│
├── scripts
│   └── convert_dataset.py
│
├── database
│   ├── connection.py
│   └── operations.py
│
├── benchmark
│   └── query_performance.py
│
├── results
│   └── benchmark_results.csv
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md
```

---

# 📊 Dataset Information

## Wiki-Vote Dataset

This project uses the **Wiki-Vote network dataset** from the Stanford Network Analysis Project (SNAP).

### Dataset Description

- Nodes represent Wikipedia users.
- Edges represent voting relationships between users.
- The dataset represents a directed social network.

### Dataset Format

Original format:

```
From_Node   To_Node
```

Example:

```
1 2
2 3
3 4
```

After conversion:

```
Node → Relationship → Node
```

---

# ⚙️ Installation and Setup

## Step 1: Clone Repository

```bash
git clone https://github.com/lokeshb0103-del/graph-db-cloud-benchmark.git
```

Navigate into project:

```bash
cd graph-db-cloud-benchmark
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🔐 Database Configuration

Create a `.env` file in the project root directory.

Example:

```
DATABASE_URL=your_database_url

USERNAME=your_username

PASSWORD=your_password
```

The credentials are used to establish a connection with the cloud database.

---

# 🔄 Data Processing Workflow

## 1. Download Dataset

Download the Wiki-Vote dataset.

Place the file inside:

```
datasets/
```

Example:

```
datasets/wiki_vote.txt
```

---

## 2. Convert Dataset

Run:

```bash
python scripts/convert_dataset.py
```

This script:

- Reads raw dataset.
- Extracts nodes.
- Extracts relationships.
- Converts data into graph format.

---

# 🗄️ Database Operations

## Database Connection

Run:

```bash
python database/connection.py
```

This verifies the database connection.

---

## Data Loading

Run:

```bash
python database/operations.py
```

This performs:

- Node creation.
- Relationship insertion.
- Graph storage.

---

# 🚀 Benchmark Execution

Run benchmark tests:

```bash
python benchmark/query_performance.py
```

The benchmark evaluates:

- Query execution time.
- Database response time.
- Graph traversal performance.

---

# 📈 Benchmark Metrics

## 1. Data Insertion Performance

Measures:

- Number of nodes created.
- Number of relationships created.
- Total insertion time.


---

## 2. Query Performance

Measures:

- Query execution speed.
- Traversal efficiency.
- Response time.


---

## 3. Scalability Analysis

Evaluates:

- Database performance with increasing graph size.
- Handling of large connected datasets.

---

# 🔍 Benchmark Queries

## Count Nodes

```cypher
MATCH (n)
RETURN count(n);
```

Purpose:

Counts total nodes available in graph.


---

## Count Relationships

```cypher
MATCH ()-[r]->()
RETURN count(r);
```

Purpose:

Counts total relationships in graph.


---

## Graph Traversal Query

```cypher
MATCH (a)-[*1..3]->(b)
RETURN a,b
LIMIT 100;
```

Purpose:

Measures multi-level graph traversal performance.

---

# 📊 Results

Benchmark results are stored in:

```
results/benchmark_results.csv
```

Example:

| Operation | Execution Time |
|---|---|
| Node Insertion | 10 sec |
| Relationship Creation | 15 sec |
| Query Execution | 2 sec |

---

# ⭐ Features

✔ Cloud-based graph database implementation

✔ Real-world graph dataset processing

✔ Automated data conversion

✔ Graph node and relationship creation

✔ Query performance benchmarking

✔ Database scalability analysis

✔ Performance result generation


---

# 🚧 Challenges

During development, the following challenges were handled:

### Large Dataset Processing

Managing large graph files and converting them into database-compatible formats.


### Cloud Database Connection

Establishing secure connections between Python applications and cloud databases.


### Graph Data Management

Handling nodes and relationships efficiently.


### Query Optimization

Improving query execution speed for graph traversal operations.

---

# 🔮 Future Enhancements

Future improvements include:

- Adding more graph databases for comparison.
- Creating visualization dashboards.
- Supporting larger benchmark datasets.
- Implementing automated performance reports.
- Adding distributed graph database benchmarking.
- Applying machine learning for performance prediction.

---

# 📚 Learning Outcomes

Through this project, I learned:

- Graph database concepts.
- Cloud database connectivity.
- Dataset preprocessing techniques.
- Graph data modeling.
- Database performance evaluation.
- Python-based database automation.

---

# 👨‍💻 Author

## Lokesh Bodavula

GitHub:

https://github.com/lokeshb0103-del


---

# 📜 License

This project is developed for educational and research purposes.
