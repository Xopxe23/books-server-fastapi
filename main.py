import uvicorn
from fastapi import FastAPI

from users.routers import router as users_router

app = FastAPI(
    title='Books'
)

app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run(app)
