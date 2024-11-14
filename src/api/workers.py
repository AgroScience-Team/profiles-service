import uuid

from fastapi import APIRouter, Depends, status

from src.schemas.worker import WorkerRequestSchema, WorkerResponseSchema
from src.schemas.token import TokenPayloadSchema
from src.services.workers_service import WorkersService
from src.utils.token import Token


router = APIRouter(
    prefix="/api/profiles/workers",
    tags=["Worker profiles"],
)


@router.post(
    "",
    response_model=WorkerResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_worker(
    schema: WorkerRequestSchema,
    worker_info: TokenPayloadSchema = Depends(Token.get_worker_payload),
    service: WorkersService = Depends()
):
    profile = await service.create_worker(uuid.UUID(worker_info.sub), schema)
    return profile


@router.get("/me", response_model=WorkerResponseSchema)
async def get_worker_me(
    worker_info: TokenPayloadSchema = Depends(Token.get_worker_payload),
    service: WorkersService = Depends()
):
    profile = await service.read_worker(uuid.UUID(worker_info.sub))
    return profile


@router.get(
    "",
    response_model=WorkerResponseSchema,
    dependencies=[Depends(Token.get_payload)]
)
async def get_worker(user_id: uuid.UUID, service: WorkersService = Depends()):
    profile = await service.read_worker(user_id)
    return profile


@router.put("/me", status_code=status.HTTP_204_NO_CONTENT)
async def update_worker(
    schema: WorkerRequestSchema,
    worker_info: TokenPayloadSchema = Depends(Token.get_worker_payload),
    service: WorkersService = Depends()
):
    await service.update_worker(uuid.UUID(worker_info.sub), schema)


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_organization(
    worker_info: TokenPayloadSchema = Depends(Token.get_worker_payload),
    service: WorkersService = Depends()
):
    await service.delete_worker(uuid.UUID(worker_info.sub))
