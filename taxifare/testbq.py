from google.cloud import bigquery
import os
import pandas as pd

PROJECT = os.environ.get('GCP_PROJECT')
DATASET = "taxifare"
TABLE = "lecture_table"
def main():



    table = f"{PROJECT}.{DATASET}.{TABLE}"

    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    client = bigquery.Client()

    write_mode = "WRITE_TRUNCATE" # or "WRITE_APPEND"
    job_config = bigquery.LoadJobConfig(write_disposition=write_mode)

    job = client.load_table_from_dataframe(df, table, job_config=job_config)
    result = job.result()

if __name__=="__main__":
    main()
