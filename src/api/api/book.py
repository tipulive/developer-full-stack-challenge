from fastapi import   Query,APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc,asc

from models.author import Author
from models.book import Book
from database import get_db
from schemas.book import BookCreate, BookUpdate
from security import get_current_user
from dependencies import get_current_active_user

router = APIRouter()


@router.get("/books_paginate")
def get_books_with_paginate(current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db),page: int = 1, limit: int = 10, search: str = None,sort: str = Query("asc", regex=r"^(asc|desc)$")):
       # Pagination logic
    offset = (page - 1) * limit
    
    queryData=asc(Book.id) if sort=="asc" else desc(Book.id)
    # Query books with author information
    query = (
        db.query(Book, Author.name.label("author_name"))
        .join(Author)
        .order_by(queryData)
    )
    
    # Search logic
    if search:
        query = query.filter(Book.name.ilike(f"%{search}%"))
    
    total_books = query.count()
    books = query.offset(offset).limit(limit).all()
    
 
    
    response_books = []
    for book, author_name in books:
        response_books.append({
            "id": book.id,
            "name": book.name,
            "pages": book.pages,
            "author_id":book.author_id,
            "author_name": author_name
            
        })
    
    return {
        "total_books": total_books,
        "books": response_books,
    }
@router.get("/BookByAuthorId")
def get_books_with_search_author_id(current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db),page: int = 1, limit: int = 10, search: str = None):
       # Pagination logic
    offset = (page - 1) * limit
    
    # Query books with author information
    query = (
        db.query(Book, Author.name.label("author_name"))
        .join(Author)
        .order_by(Book.id)
    )
    
    # Search logic
    if search:
        query = query.filter(Book.author_id==search)
    
    total_books = query.count()
    books = query.offset(offset).limit(limit).all()
    
 
    
    response_books = []
    for book, author_name in books:
        response_books.append({
            "id": book.id,
            "name": book.name,
            "pages": book.pages,
            "author_name": author_name
        })
    
    return {
        "total_books": total_books,
        "books": response_books,
    }
@router.get("/books")
def get_books(current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

''' protected
@router.get("/books")
def get_books(current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books
'''



@router.post("/books")
def create_book(book: BookCreate,current_user: str = Depends(get_current_active_user), db: Session = Depends(get_db)):
    new_book = Book(name=book.name, author_id=book.author_id, pages=book.pages)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/books/{book_id}")
def update_book(book_id: int, book:BookUpdate,current_user: str = Depends(get_current_active_user),db: Session = Depends(get_db)):
    # Check if the book exists
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Update the book data
    db_book.name = book.name
    db_book.pages = book.pages
    db_book.author_id = book.author_id
    
    db.commit()
    db.refresh(db_book)
    
    return db_book

@router.delete("/books/{book_id}")
def delete_book(book_id: int,current_user: str = Depends(get_current_active_user), db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"status":True,"message": "Book deleted successfully"}

