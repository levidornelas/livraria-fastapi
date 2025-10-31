from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from db import get_session
from data.models import Book, BookCreate, BookUpdate, BookRead
from services.book_service import (
    list_books,
    get_book,
    create_new_book,
    update_existing_book,
    delete_existing_book,
)

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[BookRead])
def read_books(session: Session = Depends(get_session)):
    return list_books(session)

@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    return create_new_book(session, book)

@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, session: Session = Depends(get_session)):
    return get_book(session, book_id)

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate, session: Session = Depends(get_session)):
    return update_existing_book(session, book_id, book_update)

@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    delete_existing_book(session, book_id)
    return {"ok": True, "message": f"Book {book_id} deletado!"}