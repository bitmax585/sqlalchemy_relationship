from .base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column(String(13))