from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from base import Base
from sqlalchemy import String, Integer
from sqlalchemy import ForeignKey



class Fee(Base):
    __tablename__ = "fees"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    price: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    rent_id: Mapped[int] = mapped_column(ForeignKey("rented.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))