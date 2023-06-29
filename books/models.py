from sqlalchemy import Column, ForeignKey, Integer, String

from database import Base


class Author(Base):
    __tablename__ = 'books_author'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)


class Book(Base):
    __tablename__ = 'books_book'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author_id = Column(ForeignKey('books_author.id'), nullable=False)
    price = Column(Integer, nullable=False)
