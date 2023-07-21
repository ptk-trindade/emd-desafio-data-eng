from datetime import timedelta, datetime
from prefect.schedules import IntervalSchedule

every_1_minute = IntervalSchedule(
    start_date=datetime.now(),
    interval=timedelta(minutes=1),
    end_date=datetime.now() + timedelta(minutes=10, seconds=5)
)



