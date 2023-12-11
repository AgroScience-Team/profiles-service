from fastapi import APIRouter, Depends, status

from src.schemas.organization import (
    OrganizationRequestSchema,
    OrganizationResponseSchema
)
from src.schemas.token import TokenPayloadSchema
from src.services.organizations_service import OrganizationsService
from src.utils.token import Token


router = APIRouter(
    prefix="/api/profiles/organizations",
    tags=["Organization profiles"],
)


@router.post(
    "",
    response_model=OrganizationResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_organization(
    schema: OrganizationRequestSchema,
    organization_info: TokenPayloadSchema = Depends(Token.get_organization_payload),
    service: OrganizationsService = Depends()
):
    organization = await service.create_organization(int(organization_info.sub), schema)
    return organization


@router.get("/me", response_model=OrganizationResponseSchema)
async def get_organization_me(
    organization_info: TokenPayloadSchema = Depends(Token.get_organization_payload),
    service: OrganizationsService = Depends()
):
    profile = await service.read_organization(int(organization_info.sub))
    return profile


@router.get(
    "",
    response_model=OrganizationResponseSchema,
    dependencies=[Depends(Token.get_payload)]
)
async def get_organization(user_id: int, service: OrganizationsService = Depends()):
    profile = await service.read_organization(user_id)
    return profile


@router.put("/me", status_code=status.HTTP_204_NO_CONTENT)
async def update_organization(
    schema: OrganizationRequestSchema,
    organization_info: TokenPayloadSchema = Depends(Token.get_organization_payload),
    service: OrganizationsService = Depends()
):
    await service.update_organization(organization_info.org, schema)


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_organization(
    organization_info: TokenPayloadSchema = Depends(Token.get_organization_payload),
    service: OrganizationsService = Depends()
):
    await service.delete_organization(organization_info.org)
