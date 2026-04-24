from pydantic import BaseModel, EmailStr, HttpUrl


class UserLoginResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    firstName: str
    lastName: str
    gender: str
    image: HttpUrl
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
