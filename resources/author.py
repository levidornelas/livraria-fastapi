from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List, Optional

from db import get_session

from data.models import Author, AuthorCreate, AuthorBase
from services.author_service import (
    list_authors,
    get_author,
    create_new_author,
    update_existing_author,
    delete_existing_author,
)
router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/", response_model=List[Author])
def read_authors(
    session: Session = Depends(get_session), 
    name: Optional[str] = None,
    id: Optional[int] = None
):
    return list_authors(session, name=name, id=id)

@router.post("/", response_model=AuthorBase)
def create_author(author: AuthorCreate, session: Session = Depends(get_session)):
    """
    Cria um novo autor
    """
    return create_new_author(session, author)

@router.get("/{author_id}", response_model=Author)
def read_author(author_id: int, session: Session = Depends(get_session)):
    """
    Retorna um autor pelo ID
    """
    return get_author(session, author_id)


@router.put("/{author_id}", response_model=Author)
def update_author(author_id: int, author_update: AuthorCreate, session: Session = Depends(get_session)):
    """
    Atualiza um autor existente
    """
    return update_existing_author(session, author_id, author_update)

@router.delete("/{author_id}")
def delete_author(author_id: int, session: Session = Depends(get_session)):
    """
    Deleta um autor existente
    """
    delete_existing_author(session, author_id)
    return {"ok": True, "message": f"Author {author_id} deletado!"}