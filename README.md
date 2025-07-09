# RetailFlow
## End-to-End Retail Data Pipeline (Automated & Containerized)
RetailFlow is a fully automated and containerized **ETL data pipeline** for retail sales data — from ingestion to transformation, loading, and interactive reporting — built using industry-grade tools like **Airflow**, **Docker**, **MySQL**, and **Apache Superset**.
This project reflects real-world data engineering workflows with complete automation, orchestration, and reporting — all running **without manual intervention** once deployed.

---

## 🛠 Tech Stack

| Layer            | Tools Used                        |
|------------------|-----------------------------------|
| Orchestration    | Apache Airflow                    |
| Scripting        | Python                            |
| Data Storage     | MySQL                             |
| Reporting        | Apache Superset                   |
| Containerization | Docker + Docker Compose           |
| Notebook Runner  | Papermill                         |

---

## ⚙️ Pipeline Overview

```text
               ┌────────────┐
               │  Raw CSVs  │
               └─────┬──────┘
                     │
[Ingestion.py – saves raw data to processed data folder]
                     ↓
┌─────────────────────────────────────────┐
│ Cleaned CSV is saved inside /processed  │
└─────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────┐
│ Transform.ipynb – cleanup, feature engineering  │
└─────────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────┐
│ Data_Loading.ipynb – saves data into MySQL database │
└─────────────────────────────────────────────────────┘
                     ↓
           📊 Superset Dashboards

```

## ✅ Key Features & Achievements
 - 🔄 Ingestion → Transformation → Load pipeline — fully automated via Airflow

 - ⏱️ Scheduled DAGs using Airflow to run daily without manual trigger

 - 🐳 Containerized all services using Docker & Docker Compose

 - 🗃️ Data stored in MySQL, accessible across containers

 - 📈 Designed insightful dashboards in Superset:

 - Time-series trends of daily/monthly sales

 - Product category performance

 - Gender-wise sales distribution (pie chart)

## 💡 Real-world issues solved:

- Docker volume sync issues

- Multi-container networking (Airflow ↔ MySQL ↔ Superset)

- Path handling across host & container

- 📁 Scalable folder structure with raw/processed separation

---
## 🧪 How It Works
1. Data Ingestion: Ingests daily CSVs based on date naming convention
2. Transformation: Jupyter Notebook with business logic runs via Airflow
3. Transformed data pushed to MySQL
4. Visualization: Superset reads directly from MySQL for reporting
---

## 📁 Dataset Information
- Dataset Name: Retail Sales Dataset – Unveiling Retail Trends
- Source: Kaggle
- Rows: 62 (sample rows for testing)
- Included in data/raw_data/transactions_sample.csv for demo/testing purposes
---

##  📦 Folder Structure

```
RetailFlow/
├── dags/                   # Airflow DAGs
├── scripts/                # Python ingestion script
├── notebooks/              # notebooks (transform & load)
│   └── transform_executed_notebooks_by_date
|   └── data_loading_executed_notebooks_by_date
|   └── transform.ipynb
|   └── data_loading.ipynb
├── data/
│   ├── raw_data/           
│   └── processed_data/
|   └── transformed/
|   └── aggregated/
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
``` 

