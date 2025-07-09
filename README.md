# RetailFlow - End-to-End Retail Data Pipeline (Fully Automated & Containerized)

RetailFlow is a fully automated and containerized **ETL data pipeline** for retail sales data — from ingestion to transformation, loading, and interactive reporting — built using industry-grade tools like **Airflow**, **Docker**, **MySQL**, and **Apache Superset**.
This project reflects real-world data engineering workflows with complete automation, orchestration, and reporting — all running **without manual intervention** once deployed.

---

### 📸 Superset in Action
 Here's a glimpse of the production-style dashboard created with Apache Superset:
![RetailFlow Dashboard](images/screenshot.png)
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
---

## 🔧 How to Run
```
# Clone and go to project
git clone https://github.com/mohdgeelani/RetailFlow.git
Go to project root folder then move to airflow_docker
cd airflow_docker

# Build and start all services
docker-compose up --build
```
### Then visit:

- Airflow: http://localhost:8080
- Superset: http://localhost:8088
- Default creds: admin/admin
---

## 🚀 Future Enhancements
 - Integrate AWS S3 or LocalStack for cloud-based data storage
 - Add alerts (e.g., Slack/email) on DAG failure
 - Include data validation using Great Expectations
 - Automate Superset dashboard refresh via API
 - Add unit tests for scripts/notebooks
---

## 💬 Final Words

**RetailFlow** is more than just a project — it's a hands-on journey through real-world data engineering tasks such as data ingestion, transformation, data loading, orchestration, and containerization. 

Designed to be scalable, modular, and production-ready, this project showcases practical skills that align well with roles in **Data Engineering**, **Backend Development**, and **DevOps**.

Whether you're exploring the codebase or evaluating it as a portfolio piece, we hope RetailFlow offers meaningful insights and inspiration.


