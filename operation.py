from exceptions import *
from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from base import Base
from book import Book
from user import User
from rented import Rented
from sqlalchemy import Date, and_, DateTime
from datetime import date, datetime
from fee import Fee
from sqlalchemy.exc import NoResultFound




class Operation:
    def __init__(self):
        self.engine: Engine = create_engine("sqlite:///library.db", echo=True)
        self.session: Session = Session(self.engine)
        Base.metadata.create_all(self.engine)

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

    def return_book(self, book_id: int):
        try:
            book: type[Book] = self.session.query(Book).filter_by(id=book_id).one()
        except NoResultFound:
            raise BookDoesNotExistException()
        rented_query = self.session.query(Rented).filter_by(book_id=book_id)
        if not self.session.query(rented_query.exists()).scalar():
            raise BookDoesNotRented()
        try:
            rented_book: type[Rented] = self.session.query(Rented).filter(
                and_(Rented.book_id == book_id, Rented.date_end == None)).one()
            rented_book.date_end = datetime.now()
            days_diff = (rented_book.date_end - rented_book.date_begin).days

            if days_diff > 30:
                self.session.add(Fee(price=days_diff-30, user_id=rented_book.user_id, rent_id=book.rents[-1].id,book_id=rented_book.book_id))

        except NoResultFound:
            raise BookDoesNotRented()

        self.session.commit()


    def rent_book(self, user_id: int, book_id: int):
        try:
            user: type[User] = self.session.query(User).filter_by(id=user_id).one()
        except NoResultFound:
            raise UserDoesNotExistException()
        try:
            book: type[Book] = self.session.query(Book).filter_by(id=book_id).one()
        except NoResultFound:
            raise BookDoesNotExistException()


        rented: type[Rented] = self.session.query(Rented).filter_by(book_id=book_id, date_end=None).first()
        if rented:
            raise BookAlreadyRented()

        self.session.add(Rented(date_begin=datetime.now(), date_end=None, user_id=user_id, book_id=book_id))
        self.session.commit()