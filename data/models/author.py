from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class AuthorBase(SQLModel):
    name: str

class Author(AuthorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    books: List["Book"] = Relationship(back_populates="author")  # type: ignore

class AuthorCreate(AuthorBase):
    name: str

class AuthorRead(SQLModel):
    name: str
    class Config:
        orm_mode = True