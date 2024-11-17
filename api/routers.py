from fastapi import APIRouter

from brokers.tasks import send_task

router = APIRouter()

@router.post("/tasks/")
async def create_task(message):
    """Отправляет задачу в Kafka"""
    await send_task(message)
    return {"status": "Task sent", "message": message}