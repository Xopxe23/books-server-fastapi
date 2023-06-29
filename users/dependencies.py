from datetime import datetime

from fastapi import Request, Depends
from jose import jwt, JWTError

from config import settings
from exceptions import TokenAbsentException, TokenIncorrectFormatException, TokenExpiredException, \
    UserIsNotPresentException
from users.dals import UserDAO


def get_token(request: Request) -> str:
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise TokenIncorrectFormatException
    expire: str = payload.get("exp")
    if not expire or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_email: str = payload.get("sub")
    user = await UserDAO.find_one_or_none(email=user_email)
    if not user:
        raise UserIsNotPresentException
    return user
