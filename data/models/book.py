from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class BookBase(SQLModel):
    title: str
    pages: Optional[int] = None
    publication_date: Optional[date] = None
    price: Optional[float] = None
    image_url: Optional[str] = None

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class BookCreate(BookBase):
    author: Optional[str] = None

class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    pages: Optional[int] = None
    publication_date: Optional[date] = None
    price: Optional[float] = None

class BookRead(SQLModel):
    id: int
    title: str
    pages: Optional[int] = None
    publication_date: Optional[date] = None
    author_id: Optional[int] = None
    author: Optional[str] = None
    image_url: Optional[str] = None

    class Config:
        from_attributes = True