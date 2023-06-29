from fastapi import APIRouter, Response

from exceptions import (IncorrectEmailOrPasswordException,
                        UserAlreadyExistsException)
from users.auth import (authenticate_user, create_access_token,
                        get_password_hash)
from users.dals import UserDAO
from users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=['Auth & Users']
)


@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)
    return {f"{user_data.email} успешно зарегестрирован!"}


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": user_data.email})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token
