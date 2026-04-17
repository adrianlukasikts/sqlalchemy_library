from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import List
from base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer
from sqlalchemy import ForeignKey


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    title: Mapped[str] = mapped_column(String(40))
    author: Mapped[str] = mapped_column(String(40))
    year: Mapped[int] = mapped_column(name="year")

    user: Mapped["User"] = relationship(back_populates="books")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    rents: Mapped[List["Rented"]] = relationship(
        back_populates="book", cascade="all"
    )