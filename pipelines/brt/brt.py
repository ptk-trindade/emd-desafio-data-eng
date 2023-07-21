import prefect
from prefect import task, Flow
import os
import requests

from pipelines.schedules import minute_to_minute


@task
def get_brt_data():
    response = requests.get('https://dados.mobilidade.rio/gps/brt', verify=False)
    return response.json()

@task
def load_csv(data):
    import pandas as pd
    df = pd.DataFrame(data)
    logger = prefect.context.get("logger")
    
    if df.shape[0] == 0: # empty dataframe
        logger.info("DataFrame is empty")
        return
    
    if not os.path.exists('database/brt_data.csv'): # creates file if doesn't exists
        logger.info("Creating file 'database/brt_data.csv'")
        df.to_csv('database/brt_data.csv')
        return
    
    df.to_csv('database/brt_data.csv', mode='a', header=False)


with Flow("brt-flow") as brt_flow:
    data = get_brt_data()
    load_csv(data["veiculos"])


brt_flow.schedule = minute_to_minute()

