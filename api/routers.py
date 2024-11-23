from fastapi import APIRouter

from brokers.tasks import send_task
from models.models import UserModel

router = APIRouter()


@router.post("/tasks/")
async def create_task(user: UserModel):
    """Отправляет задачу в Kafka"""
    await send_task(user)
    return {"status": "Task sent", "message": user}
