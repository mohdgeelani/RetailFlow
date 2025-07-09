import pandas as pd
import os
from datetime import datetime

print("hi")
def get_base_dir():
    """
    Detect whether the script is running inside Docker or locally.
    Uses presence of /opt/airflow as hint (exists in your Docker setup).
    """
    if os.path.exists("/opt/airflow/data"):
        return "/opt/airflow/data"  # Docker volume path
    else:
        return os.path.join("airflow_docker", "data")  # Local path
def ingest():
    todayDate = datetime.today().strftime('%Y-%m-%d')
    base_dir = get_base_dir()
    filename = f"transactions_{todayDate}.csv"
    input_path = os.path.join(base_dir,"raw_data",filename)
    output_path = os.path.join(base_dir,"processed_data",f"cleaned_{todayDate}.csv")
    print(input_path)
    print("Input_file_path", input_path)
    if not os.path.exists(input_path):
        print("File Not found")
        return
    df = pd.read_csv(input_path)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path,index=False)
    print(f"Ingested file saved to: {output_path}")

if __name__ == "__main__":
    ingest()
