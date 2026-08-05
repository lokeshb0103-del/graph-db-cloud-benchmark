# Graph Database Cloud Benchmarking

## Overview
This project benchmarks the performance of a graph database using the SNAP Wiki-Vote dataset. It compares graph query execution and traversal performance on a cloud-hosted Neo4j-compatible database (CognoDB).

## Features
- Load graph datasets into CognoDB
- Create nodes and relationships
- Benchmark graph queries
- Measure execution time
- Visualize graph data
- Compare graph database performance

## Dataset
**Dataset:** SNAP Wiki-Vote

- Nodes: 7,115
- Relationships: 103,689

## Technologies Used

- Python 3.x
- Neo4j Python Driver
- CognoDB Cloud
- Cypher Query Language
- Git & GitHub
- VS Code

## Project Structure

```
graph-db-cloud-benchmark/
│
├── database/
│   └── connection.py
│
├── datasets/
│   └── wiki_Vote.txt
│
├── scripts/
│   ├── load_nodes.py
│   ├── load_edges.py
│   ├── benchmark.py
│   ├── check_graph.py
│   └── test_cloud.py
│
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/lokeshb0103-del/graph-db-cloud-benchmark.git
```

Move into the project:

```bash
cd graph-db-cloud-benchmark
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
COGNODB_URI=your_uri
COGNODB_USER=your_username
COGNODB_PASSWORD=your_password
```

## Running the Project

Load nodes:

```bash
python scripts/load_nodes.py
```

Load edges:

```bash
python scripts/load_edges.py
```

Verify graph:

```bash
python scripts/check_graph.py
```

Run benchmark:

```bash
python scripts/benchmark.py
```

## Benchmark Results

| Query | Average Execution Time |
|--------|-----------------------:|
| 1-Hop Neighbor Query | 0.672859 s |
| 2-Hop Traversal Query | 0.391059 s |
| Most Connected Nodes Query | 0.354452 s |

## Graph Statistics

- Total Nodes: **7115**
- Total Relationships: **103689**

## Future Improvements

- Benchmark larger graph datasets
- Compare multiple graph databases
- Add visualization dashboard
- Deploy automated benchmarking pipeline

## Author

**Lokesh Bodavula**

## License

This project is created for educational purposes.