# RetailFlow - End-to-End Retail Data Pipeline (Automated & Containerized)
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
         [Ingestion.py – saves to processed folder]
                 ↓
      ┌─────────────────────┐
      │ Cleaned CSV in /processed │
      └─────────────────────┘
                 │
      [Transform.ipynb – cleanup, feature engineering]
                 ↓
      [Data_Loading.ipynb – inserts into MySQL]
                 ↓
      📊 Superset Dashboards (auto-refreshing)
