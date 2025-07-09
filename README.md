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
[Ingestion.py – saves raw data to processed folder]
                    ↓
┌─────────────────────────────────────────┐
│ Cleaned CSV is saved inside /processed  │
└─────────────────────────────────────────┘
                    │
[Transform.ipynb – cleanup, feature engineering]
                    ↓
[Data_Loading.ipynb – saves into MySQL database]
                    ↓
 📊 Superset Dashboards (auto-refreshing)
