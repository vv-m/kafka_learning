
from brokers.kafka_broker import broker

# Обработка задачи (subscriber)
@broker.subscriber("task-topic")
async def process_task(message: str):
    # print(f"Processing task: {message}")
    return {"message": message}

# Отправка задачи (publisher)
@broker.subscriber("task-topic")
async def send_task(message: str):
    await broker.publish(message, topic="task-topic")


# publisher = broker.publisher("task-topic-2")

# @broker.publisher("task-topic")
# @broker.subscriber("task-topic", group_id="my-unique-group")
# async def send_task(message: str) -> str:
#     return message

