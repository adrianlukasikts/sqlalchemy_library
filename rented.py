from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Date, and_, DateTime
from datetime import date, datetime
from sqlalchemy import ForeignKey
from typing import Optional


class Rented(Base):
    __tablename__ = "rented"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    date_begin: Mapped[datetime] = mapped_column(DateTime)
    date_end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    user: Mapped["User"] = relationship(back_populates="rents")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book: Mapped["Book"] = relationship(back_populates="rents")
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))