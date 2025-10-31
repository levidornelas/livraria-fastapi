from sqlmodel import SQLModel, Field
from typing import Optional

class UserBase(SQLModel):
  username: str
  email: Optional[str] = None
  age: Optional[int] = None
  password: str

class User(UserBase, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  username: str = Field(sa_column_kwargs={"unique": True}, index=True)
  email: Optional[str] = Field(sa_column_kwargs={"unique": True}, default=None, index=True)

class UserRegister(UserBase):
    pass

class UserUpdate(SQLModel):
   username: Optional[str] = None
   email: Optional[str] = None
   age: Optional[str] = None
   password: Optional[str] = None