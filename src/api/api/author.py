from fastapi import   Query,APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func,desc,asc

from models.author import Author
from models.book import Book
from database import get_db
from schemas.author import AuthorCreate, AuthorUpdate
from security import get_current_user
from dependencies import get_current_active_user

router = APIRouter()

@router.get("/authors")
def get_all_authors_with_search_and_paginate(current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db),page: int = 1, limit: int = 10, search: str = None,sort: str = Query("asc", regex=r"^(asc|desc)$")):
      # Pagination logic
    offset = (page - 1) * limit

    queryData=asc(Author.id) if sort=="asc" else desc(Author.id)
    # Query authors with their book count
    query = (
        db.query(Author, func.count(Book.id).label("book_count"))
        .outerjoin(Book)
        .group_by(Author)
        .order_by(queryData)
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
def create_author(author: AuthorCreate,current_user: str = Depends(get_current_active_user), db: Session = Depends(get_db)):
    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@router.put("/authors/{author_id}")
def update_author(author_id: int, author:AuthorUpdate,current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db)):
    # Check if the book exists
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    # Update the author data
    db_author.name = author.name
   
    
    db.commit()
    db.refresh(db_author)
    
    return db_author



