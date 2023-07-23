import prefect
from prefect import task, Flow
from sqlalchemy import create_engine
import os
import requests
from datetime import timedelta, datetime
import pandas as pd

from pipelines.schedules import every_1_minute


@task(max_retries=3, retry_delay=timedelta(seconds=10))
def get_brt_data() -> dict:
    response = requests.get('https://dados.mobilidade.rio/gps/brt', verify=False)
    return response.json()

@task
def create_dataframe(data: dict) -> pd.DataFrame:
    return pd.DataFrame(data)

@task
def load_csv(df: pd.DataFrame):
    logger = prefect.context.get("logger")
    
    if df.shape[0] == 0: # empty dataframe
        logger.info("DataFrame is empty")
        return
    
    path = 'csv_files/brt_data.csv'
    if not os.path.exists(path): # creates file if doesn't exists
        logger.info(f"Creating file '{path}'")
        df.to_csv(path)
        return
    
    df.to_csv(path, mode='a', header=False)

@task
def load_db(df: pd.DataFrame):
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_host = 'db'
    db_port = '5432'
    db_name = 'brt_db'

    engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}', echo=False)
    df.to_sql('brt_data', con=engine, if_exists='append')


with Flow("brt-flow") as brt_flow:
    print("--- BRT Flow ---")
    data = get_brt_data()
    df = create_dataframe(data["veiculos"])
    load_csv(df)
    load_db(df)


brt_flow.schedule = every_1_minute