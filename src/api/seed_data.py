from sqlalchemy.orm import Session

from security import get_password_hash
from models.user import User
from models.author import Author
from models.book import Book
from database import SessionLocal, engine


def seed_data():
    # Create database tables
    User.metadata.create_all(bind=engine)
    Book.metadata.create_all(bind=engine)
    Author.metadata.create_all(bind=engine)

    # Open a database session
    db = SessionLocal()

    try:
        # Seed users
        user1 = User(username='john123', password=get_password_hash('123456'))
        user2 = User(username='jane123', password=get_password_hash('123456'))
        db.add(user1)
        db.add(user2)
        db.commit()

        # Seed authors
        author1 = Author(name='Author 1')
        author2 = Author(name='Author 2')
        db.add(author1)
        db.add(author2)
        db.commit()

        # Seed books
        book1 = Book(name='Book 1', pages=100, author_id=author1.id)
        book2 = Book(name='Book 2', pages=200, author_id=author2.id)
        db.add(book1)
        db.add(book2)
        db.commit()

    finally:
        # Close the database session
        db.close()

if __name__ == "__main__":
    seed_data()
