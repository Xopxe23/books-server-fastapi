from books.models import Author, Book
from dao.base import BaseDAO


class BookDAO(BaseDAO):
    model = Book
