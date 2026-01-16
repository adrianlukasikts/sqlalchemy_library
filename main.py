from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    title: Mapped[str] = mapped_column(String(40))
    author: Mapped[str] = mapped_column(String(40))
    year: Mapped[int] = mapped_column(name="year")

    user: Mapped["User"] = relationship(back_populates="books")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    name: Mapped[str] = mapped_column(String(40))
    surname: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(String(40))

    books: Mapped[List["Book"]] = relationship(
        back_populates="user", cascade="all"
    )


from sqlalchemy import create_engine

engine = create_engine("sqlite:///library.db", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    osoba_alibabska = Book(title="Osoba Alibabska i 14 osób z doświadczeniem rozbójniczym", author="nieznany", year="1967")

    kacper_barszcz = User(
        name="Kacper",
        surname="Barszcz",
        email="kacper.barscz09@gmail.com",
        books=[osoba_alibabska,
               Book(title="Osoba Tadeuszowska", author="Adam Mickiewicz", year="1867")]
    )

    john_doe = User(
        name="John",
        surname="Doe",
        email="johndoe@example.com",
        books=[osoba_alibabska]
    )

    session.add_all([kacper_barszcz, john_doe])

    session.commit()