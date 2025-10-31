from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from db import get_session
from data.models.user import User, UserRegister, UserUpdate

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=List[User])
async def get_users(session: Session = Depends(get_session)):
  return session.exec(select(User)).all()

@router.post("/", response_model=User)
async def create_user(user: UserRegister, session: Session = Depends(get_session)):
  db_user = User.model_validate(user)
  session.add(db_user)
  session.commit()
  session.refresh(db_user)

  return db_user