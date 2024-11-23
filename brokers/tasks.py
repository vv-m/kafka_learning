from brokers.kafka_broker import broker
from models.models import UserModel


# Обработка задачи (subscriber)
@broker.subscriber("task-topic")
async def process_task(user: UserModel):
    print(f"Processing for user: {user.name}")
    return {"user": user}


# Отправка задачи (publisher)
async def send_task(user: UserModel):
    await broker.publish(user, topic="task-topic")
