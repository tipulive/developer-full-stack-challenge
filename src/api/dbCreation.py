
from models.author import Author
from models.book import Book
from models.user import User 
from database import Base, engine


def create_tables():
    Base.metadata.create_all(bind=engine)
 
