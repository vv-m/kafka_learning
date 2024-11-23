from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.routers import router
from brokers.kafka_broker import broker
from brokers.scheduler import scheduler


# Определяем жизненный цикл приложения с помощью декоратора @asynccontextmanager
# Этот метод позволяет управлять ресурсами, которые нужно запускать и закрывать с приложением
@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    await broker.start()  # Запуск Kafka брокера при старте приложения
    scheduler.start()  # Запуск планировщика задач
    yield
    await broker.close()  # Закрытие Kafka брокера при остановке приложения
    scheduler.shutdown()  # Завершение работы планировщика задач


app = FastAPI(title="FastAPI & Kafka (KRaft)", lifespan=lifespan)
app.include_router(router)
