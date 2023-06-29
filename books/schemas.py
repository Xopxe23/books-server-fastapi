from pydantic import BaseModel


class SBookShow(BaseModel):
    id: str
    name: str
    author_id: int
    price: int

    class Config:
        orm_mode = True


class SBookCreate(BaseModel):
    name: str
    author_id: int
    price: int
