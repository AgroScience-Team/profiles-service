import uuid
from datetime import date

from sqlalchemy import Date, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    surname: Mapped[str] = mapped_column(String(128), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(128), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=True)
    phone_number: Mapped[str] = mapped_column(String(32), nullable=True)
