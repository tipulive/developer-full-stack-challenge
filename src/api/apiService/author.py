from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from models.author import Author
from models.book import Book
from database import get_db
from schemas.author import AuthorCreate, AuthorUpdate
from security import get_current_user
from dependencies import get_current_active_user

router = APIRouter()

@router.get("/authors")
def get_all_authors_with_search_and_paginate(db: Session = Depends(get_db),page: int = 1, limit: int = 10, search: str = None):
      # Pagination logic
    offset = (page - 1) * limit
    
    # Query authors with their book count
    query = (
        db.query(Author, func.count(Book.id).label("book_count"))
        .outerjoin(Book)
        .group_by(Author)
        .order_by(Author.id)
    )
    
    # Search logic
    if search:
        query = query.filter(Author.name.ilike(f"%{search}%"))
    
    total_authors = query.count()
    authors = query.offset(offset).limit(limit).all()
    
    
    
    response_authors = []
    for author, book_count in authors:
        response_authors.append({
            "id": author.id,
            "name": author.name,
            "book_count": book_count
        })
    
    return {
        "total_authors": total_authors,
        "authors": response_authors,
    }






''' protected
@router.get("/books")
def get_books(current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books
'''



@router.post("/authors")
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

# Implement other CRUD endpoints for books: read by id, update, and delete
