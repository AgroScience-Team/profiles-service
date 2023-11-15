from fastapi import FastAPI

from src.api.organizations import router as organizations_router


app = FastAPI(
    title="Profiles service",
    description="Digital twin profiles microservice.",
    version="0.0.1"
)

app.include_router(organizations_router)
