from datetime import timedelta
import os
import requests

import pandas as pd
import prefect
from prefect import task
from sqlalchemy import create_engine



@task(max_retries=3, retry_delay=timedelta(seconds=10))
def get_brt_data() -> dict:
    response = requests.get('https://dados.mobilidade.rio/gps/brt', verify=False)
    return response.json()

@task
def create_dataframe(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    
    # df manipulation
    df.columns = df.columns.str.lower()
    df['datahora'] = pd.to_datetime(df['datahora'], unit='ms')

    return df

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
    df.to_sql('brt_data', con=engine, if_exists='append', index=False)