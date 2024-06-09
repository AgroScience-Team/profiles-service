import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.organizations import router as organizations_router
from src.api.workers import router as workers_router
from src.broker.consumer import get_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    consumer = get_consumer()
    consuming = asyncio.create_task(consumer.delete_users())
    await asyncio.gather(consuming)
    yield


app = FastAPI(
    title="Profiles service",
    description="Digital twin profiles microservice.",
    version="0.0.1",
    lifespan=lifespan
)

app.include_router(organizations_router)
app.include_router(workers_router)
