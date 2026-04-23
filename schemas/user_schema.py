from pydantic import BaseModel, EmailStr, HttpUrl

class UserLoginResponse(BaseModel):
    id: int
    username: str
    email: EmailStr  # Автоматически проверит формат почты
    firstName: str
    lastName: str
    gender: str
    image: HttpUrl   # Проверит, что это валидная ссылка
    accessToken: str
    refreshToken: str

class UserMeResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    firstName: str
    lastName: str
    gender: str
    image: HttpUrl