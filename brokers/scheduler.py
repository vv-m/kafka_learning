from apscheduler.schedulers.asyncio import AsyncIOScheduler

from brokers.tasks import send_task
from models.models import example_obj_pydantic


async def scheduled_task():
    print("Scheduled task executed!")
    await send_task(example_obj_pydantic)


scheduler = AsyncIOScheduler()
scheduler.add_job(scheduled_task, "interval", seconds=3)
