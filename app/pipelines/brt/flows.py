from prefect import Flow
from prefect.run_configs import DockerRun

from pipelines.brt.schedules import brt_schedule
from pipelines.brt.tasks import (
    get_brt_data,
    create_dataframe,
    load_csv,
    load_db,
)


with Flow(
    name="BRT: BRT Dados de GPS"
) as brt_gps_flow:
    
    # get gps data
    data = get_brt_data()
    
    df = create_dataframe(data["veiculos"])

    # Save data to csv and Postgres
    load_csv(df)
    load_db(df)


brt_gps_flow.schedule = brt_schedule
brt_gps_flow.run_config = DockerRun()