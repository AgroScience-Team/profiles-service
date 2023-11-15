from fastapi import FastAPI

from src.api.organizations import router as organizations_router
from src.api.workers import router as workers_router


app = FastAPI(
    title="Profiles service",
    description="Digital twin profiles microservice.",
    version="0.0.1"
)

app.include_router(organizations_router)
app.include_router(workers_router)
