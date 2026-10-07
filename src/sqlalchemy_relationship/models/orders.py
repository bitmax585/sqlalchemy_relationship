from .base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(primary_key=True)
    customer_id: Mapped[str] = mapped_column(
        ForeignKey("customers.id")
    )

    