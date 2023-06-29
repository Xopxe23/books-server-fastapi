from fastapi import APIRouter

from books.dals import BookDAO
from books.schemas import SBookCreate, SBookShow

router = APIRouter(
    prefix='/books',
    tags=['books & authors']
)


@router.get('/')
async def get_books() -> list[SBookShow]:
    return await BookDAO.find_all()


@router.post('/')
async def create_book(book_data: SBookCreate):
    await BookDAO.add(name=book_data.name, author_id=book_data.author_id, price=book_data.price)
    return f'Book "{book_data.name}" added!'
