from sqlmodel import Session, select
from typing import List, Optional
from data.models import Author

def get_all_authors(session: Session, filters: Optional[dict] = None) -> List[Author]:
  query = select(Author)
  if filters.get("name"):
      query = query.where(Author.name == filters["name"])
  if filters.get("id"):
      query = query.where(Author.id == filters["id"])
  return session.exec(query).all()

def get_author_by_id(session: Session, author_id: int) -> Optional[Author]:
  return session.get(Author, author_id)

def create_author(session: Session, author: Author) -> Author:
  session.add(author)
  session.commit()
  session.refresh(author)
  return author

def update_author(session: Session, author: Author) -> Author:
    session.add(author)
    session.commit()
    session.refresh(author)
    return author

def delete_author(session: Session, author: Author) -> None:
    session.delete(author)
    session.commit()