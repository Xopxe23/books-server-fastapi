from fastapi import APIRouter

from exceptions import UserAlreadyExistsException
from users.auth import get_password_hash
from users.dals import UserDAO
from users.schemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=['Auth & Users']
)


@router.post('/register')
async def register_user(user_data: SUserRegister):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)
    return {f"{user_data.email} успешно зарегестрирован!"}
