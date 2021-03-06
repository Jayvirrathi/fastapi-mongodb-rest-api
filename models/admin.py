from pydantic import BaseModel, Field, EmailStr


class AdminModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Elon Musk",
                "email": "elon@gmail.com",
                "password": "elonmusk"
            }
        }