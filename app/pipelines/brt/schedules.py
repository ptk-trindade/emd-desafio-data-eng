from datetime import timedelta, datetime

from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock
import pytz

brt_schedule = Schedule(
    clocks=[
        IntervalClock(
            interval=timedelta(minutes=1),
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(minutes=10, seconds=5),
        )]
)