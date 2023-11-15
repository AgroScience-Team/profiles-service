from datetime import date

from pydantic import BaseModel, Field


class WorkerRequestSchema(BaseModel):
    name: str = Field(max_length=128)
    surname: str = Field(max_length=128)
    patronymic: str | None = Field(max_length=128)
    date_of_birth: date | None
    phone_number: str | None = Field(max_length=32)


class WorkerResponseSchema(WorkerRequestSchema):
    id: int
    user_id: int
    name: str
    surname: str
    patronymic: str | None
    date_of_birth: date | None
    phone_number: str | None
