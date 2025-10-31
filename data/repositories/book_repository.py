from sqlmodel import Session, select
from typing import List, Optional
from data.models import Book
from sqlalchemy.orm import selectinload

def get_all_books(session: Session) -> List[Book]:
    statement = select(Book).options(selectinload(Book.author))
    exec = session.exec(statement).all()
    for book in exec:
        print(f"Book: {book.title}, Author: {book.author.name}")
    return exec

def get_book_by_id(session: Session, book_id: int) -> Optional[Book]:
    return session.get(Book, book_id)

def create_book(session: Session, book: Book) -> Book:
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def update_book(session: Session, book: Book) -> Book:
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def delete_book(session: Session, book: Book) -> None:
    session.delete(book)
    session.commit()