from sqlmodel import Session
from typing import List
from data.models import Author, AuthorCreate
from data.repositories.author_repository import (
    get_all_authors,
    get_author_by_id,
    create_author as repo_create_author,
    update_author as repo_update_author,
    delete_author as repo_delete_author,
)
from fastapi import HTTPException


def list_authors(session: Session, **filters) -> List[Author]:
  return get_all_authors(session, filters)

def get_author(session: Session, author_id: int) -> Author:
  author = get_author_by_id(session, author_id)
  if not author:
      raise HTTPException(status_code=404, detail="Author não encontrado")
  return author

def create_new_author(session: Session, author_data: AuthorCreate) -> Author:
    new_author = Author(name=author_data.name)
    repo_create_author(session, new_author)
    return new_author

def update_existing_author(session: Session, author_id: int, author_update: Author) -> Author:
  author = get_author(session, author_id)
  author.name = author_update.name or author.name
  return repo_update_author(session, author)

def delete_existing_author(session: Session, author_id: int) -> None:
  author = get_author(session, author_id)
  repo_delete_author(session, author)