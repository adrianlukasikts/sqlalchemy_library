from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from base import  Base
from typing import List
from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    name: Mapped[str] = mapped_column(String(40))
    surname: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(String(40))

    books: Mapped[List["Book"]] = relationship(
        back_populates="user", cascade="all"
    )
    rents: Mapped[List["Rented"]] = relationship(
        back_populates="user", cascade="all"
    )