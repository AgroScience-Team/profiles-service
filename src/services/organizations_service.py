from fastapi import Depends, HTTPException, status

from sqlalchemy import delete, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.models.organizations import Organization
from src.schemas.organization import OrganizationRequestSchema


class OrganizationsService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
    
    async def read_organization(self, user_id: int = None) -> Organization:
        result = await self.session.execute(
            select(Organization)
            .where(Organization.user_id == user_id)
        )
        profile = result.scalar()
        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found"
            )
        return profile
    
    async def create_organization(
        self,
        user_id: int,
        schema: OrganizationRequestSchema
    ) -> Organization:
        organization = Organization(
            user_id=user_id,
            name=schema.name,
            description=schema.description,
            city=schema.city,
            inn=schema.inn,
            phone_number=schema.phone_number,
            website=schema.website
        )
        try:
            self.session.add(organization)
            await self.session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Profile with user_id: {user_id} already exists"
            )
        return organization

    async def update_organization(
        self,
        user_id: int,
        schema: OrganizationRequestSchema
    ) -> None:
        _ = await self.read_organization(user_id)
        await self.session.execute(
            update(Organization)
            .where(Organization.user_id == user_id)
            .values(**schema.model_dump())
        )
        await self.session.commit()
        
    async def delete_organization(self, user_id: int) -> None:
        await self.session.execute(
            delete(Organization)
            .where(Organization.user_id == user_id)
        )
        await self.session.commit()
