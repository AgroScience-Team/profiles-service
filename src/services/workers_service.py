from fastapi import Depends, HTTPException, status

from sqlalchemy import delete, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.models.workers import Worker
from src.schemas.worker import WorkerRequestSchema


class WorkersService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
    
    async def read_worker(self, user_id: int = None) -> Worker:
        result = await self.session.execute(
            select(Worker)
            .where(Worker.user_id == user_id)
        )
        profile = result.scalar()
        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found"
            )
        return profile
    
    async def create_worker(
        self,
        user_id: int,
        schema: WorkerRequestSchema
    ) -> Worker:
        worker = Worker(
            user_id=user_id,
            name=schema.name,
            surname=schema.surname,
            patronymic=schema.patronymic,
            date_of_birth=schema.date_of_birth,
            phone_number=schema.phone_number
        )
        try:
            self.session.add(worker)
            await self.session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Profile with user_id: {user_id} already exists"
            )
        return worker

    async def update_worker(self, user_id: int, schema: WorkerRequestSchema) -> None:
        _ = await self.read_worker(user_id)
        await self.session.execute(
            update(Worker)
            .where(Worker.user_id == user_id)
            .values(**schema.model_dump())
        )
        await self.session.commit()
        
    async def delete_worker(self, user_id: int) -> None:
        await self.session.execute(
            delete(Worker)
            .where(Worker.user_id == user_id)
        )
        await self.session.commit()
