import uuid

from pydantic import BaseModel, Field


class OrganizationRequestSchema(BaseModel):
    name: str = Field(max_length=128)
    description: str | None
    city: str = Field(max_length=64)
    inn: str | None = Field(max_length=64)
    phone_number: str | None = Field(max_length=32)
    website: str | None = Field(max_length=128)

    
class OrganizationResponseSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    description: str | None
    city: str
    inn: str | None
    phone_number: str | None
    website: str | None
