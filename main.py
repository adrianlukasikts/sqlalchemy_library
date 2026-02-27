from typing import List
from typing import Optional
from sqlalchemy import DateTime, Null, Date
from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass



class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    title: Mapped[str] = mapped_column(String(40))
    author: Mapped[str] = mapped_column(String(40))
    year: Mapped[int] = mapped_column(name="year")

    user: Mapped["User"] = relationship(back_populates="books")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=True)
    rents: Mapped[List["Rented"]] = relationship(
        back_populates="book", cascade="all"
    )


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

class Rented(Base):
    __tablename__ = "rented"
    id: Mapped[int] = mapped_column(primary_key=True, name="id", autoincrement=True)
    date_begin: Mapped[Date] = mapped_column(Date)
    date_end: Mapped[Date] = mapped_column(Date, nullable=True)
    user: Mapped["User"] = relationship(back_populates="rents")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book: Mapped["Book"] = relationship(back_populates="rents")
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))


class UserDoesNotExistException(Exception):
    pass
class BookDoesNotExistException(Exception):
    pass
class BookAlreadyRented(Exception):
    pass

class Operation:
    def __init__(self):
        self.engine: Engine = create_engine("sqlite:///library.db", echo=True)
        self.session: Session = Session(self.engine)

    def insert_book(self, title: str, author: str, year: str):
        self.session.add(Book(title=title, author=author, year=year))
        self.session.commit()

    def insert_user(self, name: str, surname: str, email: str):
        self.session.add(User(name=name, surname=surname, email=email, books=[]))
        self.session.commit()

    def update_book_owner(self, book_id: int, user_id: int):
        user: type[User] = self.session.query(User).filter_by(id=user_id).one()
        book: type[Book] = self.session.query(Book).filter_by(id=book_id).one()

        if not user:
            raise UserDoesNotExistException()
        if not book:
            raise BookDoesNotExistException()

        book.user_id = user_id

        self.session.commit()
    def rent_book(self,user_id:int,book_id:int):
        user: type[User] = self.session.query(User).filter_by(id=user_id).one()
        book: type[Book] = self.session.query(Book).filter_by(id=book_id).one()
        rented:type[Rented] = self.session.query(Rented).filter_by(book_id=book_id,date_end=Null).one()
        if not user:
            raise UserDoesNotExistException()
        if not book:
            raise BookDoesNotExistException()
        if rented:
            raise BookAlreadyRented()

        self.session.add(Rented(date_begin=date(2026,2,27),date_end=Null,user_id=user_id,book_id=book_id))
        self.session.commit()





    def init_db(self):
        Base.metadata.create_all(self.engine)


operation = Operation()
operation.init_db()
# operation.insert_user("Kacper", "Barszcz", "kapi@A.com")
# operation.insert_book("Balladyna", "Julisz Slowacki", "1830")
#
# operation.update_book_owner(1, 1)
operation.rent_book(2,2)

