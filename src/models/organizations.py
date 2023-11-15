from datetime import date

from sqlalchemy import Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Organization(Base):
    __tablename__ = "organizations"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    city: Mapped[str] = mapped_column(String(64), nullable=False)
    inn: Mapped[str] = mapped_column(String(64), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(32), nullable=True)
    website: Mapped[str] = mapped_column(String(128), nullable=True)
