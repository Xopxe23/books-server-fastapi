import uvicorn
from fastapi import FastAPI

from books.routers import router as books_router
from users.routers import router as users_router

app = FastAPI(
    title='Books'
)

app.include_router(users_router)
app.include_router(books_router)


if __name__ == "__main__":
    uvicorn.run(app)
