from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True,name="id", autoincrement=True )
    title: Mapped[str] = mapped_column(String(40))
    author: Mapped[str] = mapped_column(String(40))
    year: Mapped[int] = mapped_column(name="year")

from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True)