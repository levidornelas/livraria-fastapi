from sqlmodel import Session
from typing import List
from data.models.book import Book, BookCreate, BookUpdate
from data.repositories.book_repository import (
    get_all_books,
    get_book_by_id,
    create_book as repo_create_book,
    update_book as repo_update_book,
    delete_book as repo_delete_book,
)
from fastapi import HTTPException

def list_books(session: Session) -> List[Book]:
    return get_all_books(session)

def get_book(session: Session, book_id: int) -> Book:
    book = get_book_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book não encontrado")
    return book

def create_new_book(session: Session, book_data: BookCreate) -> Book:
    book = Book(
        title=book_data.title,
        pages=book_data.pages,
        publication_date=book_data.publication_date,
        price=book_data.price,
        image_url=book_data.image_url,
        author=book_data.author
    )

    return repo_create_book(session, book)

def update_existing_book(session: Session, book_id: int, book_update: BookUpdate) -> Book:
    book = get_book(session, book_id)
    book.title = book_update.title or book.title
    book.price = book_update.price or book.price
    return repo_update_book(session, book)

def delete_existing_book(session: Session, book_id: int) -> None:
    book = get_book(session, book_id)
    repo_delete_book(session, book)