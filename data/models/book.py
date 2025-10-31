from sqlmodel import Relationship, SQLModel, Field
from typing import Optional
from datetime import date
from data.models import AuthorCreate, AuthorRead

class BookBase(SQLModel):
    title: str
    pages: Optional[int] = None
    publication_date: Optional[date] = None
    price: Optional[float] = None
    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    image_url: Optional[str] = None

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author: Optional["Author"] = Relationship(back_populates="books") # type: ignore

class AuthorCreate(SQLModel):
    name: str

class BookCreate(BookBase):
    author_id: Optional[int] = None  
    author: Optional[AuthorCreate] = None

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
    price: Optional[float] = None
    author_id: Optional[int] = None
    author: Optional[AuthorRead] = None
    image_url: Optional[str] = None

    class Config:
        orm_mode = True