from uuid import UUID

from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    id: UUID = ""
    email: EmailStr
    is_active: bool
    username: str = Field(..., min_length=8, max_length=64, description="The name that represents the user")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "a2a18886-d3a2-4774-8e5f-69f7e1057a7d",
                "name": "John Doe",
                "email": "user@email.com",
                "is_active": True,
                "password": "f1edef6a67e7445c8c88d189fd7ff63b",
            }
        }

    def __str__(self):
        return f"{self.id}, {self.username}, {self.email}"


class UserCreate(User):
    password: str = Field(
        None, min_length=6, max_length=16, description="A text value with length between 6 and 16 characters"
    )

    def hash_password(self):
        if not self.password or len(self.password) > 16:
            return

        return pwd_context.hash(self.password)
